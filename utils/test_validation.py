import pytest
from validation import Validation


@pytest.mark.parametrize("function_input, min_x, max_x", [
    ("", "-1", "1"),                  # Empty function input
    ("x", "", "1"),                   # Empty min_x
    ("x", "-1", ""),                  # Empty max_x
    ("   ", "-1", "1"),               # Whitespace function input
    ("x", "abc", "1"),                # Invalid min_x (non-numeric)
    ("x", "-1", "xyz"),               # Invalid max_x (non-numeric)
    ("x", "5", "5"),                  # min_x equals max_x
    ("x", "10", "-10"),               # min_x greater than max_x
    ("5 * x**2", "-1", "1"),          # Invalid math expression with '^' instead of '**'
    ("eval(x)", "-1", "1"),           # Invalid math expression containing blocked keyword 'eval'
    ("5*x", "-inf", "inf"),           # Extremely large or small min_x or max_x
])
def test_validate_invalid(function_input, min_x, max_x):
    validation = Validation(function_input, min_x, max_x)
    assert not validation.validate()

