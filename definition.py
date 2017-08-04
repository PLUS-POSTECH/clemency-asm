instruction_data = {
    'AD': (
        'Add',
        ('0000000', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'ADC': (
        'Add With Carry',
        ('0100000', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'ADCIM': (
        'Add Immediate Multi Reg With Carry',
        ('0100010', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7'),
    ),
    'ADCM': (
        'Add Multi Reg With Carry',
        ('0100010', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'ADF': (
        'Add Floating Point',
        ('0000001', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'ADFM': (
        'Add Floating Point Multi Reg',
        ('0000011', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'ADI': (
        'Add Immediate',
        ('0000000', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7'),
    ),
    'ADIM': (
        'Add Immediate Multi Reg',
        ('0000010', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7'),
    ),
    'ADM': (
        'Add Multi Reg',
        ('0000010', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'AN': (
        'And',
        ('0010100', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'ANI': (
        'And Immediate',
        ('0010100', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7'),
    ),

    'ANM': (
        'And Multi Reg',
        ('0010110', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'ADCI': (
        'Add Immediate With Carry',
        ('0100000', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7'),
    ),
    'BN': (
        'Branch: Not Equal / Not Zero',
        ('110000', '0000', '$0'),
        ('Offset17',),
    ),
    'BE': (
        'Branch: Equal / Zero',
        ('110000', '0001', '$0'),
        ('Offset17',),
    ),
    'BL': (
        'Branch: Less Than',
        ('110000', '0010', '$0'),
        ('Offset17',),
    ),
    'BLE': (
        'Branch: Less than or Equal',
        ('110000', '0011', '$0'),
        ('Offset17',),
    ),
    'BG': (
        'Branch: Greater Than',
        ('110000', '0100', '$0'),
        ('Offset17',),
    ),
    'BGE': (
        'Branch: Greater Than or Equal',
        ('110000', '0101', '$0'),
        ('Offset17',),
    ),
    'BNO': (
        'Branch: Not Overflow',
        ('110000', '0110', '$0'),
        ('Offset17',),
    ),
    'BO': (
        'Branch: Overflow',
        ('110000', '0111', '$0'),
        ('Offset17',),
    ),
    'BNS': (
        'Branch: Not Signed',
        ('110000', '1000', '$0'),
        ('Offset17',),
    ),
    'BS': (
        'Branch: Signed',
        ('110000', '1001', '$0'),
        ('Offset17',),
    ),
    'BSL': (
        'Branch: Signed Less Than',
        ('110000', '1010', '$0'),
        ('Offset17',),
    ),
    'BSLE': (
        'Branch: Signed Less Than or Equal',
        ('110000', '1011', '$0'),
        ('Offset17',),
    ),
    'BSG': (
        'Branch: Signed Greater Than',
        ('110000', '1100', '$0'),
        ('Offset17',),
    ),
    'BSGE': (
        'Branch: Signed Greater Than or Equal',
        ('110000', '1101', '$0'),
        ('Offset17',),
    ),
    'B': (
        'Branch: Always',
        ('110000', '1111', '$0'),
        ('Offset17',),
    ),
    'BF': (
        'Bit Flip',
        ('101001100', '$0', '$1', '1000000', '$UF'),
        ('rA', 'rB'),
    ),
    'BFM': (
        'Bit Flip Multi Reg',
        ('101001110', '$0', '$1', '1000000', '$UF'),
        ('rA', 'rB'),
    ),
    'BRN': (
        'Branch Register: Not Equal / Not Zero',
        ('110010', '0000', '$0', '000'),
        ('rA',),
    ),
    'BRE': (
        'Branch Register: Equal / Zero',
        ('110010', '0001', '$0', '000'),
        ('rA',),
    ),
    'BRL': (
        'Branch Register: Less Than',
        ('110010', '0010', '$0', '000'),
        ('rA',),
    ),
    'BRLE': (
        'Branch Register: Less Than or Equal',
        ('110010', '0011', '$0', '000'),
        ('rA',),
    ),
    'BRG': (
        'Branch Register: Greatre Than',
        ('110010', '0100', '$0', '000'),
        ('rA',),
    ),
    'BRGE': (
        'Branch Register: Greatre Than or Equal',
        ('110010', '0101', '$0', '000'),
        ('rA',),
    ),
    'BRNO': (
        'Branch Register: Not Overflow',
        ('110010', '0110', '$0', '000'),
        ('rA',),
    ),
    'BRO': (
        'Branch Register: Overflow',
        ('110010', '0111', '$0', '000'),
        ('rA',),
    ),
    'BRNS': (
        'Branch Register: Not Signed',
        ('110010', '1000', '$0', '000'),
        ('rA',),
    ),
    'BRS': (
        'Branch Register: Signed',
        ('110010', '1001', '$0', '000'),
        ('rA',),
    ),
    'BRSL': (
        'Branch Register: Signed Less Than',
        ('110010', '1010', '$0', '000'),
        ('rA',),
    ),
    'BRSLE': (
        'Branch Register: Signed Less Than or Equal',
        ('110010', '1011', '$0', '000'),
        ('rA',),
    ),
    'BRSG': (
        'Branch Register: Greater Than',
        ('110010', '1100', '$0', '000'),
        ('rA',),
    ),
    'BRSGE': (
        'Branch Register: Greater Than or Equal',
        ('110010', '1101', '$0', '000'),
        ('rA',),
    ),
    'BR': (
        'Branch Register: Always',
        ('110010', '1111', '$0', '000'),
        ('rA',),
    ),
    'BRA': (
        'Branch Absolute',
        ('111000100', '$0'),
        ('Location27',),
    ),
    'BRR': (
        'Branch Relative',
        ('111000000', '$0'),
        ('Offset27',),
    ),
    'CN': (
        'Call Conditional: Not Equal / Not Zero',
        ('110101', '0000', '$0'),
        ('Offset17',),
    ),
    'CE': (
        'Call Conditional: Equal / Zero',
        ('110101', '0001', '$0'),
        ('Offset17',),
    ),
    'CL': (
        'Call Conditional: Less Than',
        ('110101', '0010', '$0'),
        ('Offset17',),
    ),
    'CLE': (
        'Call Conditional: Less Than or Equal',
        ('110101', '0011', '$0'),
        ('Offset17',),
    ),
    'CG': (
        'Call Conditional: Greater Than',
        ('110101', '0100', '$0'),
        ('Offset17',),
    ),
    'CGE': (
        'Call Conditional: Greater Than or Equal',
        ('110101', '0101', '$0'),
        ('Offset17',),
    ),
    'CNO': (
        'Call Conditional: Not Overflow',
        ('110101', '0110', '$0'),
        ('Offset17',),
    ),
    'CO': (
        'Call Conditional: Overflow',
        ('110101', '0111', '$0'),
        ('Offset17',),
    ),
    'CNS': (
        'Call Conditional: Not Signed',
        ('110101', '1000', '$0'),
        ('Offset17',),
    ),
    'CS': (
        'Call Conditional: Signed',
        ('110101', '1001', '$0'),
        ('Offset17',),
    ),
    'CSL': (
        'Call Conditional: Signed Less Than',
        ('110101', '1010', '$0'),
        ('Offset17',),
    ),
    'CSLE': (
        'Call Conditional: Signed Less Than or Equal',
        ('110101', '1011', '$0'),
        ('Offset17',),
    ),
    'CSG': (
        'Call Conditional: Signed Greater Than',
        ('110101', '1100', '$0'),
        ('Offset17',),
    ),
    'CSGE': (
        'Call Conditional: Signed Greater Than or Equal',
        ('110101', '1101', '$0'),
        ('Offset17',),
    ),
    'C': (
        'Call Conditional: Always',
        ('110101', '1111', '$0'),
        ('Offset17',),
    ),
    'CAA': (
        'Call Absolute',
        ('111001100', '$0'),
        ('Location27',),
    ),
    'CAR': (
        'Call Relative',
        ('111001000', '$0'),
        ('Offset27',),
    ),
    'CM': (
        'Compare',
        ('10111000', '$0', '$1'),
        ('rA', 'rB'),
    ),
    'CMF': (
        'Compare Floating Point',
        ('10111010', '$0', '$1'),
        ('rA', 'rB'),
    ),
    'CMFM': (
        'Compare Floating Point Multi Reg',
        ('10111110', '$0', '$1'),
        ('rA', 'rB'),
    ),
    'CMI': (
        'Compare Immediate',
        ('10111001', '$0', '$1'),
        ('rA', 'IMM14'),
    ),
    'CMIM': (
        'Compare Immediate Multi Reg',
        ('10111101', '$0', '$1'),
        ('rA', 'IMM14'),
    ),
    'CMM': (
        'Compare Multi Reg',
        ('10111100', '$0', '$1'),
        ('rA', 'rB'),
    ),
    'CRN': (
        'Call Register Conditional: Not Equal / Not Zero',
        ('110111', '0000', '$0', '000'),
        ('rA',),
    ),
    'CRE': (
        'Call Register Conditional: Equal / Zero',
        ('110111', '0001', '$0', '000'),
        ('rA',),
    ),
    'CRL': (
        'Call Register Conditional: Less Than',
        ('110111', '0010', '$0', '000'),
        ('rA',),
    ),
    'CRLE': (
        'Call Register Conditional: Less Than or Equal',
        ('110111', '0011', '$0', '000'),
        ('rA',),
    ),
    'CRG': (
        'Call Register Conditional: Greater Than',
        ('110111', '0100', '$0', '000'),
        ('rA',),
    ),
    'CRGE': (
        'Call Register Conditional: Greater Than or Equal',
        ('110111', '0101', '$0', '000'),
        ('rA',),
    ),
    'CRNO': (
        'Call Register Conditional: Not Overflow',
        ('110111', '0110', '$0', '000'),
        ('rA',),
    ),
    'CRO': (
        'Call Register Conditional: Overflow',
        ('110111', '0111', '$0', '000'),
        ('rA',),
    ),
    'CRNS': (
        'Call Register Conditional: Not Signed',
        ('110111', '1000', '$0', '000'),
        ('rA',),
    ),
    'CRS': (
        'Call Register Conditional: Signed',
        ('110111', '1001', '$0', '000'),
        ('rA',),
    ),
    'CRSL': (
        'Call Register Conditional: Signed Less Than',
        ('110111', '1010', '$0', '000'),
        ('rA',),
    ),
    'CRSLE': (
        'Call Register Conditional: Signed Less Than or Equal',
        ('110111', '1011', '$0', '000'),
        ('rA',),
    ),
    'CRSG': (
        'Call Register Conditional: Greater Than',
        ('110111', '1100', '$0', '000'),
        ('rA',),
    ),
    'CRSGE': (
        'Call Register Conditional: Greater Than or Equal',
        ('110111', '1101', '$0', '000'),
        ('rA',),
    ),
    'CR': (
        'Call Register Conditional: Always',
        ('110111', '1111', '$0', '000'),
        ('rA',),
    ),
    'DBRK': (
        'Debug Break',
        ('111111111111111111'),
        (),
    ),
    'DI': (
        'Disable Interrupts',
        ('101000000101', '$0', '0'),
        ('rA',),
    ),
    'DMT': (
        'Direct Memory Transfer',
        ('0110100', '$0', '$1', '$2', '00000'),
        ('rA', 'rB', 'rC'),
    ),
    'DV': (
        'Divide',
        ('0001100', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'DVF': (
        'Divide Floating Point',
        ('0001101', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'DVFM': (
        'Divide Floating Point Multi Reg',
        ('0001111', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'DVI': (
        'Divide Immediate',
        ('0001100', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7'),
    ),
    'DVIM': (
        'Divide Immediate Multi Reg',
        ('0001110', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7'),
    ),
    'DVIS': (
        'Divide Immediate Signed',
        ('0001100', '$0', '$1', '$2', '11', '$UF'),
        ('rA', 'rB', 'IMM7'),
    ),
    'DVISM': (
        'Divide Immediate Signed Multi Reg',
        ('0001110', '$0', '$1', '$2', '11', '$UF'),
        ('rA', 'rB', 'IMM7'),
    ),
    'DVM': (
        'Divide Multi Reg',
        ('0001110', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'DVS': (
        'Divide Signed',
        ('0001100', '$0', '$1', '$2', '0010', '$UF'),
        ('rA', 'rB', 'rC')
    ),
    'DVSM': (
        'Divide Signed Multi Reg',
        ('0001110', '$0', '$1', '$2', '0010', '$UF'),
        ('rA', 'rB', 'rC')
     ),
    'EI': (
        'Enable Interrupts',
        ('101000000100', '$0', '0'),
        ('rA',)
    ),
    'FTI': (
        'Float to Integer',
        ('101000101', '$0', '$1', '00000000'),
        ('rA', 'rB')
     ),
    'FTIM': (
        'Float to Integer Multi Reg',
        ('101000111', '$0', '$1', '00000000'),
        ('rA', 'rB')
     ),
    'HT': (
        'Halt',
        ('101000000011000000'),
        ()
    ),
    'IR': (
        'Interrupt Return',
        ('101000000001000000'),
        ()
    ),
    'ITF': (
        'Integer to Float',
        ('101000100', '$0', '$1', '00000000'),
        ('rA', 'rB')
     ),
    'ITFM': (
        'Integer to Float Multi Reg',
        ('101000110', '$0', '$1', '00000000'),
        ('rA', 'rB')
     ),
    'LDS': (
        'Load Single',
        ('1010100', '$0', '$1', '$3', '00', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),
    'LDSI': (
        'Load Single Inc',
        ('1010100', '$0', '$1', '$3', '01', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),
    'LDSD': (
        'Load Single Dec',
        ('1010100', '$0', '$1', '$3', '10', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),
    'LDT': (
        'Load Tri',
        ('1010110', '$0', '$1', '$3', '00', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),
    'LDTI': (
        'Load Tri Inc',
        ('1010110', '$0', '$1', '$3', '01', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),
    'LDTD': (
        'Load Tri Dec',
        ('1010110', '$0', '$1', '$3', '10', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),
    'LDW': (
        'Load Word',
        ('1010101', '$0', '$1', '$3', '00', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),
    'LDWI': (
        'Load Word Inc',
        ('1010101', '$0', '$1', '$3', '01', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),
    'LDWD': (
        'Load Word Dec',
        ('1010101', '$0', '$1', '$3', '10', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),
    'MD': (
        'Modulus',
        ('0010000', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'MDF': (
        'Modulus Floating Point',
        ('0010001', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'MDFM': (
        'Modulus Floating Point Multi Reg',
        ('0010011', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'MDI': (
        'Modulus Immediate',
        ('0010000', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'MDIM': (
        'Modulus Immediate Multi Reg',
        ('0010010', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'MDIS': (
        'Modulus Immediate Signed',
        ('0010000', '$0', '$1', '$2', '11', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'MDISM': (
        'Modulus Immediate Signed Multi Reg',
        ('0010010', '$0', '$1', '$2', '11', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'MDM': (
        'Modulus Multi Reg',
        ('0010010', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'MDS': (
        'Modulus Signed',
        ('0010000', '$0', '$1', '$2', '0010', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'MDSM': (
        'Modulus Signed Multi Reg',
        ('0010010', '$0', '$1', '$2', '0010', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'MH': (
        'Move High',
        ('10001', '$0', '$1'),
        ('rA', 'IMM17')
    ),

    'ML': (
        'Move Low',
        ('10010', '$0', '$1'),
        ('rA', 'IMM17')
    ),

    'MS': (
        'Move Low Signed',
        ('10011', '$0', '$1'),
        ('rA', 'IMM17')
    ),

    'MU': (
        'Multiply',
        ('0001000', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'MUF': (
        'Multiply Floating Point',
        ('0001001', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'MUFM': (
        'Multiply Floating Point Multi Reg',
        ('0001011', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'MUI': (
        'Multiply Immediate',
        ('0001000', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'MUIM': (
        'Multiply Immediate Multi Reg',
        ('0001010', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'MUIS': (
        'Multiply Immediate Signed',
        ('0001000', '$0', '$1', '$2', '11', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'MUISM': (
        'Multiply Immediate Signed Multi Reg',
        ('0001010', '$0', '$1', '$2', '11', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'MUM': (
        'Multiply Multi Reg',
        ('0001010', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'MUS': (
        'Multiply Signed',
        ('0001000', '$0', '$1', '$2', '0010', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'MUSM': (
        'Multiply Signed Multi Reg',
        ('0001010', '$0', '$1', '$2', '0010', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'NG': (
        'Negate',
        ('101001100', '$0', '$1', '0000000', '$UF'),
        ('rA', 'rB')
    ),

    'NGF': (
        'Negate Floating Point',
        ('101001101', '$0', '$1', '0000000', '$UF'),
        ('rA', 'rB')
    ),

    'NGFM': (
        'Negate Floating Point Multi Reg',
        ('101001111', '$0', '$1', '0000000', '$UF'),
        ('rA', 'rB')
    ),

    'NGM': (
        'Negate Multi Reg',
        ('101001110', '$0', '$1', '0000000', '$UF'),
        ('rA', 'rB')
    ),

    'NT': (
        'Not',
        ('101001100', '$0', '$1', '0100000', '$UF'),
        ('rA', 'rB')
    ),

    'NTM': (
        'Not Multi Reg',
        ('101001110', '$0', '$1', '0100000', '$UF'),
        ('rA', 'rB')
    ),

    'OR': (
        'Or',
        ('0011000', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'ORI': (
        'Or Immediate',
        ('0011000', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'ORM': (
        'Or Multi Reg',
        ('0011010', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'RE': (
        'Return',
        ('101000000000000000'),
        ()
    ),

    'RF': (
        'Read Flags',
        ('101000001100', '$0', '0'),
        ('rA',)
    ),

    'RL': (
        'Rotate Left',
        ('0110000', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),
    'RLI': (
        'Rotate Left Immediate',
        ('1000000', '$0', '$1', '$2', '00', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'RLIM': (
        'Rotate Left Immediate Multi Reg',
        ('1000010', '$0', '$1', '$2', '00', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'RLM': (
        'Rotate Left Multi Reg',
        ('0110010', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'RMP': (
        'Read Memory Protection',
        ('1010010', '$0', '$1', '0000000000'),
        ('rA', 'rB')
    ),

    'RND': (
        'Random',
        ('101001100', '$0', '000001100000', '$UF'),
        ('rA',)
    ),

    'RNDM': (
        'Random Multi Reg',
        ('101001110', '$0', '000001100000', '$UF'),
        ('rA',)
    ),

    'RR': (
        'Rotate Right',
        ('0110001', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),
    'RRI': (
        'Rotate Right Immediate',
        ('1000001', '$0', '$1', '$2', '00', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'RRIM': (
        'Rotate Right Immediate Multi Reg',
        ('1000011', '$0', '$1', '$2', '00', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'RRM': (
        'Rotate Right Multi Reg',
        ('0110011', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'SA': (
        'Shift Arithemetic Right',
        ('0101101', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),
    'SAI': (
        'Shift Arithemetic Right Immediate',
        ('0111101', '$0', '$1', '$2', '00', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'SAIM': (
        'Shift Arithemetic Right Immediate Multi Reg',
        ('0111111', '$0', '$1', '$2', '00', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'SAM': (
        'Shift Arithemetic Right Multi Reg',
        ('0101111', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'SB': (
        'Substract',
        ('0000100', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'SBC': (
        'Substract With Carry',
        ('0100100', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'SBCI': (
        'Substract Immediate With Carry',
        ('0100100', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'SBCIM': (
        'Substract Immediate Multi Reg With Carry',
        ('0100110', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'SBCM': (
        'Substract Multi Reg With Carry',
        ('0100110', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'SBF': (
        'Substract Floating Point',
        ('0000101', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'SBFM': (
        'Substract Floating Point Multi Reg',
        ('0000111', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'SBI': (
        'Substract Immediate',
        ('0000100', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'SBIM': (
        'Substract Immediate Multi Reg',
        ('0000110', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'SBM': (
        'Substract Multi Reg',
        ('0000110', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'SES': (
        'Sign Extend Single',
        ('101000000111', '$0', '$1', '00000'),
        ('rA', 'rB')
    ),

    'SEW': (
        'Sign Extend Word',
        ('101000001000', '$0', '$1', '00000'),
        ('rA', 'rB')
    ),

    'SF': (
        'Set Flags',
        ('101000001011', '$0', '0'),
        ('rA',)
    ),

    'SL': (
        'Shift Left',
        ('0101000', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'SLI': (
        'Shift Left Immediate',
        ('0111000', '$0', '$1', '$2', '00', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'SLIM': (
        'Shift Left Immediate Multi Reg',
        ('0111010', '$0', '$1', '$2', '00', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'SLM': (
        'Shift Left Multi Reg',
        ('0101010', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'SMP': (
        'Set Memory Protection',
        ('1010010', '$0', '$1', '1', '$2', '0000000'),
        ('rA', 'rB', 'IMM2')
    ),

    'SR': (
        'Shift Right',
        ('0101001', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'SRI': (
        'Shift Right Immediate',
        ('0111001', '$0', '$1', '$2', '00', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'SRIM': (
        'Shift Right Immediate Multi Reg',
        ('0111011', '$0', '$1', '$2', '00', '$UF'),
        ('rA', 'rB', 'IMM7')
    ),

    'SRM': (
        'Shift Right Multi Reg',
        ('0101011', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC')
    ),

    'STS': (
        'Store Single',
        ('1011000', '$0', '$1', '$3', '00', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),

    'STSI': (
        'Store Single Inc',
        ('1011000', '$0', '$1', '$3', '01', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),

    'STSD': (
        'Store Single Dec',
        ('1011000', '$0', '$1', '$3', '10', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),

    'STT': (
        'Store Tri',
        ('1011010', '$0', '$1', '$3', '00', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),

    'STTI': (
        'Store Tri Inc',
        ('1011010', '$0', '$1', '$3', '01', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),

    'STTD': (
        'Store Tri Dec',
        ('1011010', '$0', '$1', '$3', '10', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),

    'STW': (
        'Store Word',
        ('1011001', '$0', '$1', '$3', '00', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),
    'STWI': (
        'Store Word Inc',
        ('1011001', '$0', '$1', '$3', '01', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),
    'STWD': (
        'Store Word Dec',
        ('1011001', '$0', '$1', '$3', '10', '$2', '000'),
        ('rA', ['rB', 'Offset27', 'IMM5'])
    ),

    'WT': (
        'Wait',
        ('101000000010000000'),
        (),
    ),

    'XR': (
        'Xor',
        ('0011100', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'XRI': (
        'Xor Immediate',
        ('0011100', '$0', '$1', '$2', '01', '$UF'),
        ('rA', 'rB', 'IMM7'),
    ),
    'XRM': (
        'Xor Multi Reg',
        ('0011110', '$0', '$1', '$2', '0000', '$UF'),
        ('rA', 'rB', 'rC'),
    ),
    'ZES': (
        'Zero Extend Single',
        ('101000001001', '$0', '$1', '00000'),
        ('rA', 'rB'),
    ),
    'ZEW': (
        'Zero Extend Word',
        ('101000001010', '$0', '$1', '00000'),
        ('rA', 'rB'),
    )
}
