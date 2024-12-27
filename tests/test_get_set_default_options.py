import pytest
from real2tex import real2tex, set_options, get_options, reset_options


def test_default_options():
    default_options = get_options()
    assert default_options["precision"] == 2
    assert default_options["multiply_symbol"] == "\\cdot"
    assert default_options["no_10_to_the_zero"] == True


def test_set_options():
    set_options(precision=3, multiply_symbol="*", no_10_to_the_zero=False)
    options = get_options()
    assert options["precision"] == 3
    assert options["multiply_symbol"] == "*"
    assert options["no_10_to_the_zero"] == False
    reset_options()

    set_options(precision=3)
    options = get_options()
    assert options["precision"] == 3
    assert options["multiply_symbol"] == "\\cdot"
    assert options["no_10_to_the_zero"] == True
    reset_options()

    set_options(multiply_symbol="*")
    options = get_options()
    assert options["precision"] == 2
    assert options["multiply_symbol"] == "*"
    assert options["no_10_to_the_zero"] == True
    reset_options()

    set_options(no_10_to_the_zero=False)
    options = get_options()
    assert options["precision"] == 2
    assert options["multiply_symbol"] == "\\cdot"
    assert options["no_10_to_the_zero"] == False
    reset_options()

    set_options(precision=4, multiply_symbol="*")
    options = get_options()
    assert options["precision"] == 4
    assert options["multiply_symbol"] == "*"
    assert options["no_10_to_the_zero"] == True
    reset_options()


def test_set_invalid_option():
    with pytest.raises(ValueError):
        set_options(invalid_option=123)


def test_set_invalid_type():
    with pytest.raises(ValueError):
        set_options(precision="three")


def test_reset_options():
    set_options(precision=3, multiply_symbol="*", no_10_to_the_zero=False)
    reset_options()
    options = get_options()
    assert options["precision"] == 2
    assert options["multiply_symbol"] == "\\cdot"
    assert options["no_10_to_the_zero"] == True


def test_changed_options():
    set_options(precision=3, multiply_symbol="*", no_10_to_the_zero=False)
    assert real2tex(0.00012345) == "1.234 * 10^{\\minus 4}"
    assert real2tex(1e-14, 2) == "1 * 10^{\\minus 14}"
    assert real2tex(1.23e4, 2, multiply_symbol="\\cdot") == "1.23 \\cdot 10^{4}"
    assert real2tex(1.2300e4, 4) == "1.23 * 10^{4}"
    assert real2tex(1.2300e4, 6) == "1.23 * 10^{4}"
    assert real2tex(0.000123) == "1.23 * 10^{\\minus 4}"
    assert real2tex(123456, 2) == "1.23 * 10^{5}"
    assert real2tex(1.23e4, 2, "*") == "1.23 * 10^{4}"
    assert real2tex(0.0, 2) == "0 * 10^{0}"
    assert real2tex(-0.0, 2) == "0 * 10^{0}"
    assert real2tex(1.1, 0) == "1 * 10^{0}"
    assert real2tex(-1.1, 0) == "-1 * 10^{0}"
    assert real2tex(1.1, 0) == "1 * 10^{0}"
    assert real2tex(1.1, 0, no_10_to_the_zero=True) == "1"
    reset_options()
    assert real2tex(1e-14, 2) == "1 \\cdot 10^{\\minus 14}"
    assert real2tex(1.23e4, 2) == "1.23 \\cdot 10^{4}"
    assert real2tex(1.2300e4, 4) == "1.23 \\cdot 10^{4}"
    assert real2tex(1.2300e4, 6) == "1.23 \\cdot 10^{4}"
    assert real2tex(0.000123, 3) == "1.23 \\cdot 10^{\\minus 4}"
    assert real2tex(123456, 2) == "1.23 \\cdot 10^{5}"
    assert real2tex(1.23e4, 2, "*") == "1.23 * 10^{4}"
    assert real2tex(0.0, 2) == "0"
    assert real2tex(-0.0, 2) == "0"
    assert real2tex(1.1, 0) == "1"
    assert real2tex(-1.1, 0) == "-1"
    assert real2tex(1.1, 0, no_10_to_the_zero=False) == "1 \\cdot 10^{0}"
