import pytest


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



class YearDigits:
    """For a given year, show how to calulate an integer using all the digits of the year"""
    def __init__(self, year):
        self.year = year


    @staticmethod
    def digits_of(number):
        if number == 0:
            return [0]  # Special case for 0

        digits = []
        number = abs(number) # handle negative numbers.

        while number > 0:
            digit = number % 10
            digits.insert(0, digit) # Insert at the beginning to maintain order
            number //= 10

        return digits
    
    @staticmethod
    def is_exact_match(target, digit_list):
        if len(digit_list) != 1:
            return False
        
        return target == digit_list[0]


    def is_sum_of_two_digits(target, digit_list):
        if len(digit_list) != 2:
            return False

        return target == sum(digit_list)
        
        
    def try_first_digit_addition(self, year_digits, target):
      first_digit = str(year_digits[0])
      reduced_target = target - year_digits[0]
      remaining_year =int("".join([str(x) for x in year_digits[1:]]))
      return "(" + first_digit + "+" + YearDigits(remaining_year).calculate_for(reduced_target) + ")"
      

    def calculate_for(self, target):
        year_digits = YearDigits.digits_of(self.year)

        if YearDigits.is_exact_match(target, year_digits):
            return f"{target}"
        if YearDigits.is_sum_of_two_digits(target, year_digits):
            return "(" + "+".join([str(x) for x in year_digits]) + ")"
        if len(year_digits) > 2:
          return self.try_first_digit_addition(year_digits, target)
        else:
            raise ValueError("Cannot calculate the target value using the digits of the year.")
