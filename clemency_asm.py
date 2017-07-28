import binascii
import re
import sys

from definition import instruction_data

def pad_bin(value, size):
    # Immediate value maximum is 27 bit
    assert -67108864 <= value < 134217728
    if value < 0:
        value = value & 0xffffffff
    bin_str = bin(value)[2:].zfill(size)
    return bin_str[-size:]

def register_name_to_bit(name):
    name = name.lower()
    for i in range(29):
        if name == 'r%02d' % i:
            return pad_bin(i, 5)
    if name == 'st':
        return pad_bin(29, 5)
    elif name == 'ra':
        return pad_bin(30, 5)
    elif name == 'pc':
        return pad_bin(31, 5)
    raise Exception('Unknown Register')

class BitWriter(object):
    def __init__(self):
        self.data = ''
        self.cnt = 0

    def write(self, bin_str):
        # calculate trailing character
        remain_bits = ''
        if self.cnt != 0:
            remain_bits = bin(ord(self.data[-1]))[2:].zfill(8)[:self.cnt]
            self.data = self.data[:-1]
        remain_bits += bin_str

        # add padding
        pad_len = len(remain_bits) % 8
        if pad_len != 0:
            remain_bits += '0'*(8-pad_len)

        # apply data
        hex_str = '%0*X' % ((len(remain_bits) + 3) // 4, int(remain_bits, 2))
        if len(hex_str) % 2 == 1:
            hex_str = '0' + hex_str
        self.data += binascii.unhexlify(hex_str)
        self.cnt = (self.cnt + len(bin_str)) % 8


class Instruction(object):
    def __init__(self, description, format, parse):
        self.description = description
        self.format = format
        self.parse = parse
        self.data = []

        for c in parse:
            if type(c) is list:
                self.data += c
            else:
                self.data += (c,)

        def data_size(index):
            assert 0 <= index < len(self.data)
            pattern = self.data[index]
            if pattern == 'rA' or pattern == 'rB' or pattern == 'rC':
                return 5
            elif pattern.startswith('IMM'):
                size = int(pattern[3:])
                return size
            elif pattern.startswith('Offset'):
                size = int(pattern[6:])
                return size
            elif pattern.startswith('Location'):
                size = int(pattern[8:])
                return size
            else:
                raise Exception("Unknown data format")

        bits = 0
        for pattern in self.format:
            if pattern[0] == '0' or pattern[0] == '1':
                assert(all(c == '0' or c == '1' for c in pattern))
                bits += len(pattern)
            elif pattern[0] == '$':
                if pattern == '$UF':
                    bits += 1
                else:
                    idx = int(pattern[1:])
                    bits += data_size(idx)

        assert bits % 9 == 0
        self.size = bits / 9

    def to_bitstring(self, pc, tail, uf, label_dictionary):
        delimiters = []
        for (i, pattern) in enumerate(self.parse[:-1]):
            if i+1 < len(self.parse) and type(self.parse[i+1]) is list:
                delimiters += (',[', '+', ',', ']')
            else:
                delimiters.append(',')

        prev_index = 0
        input_data = []
        for delimiter in delimiters:
            delim_index = tail.index(delimiter, prev_index)
            input_data.append(tail[prev_index:delim_index])
            prev_index = delim_index+len(delimiter)
        input_data.append(tail[prev_index:])

        converted_data = []
        for (i, pattern) in enumerate(self.data):
            if pattern == 'rA' or pattern == 'rB' or pattern == 'rC':
                converted_data.append(register_name_to_bit(input_data[i]))
            elif pattern.startswith('IMM'):
                size = int(pattern[3:])
                value = int(input_data[i], base=0)
                converted_data.append(pad_bin(value, size))
            elif pattern.startswith('Offset'):
                size = int(pattern[6:])
                assert input_data[i] in label_dictionary
                value = label_dictionary[input_data[i]] - pc
                converted_data.append(pad_bin(value, size))
            elif pattern.startswith('Location'):
                size = int(pattern[8:])
                try:
                    value = int(input_data[i], base=0)
                except ValueError:
                    assert input_data[i] in label_dictionary
                    value = label_dictionary[input_data[i]]
                converted_data.append(pad_bin(value, size))
            else:
                raise Exception("Unknown data format")

        bit_str = ''
        for pattern in self.format:
            if pattern[0] == '0' or pattern[0] == '1':
                assert(all(c == '0' or c == '1' for c in pattern))
                bit_str += pattern
            elif pattern[0] == '$':
                if pattern == '$UF':
                    bit_str += '1' if uf else '0'
                else:
                    idx = int(pattern[1:])
                    bit_str += converted_data[idx]

        assert len(bit_str) % 9 == 0

        # shuffle middle endian
        shuffled = ''
        while len(bit_str) >= 27:
            shuffled += bit_str[9:18] + bit_str[0:9] + bit_str[18:27]
            bit_str = bit_str[27:]
        if len(bit_str) == 18:
            shuffled += bit_str[9:18] + bit_str[0:9]
        else:
            shuffled += bit_str

        return shuffled


instructions = {}
for k, v in instruction_data.iteritems():
    instructions[k] = Instruction(*v)

def asm(text):
    def strip_line(line):
        line = line.strip()
        # remove spaces around +
        line = re.sub(r'\s*\+\s*', r'+', line)
        # replace multiple spaces
        line = re.sub(r'\s+', ' ', line)
        # remove spaces after comma
        line = re.sub(r', ', ',', line)
        return line
    lines = map(strip_line, text.split('\n'))

    # label resolving
    current_offset = 0
    labels = {}
    for line in lines:
        if line == '':
            continue
        if line[-1] == ':':
            # Label
            label_name = line[:-1]
            assert label_name.isalnum()
            labels[label_name] = current_offset
        else:
            # Instruction
            splitted = line.split(' ')

            instruction_kind = splitted[0].upper()
            if instruction_kind[-1] == '.':
                uf = 1
                instruction_kind = instruction_kind[:-1]
            else:
                uf = 0
            assert instruction_kind in instructions

            instruction = instructions[instruction_kind]
            current_offset += instruction.size

    # assembling
    current_offset = 0
    result = BitWriter()
    for line in lines:
        if line == '':
            continue
        if line[-1] == ':':
            # Label
            pass
        else:
            # Instruction
            splitted = line.split(' ')
            assert(len(splitted) == 1 or len(splitted) == 2)

            instruction_kind = splitted[0].upper()
            if instruction_kind[-1] == '.':
                uf = 1
                instruction_kind = instruction_kind[:-1]
            else:
                uf = 0
            assert instruction_kind in instructions

            instruction = instructions[instruction_kind]
            result.write(
                instruction.to_bitstring(
                    current_offset,
                    splitted[1] if len(splitted) == 2 else '',
                    uf,
                    labels
                )
            )
            current_offset += instruction.size

    return result.data


if __name__ == "__main__":
    if len(sys.argv) < 3:
       print 'Usage: {} input_file output_file'.format(sys.argv[0])
       exit(0)

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    with open(input_file_name, 'rb') as f:
        data = f.read()

    with open(output_file_name, 'w') as f:
        f.write(asm(data))
