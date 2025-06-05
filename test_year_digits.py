import pytest
from year_digits import YearDigits


@pytest.mark.skip(reason="Too complex early example")
def test_2025_0():
    year_calcaulator = YearDigits(2025)

    assert year_calcaulator.calculate_for(0) == "0 = 0 * (2  + 2 + 5)"


def test_year_1():
    year_calculator = YearDigits(1)

    assert year_calculator.calculate_for(1) == "1"


def test_year_10_make_1():
    year_calculator = YearDigits(10)

    assert year_calculator.calculate_for(1) == "(1+0)"



def test_2_1_exception():
    year_calculator = YearDigits(2)
    with pytest.raises(ValueError):
        year_calculator.calculate_for(1)

        
def test_year_111_make_3():
    year_calculator = YearDigits(111)

    assert year_calculator.calculate_for(3) == "(1+(1+1))"
    
def test_year_5432_make_14():
  year_calculator = YearDigits(5432)
  
  assert year_calculator.calculate_for(14) == "(5+(4+(3+2)))"


def test_year_54_make_1():
    year_calculator = YearDigits(54)
    
    assert year_calculator.calculate_for(1) == "(5-4)"


def test_year_32_make_1():
    year_calculator = YearDigits(32)
    
    assert year_calculator.calculate_for(1) == "(3-2)"


def test_year_522_make_1():
    year_calculator = YearDigits(522)
    
    assert year_calculator.calculate_for(1) == "(5-(2+2))"



