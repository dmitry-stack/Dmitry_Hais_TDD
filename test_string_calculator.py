import pytest
from string_calculator import StringCalculator


@pytest.fixture
def calc():
    return StringCalculator()


def test_empty_string_returns_zero(calc):
    assert calc.Calculate("") == 0


@pytest.mark.parametrize("arg, expected", [
    ("3", 3),
    ("42", 42),
    ("007", 7),
    ("   21", 21)

])

def test_single_number_returns_value(calc, arg, expected):
    assert calc.Calculate(arg) == expected



def test_two_numbers_sum(calc):
    assert calc.Calculate("1,2") == 3

def test_newline_sum(calc):
    assert calc.Calculate("1\n2,3") == 6


def test_multiple_numbers(calc):
    assert calc.Calculate("1,2,3,4") == 10


@pytest.mark.parametrize("arg, expected", [
    ("2,1001", 2),
    ("1000,2", 1002),
])
def test_ignore_large_numbers(calc, arg, expected):
    assert calc.Calculate(arg) == expected


def test_single_character_delimiter(calc):
    assert calc.Calculate("//;\n1;2") == 3


def test_long_delimiter(calc):
    assert calc.Calculate("//[***]\n1***2***3") == 6


def test_multiple_delimiters(calc):
    assert calc.Calculate("//[;][#]\n1;2#3") == 6


def test_negative_numbers_raise_exception(calc):

    with pytest.raises(Exception) as excinfo:
        calc.Calculate("1,-2,3")

    assert "Negatives not allowed: [-2]" in str(excinfo.value)


def test_multiple_negative_numbers(calc):

    with pytest.raises(Exception) as excinfo:
        calc.Calculate("//;\n-1;2;-5")

    assert "Negatives not allowed: [-1, -5]" in str(excinfo.value)