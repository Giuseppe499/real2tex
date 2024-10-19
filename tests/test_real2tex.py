import pytest
from real2tex import scientific_notation, real2tex

def test_scientific_notation_float():
    assert scientific_notation(1e-14, 2) == ('1', '14', True)
    assert scientific_notation(1.23e4, 2) == ('1.23', '4', False)
    assert scientific_notation(1.2300e4, 4) == ('1.23', '4', False)
    assert scientific_notation(1.2300e4, 6) == ('1.23', '4', False)
    assert scientific_notation(0.000123, 3) == ('1.23', '4', True)
    assert scientific_notation(123456, 2) == ('1.23', '5', False)
    assert scientific_notation(123456, 4) == ('1.2346', '5', False)
    assert scientific_notation(.0, 2) == ('0', '0', False)
    assert scientific_notation(-.0, 2) == ('0', '0', False)

def test_real2tex_float():
    assert real2tex(1e-14, 2) == '1 \\cdot 10^{\\minus 14}'
    assert real2tex(1.23e4, 2) == '1.23 \\cdot 10^{4}'
    assert real2tex(1.2300e4, 4) == '1.23 \\cdot 10^{4}'
    assert real2tex(1.2300e4, 6) == '1.23 \\cdot 10^{4}'
    assert real2tex(0.000123, 3) == '1.23 \\cdot 10^{\\minus 4}'
    assert real2tex(123456, 2) == '1.23 \\cdot 10^{5}'
    assert real2tex(1.23e4, 2, "*") == '1.23 * 10^{4}'
    assert real2tex(.0, 2) == '0'
    assert real2tex(-.0, 2) == '0'
    assert real2tex(1.1, 0) == '1'
    assert real2tex(-1.1, 0) == '-1'
    assert real2tex(1.1, 0, no_10_to_the_zero=False) == '1 \\cdot 10^{0}'


def test_scientific_notation_integers():
    assert scientific_notation(1000, 2) == ('1', '3', False)
    assert scientific_notation(-1000, 2) == ('-1', '3', False)
    assert scientific_notation(0, 2) == ('0', '0', False)
    assert scientific_notation(1, 2) == ('1', '0', False)
    assert scientific_notation(-1, 2) == ('-1', '0', False)
    assert scientific_notation(123456789, 2) == ('1.23', '8', False)
    assert scientific_notation(-123456789, 2) == ('-1.23', '8', False)
    assert scientific_notation(123456789, 4) == ('1.2346', '8', False)
    assert scientific_notation(-123456789, 4) == ('-1.2346', '8', False)

def test_real2tex_integers():
    assert real2tex(1000, 2) == '1 \\cdot 10^{3}'
    assert real2tex(-1000, 2) == '-1 \\cdot 10^{3}'
    assert real2tex(0, 2) == '0'
    assert real2tex(1, 2) == '1'
    assert real2tex(-1, 2) == '-1'
    assert real2tex(123456789, 2) == '1.23 \\cdot 10^{8}'
    assert real2tex(-123456789, 2) == '-1.23 \\cdot 10^{8}'
    assert real2tex(123456789, 4) == '1.2346 \\cdot 10^{8}'
    assert real2tex(-123456789, 4) == '-1.2346 \\cdot 10^{8}'

if __name__ == "__main__":
    pytest.main()