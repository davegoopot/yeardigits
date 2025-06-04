from abc import ABC, abstractmethod


class _Operator(ABC):
    """Abstract base class for calculation operators"""
    
    @abstractmethod
    def try_calculate(self, target, year_digits):
        """
        Try to calculate the target using this operator.
        Returns the calculation string if successful, None if not applicable.
        """
        pass


class _ExactMatchOperator(_Operator):
    """Operator for exact match when target equals a single digit"""
    
    def try_calculate(self, target, year_digits):
        if len(year_digits) != 1:
            return None
        
        if target == year_digits[0]:
            return f"{target}"
        
        return None


class _AdditionOperator(_Operator):
    """Operator for addition-based calculations"""
    
    def try_calculate(self, target, year_digits):
        # Try sum of two digits
        if len(year_digits) == 2 and target == sum(year_digits):
            return "(" + "+".join([str(x) for x in year_digits]) + ")"
        
        # Try first digit addition for more than 2 digits
        if len(year_digits) > 2:
            first_digit = str(year_digits[0])
            reduced_target = target - year_digits[0]
            remaining_year = int("".join([str(x) for x in year_digits[1:]]))
            remaining_calculation = YearDigits(remaining_year).calculate_for(reduced_target)
            return "(" + first_digit + "+" + remaining_calculation + ")"
        
        return None


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
    
    def calculate_for(self, target):
        year_digits = YearDigits.digits_of(self.year)
        
        # List of operators to try in order
        operators = [
            _ExactMatchOperator(),
            _AdditionOperator()
        ]
        
        # Try each operator in turn
        for operator in operators:
            result = operator.try_calculate(target, year_digits)
            if result is not None:
                return result
        
        # If no operator worked, raise an error
        raise ValueError("Cannot calculate the target value using the digits of the year.")