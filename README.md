# clemency_asm

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
