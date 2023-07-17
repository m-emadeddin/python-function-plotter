from plotter import Plotter
import pytest


@pytest.mark.parametrize("function , min_x, max_x , expected", [
    ("x", -1, 1, 1),           # Valid
    ("_x", -1, 1, 0),          # Invalid: Starts with underscore
    ("sin(x))", -1, 1, 0),     # Invalid: Extra closing parenthesis
    ("sin(x)", -1, 1, 1),      # Valid
    ("x*5+4*2", -1, 1, 1),     # Valid
    ("3 + 4 -", -1, 1, 0),     # Invalid: Incomplete expression
    ("5 * x^2 +", -1, 1, 0),   # Invalid: Incomplete expression
    ("x - y", -1, 1, 0),       # Invalid: Invalid variable name 'y'
    ("2x", -1, 1, 0),          # Invalid: Missing multiplication operator
    ("sqrt(4)", -1, 1, 1),     # Valid: Square root function
    ("exp(2)", -1, 1, 1),      # Valid: Exponential function
    ("log(x)", -1, 1, 1),      # Valid: Logarithmic function - Warning, log(x) only valid x -> ]0 , inf[
    ("abs(x)", -1, 1, 1),      # Valid: Absolute value function
    ("5 % 2", -1, 1, 1),       # Valid: Modulo operation
    ("2**3", -1, 1, 1),        # Valid: Exponentiation
    ("5 / 0", -1, 1, 0),       # Invalid: Division by zero
])

def test_valid_function(function ,min_x, max_x, expected):
    valid = 1
    try:
        Plotter().get_values(function, min_x, max_x)
    except:
        valid = 0
    assert  valid == expected


