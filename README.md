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

Is it also possible to change the default arguments of the module (`precision`, `multiply_symbol`,
...) with the
`set_options` function. Furthermore, the current options can be retrieved with
the `get_options` function and reset to the default values with the
`reset_options` function.
```python
import real2tex as rt

tex = rt.real2tex(1.2345e-6)
print(tex) # "1.23 \cdot 10^{\minus 6}"

rt.set_options(precision=4, multiply_symbol="*")
tex = rt.real2tex(1.2345e-6)
print(tex) # "1.2345 * 10^{\minus 6}"

print(rt.get_options()) # Get current options

rt.reset_options() # Reset options to default
```