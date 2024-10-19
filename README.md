# real2tex

`real2tex` is a Python module that converts a real number
to a string of LaTeX code that represents the number
in scientific notation.

## Installation
```
pip install real2tex
```

## Usage
```python
from real2tex import real2tex

tex = real2tex(1.2345e-6, precision=2)
print(tex) # "1.23 \cdot 10^{\minus 6}"
```