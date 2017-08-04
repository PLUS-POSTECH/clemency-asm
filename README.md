# clemency_asm

[cLEMENCy architecture](https://blog.legitbs.net/2017/07/the-clemency-architecture.html) is a custom architecture created by legitBS for DEFCON 25. This repository contains an assembler for cLEMENCy architecture, which was developed during the contest period.

## Usage
### As a standalone binary
```bash
$ python clemency_asm.py sample/test.casm output.bin
```

### As a library
```python
from clemency_asm import asm
asm('AD r00, r00, r01')
```

## Macro Instruction
### MA!: Move All
```
MA! rA, IMM
==
ML rA, IMM & 0b1111111111
MH rA, IMM >> 10
```
