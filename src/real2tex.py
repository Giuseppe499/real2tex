# real2tex
# Copyright (C) 2024  Giuseppe Scarlato
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from numbers import Real
import copy

DEFAULT_OPTIONS = {
    "precision": [2, int],
    "multiply_symbol": ["\\cdot", str],
    "no_10_to_the_zero": [True, bool],
}

options = copy.deepcopy(DEFAULT_OPTIONS)


def set_options(**kwargs):
    for key, value in kwargs.items():
        if key in options:
            if isinstance(value, options[key][1]):
                options[key][0] = value
            else:
                raise ValueError(f"Value of {key} must be of type {options[key][1]}")
        else:
            raise ValueError(f"Unknown option {key}")


def get_options() -> dict:
    return {key: options[key][0] for key in options}


def reset_options():
    global options
    options = copy.deepcopy(DEFAULT_OPTIONS)


def scientific_notation(
    num: Real, precision: int = None
) -> tuple[str, str, bool]:
    if precision is None:
        precision = options["precision"][0]
    num_str = f"{num:.{precision}e}"
    mantissa, exponent = num_str.split("e")
    negative_exponent = True if exponent[0] == "-" else False
    exponent = exponent[1:]
    # Remove leading zeros in the exponent
    exponent = exponent.lstrip("0")
    if len(exponent) == 0:
        exponent = "0"
    # Remove trailing zeros in the mantissa
    mantissa = mantissa.rstrip("0")
    # Remove trailing dot in the mantissa
    mantissa = mantissa.rstrip(".")
    # Remove sign if mantissa is zero
    if mantissa == "-0":
        mantissa = "0"
    return mantissa, exponent, negative_exponent


def real2tex(
    num: Real,
    precision: int = None,
    multiply_symbol: str = None,
    no_10_to_the_zero: bool = None,
) -> str:
    if precision is None:
        precision = options["precision"][0]
    if multiply_symbol is None:
        multiply_symbol = options["multiply_symbol"][0]
    if no_10_to_the_zero is None:
        no_10_to_the_zero = options["no_10_to_the_zero"][0]

    mantissa, exponent, negative_exponent = scientific_notation(num, precision)
    if negative_exponent:
        exponent = f"\\minus {exponent}"
    if exponent == "0" and no_10_to_the_zero:
        return f"{mantissa}"
    return f"{mantissa} {multiply_symbol} 10^{{{exponent}}}"
