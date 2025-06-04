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


    @staticmethod
    def is_sum_of_two_digits(target, digit_list):
        if len(digit_list) != 2:
            return False

        return target == sum(digit_list)
    
    @staticmethod
    def is_difference_of_two_digits(target, digit_list):
        if len(digit_list) != 2:
            return False

        return target == abs(digit_list[0] - digit_list[1])
        
        
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
        if YearDigits.is_difference_of_two_digits(target, year_digits):
            # Return the subtraction in the correct order: larger - smaller
            if year_digits[0] - year_digits[1] == target:
                return f"({year_digits[0]}-{year_digits[1]})"
            else:
                return f"({year_digits[1]}-{year_digits[0]})"
        if len(year_digits) > 2:
          return self.try_first_digit_addition(year_digits, target)
        else:
            raise ValueError("Cannot calculate the target value using the digits of the year.")