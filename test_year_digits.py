import pytest

def test_2025_0():
    year_calcaulator = YearDigits(2025)

    assert year_calcaulator.calculate_for(0) == "0 = 0 * (2  + 2 + 5)"

@pytest.mark.skip("Not implemented yet")
def test_2025_1():
    year_calcaulator = YearDigits(2025)

    assert year_calcaulator.calculate_for(1) == "1 = 5 - 2 - 2 + 0"

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 1, 1),
    (1, 0, 1)
])
def test_plus_operator(a, b, expected):
    plus = PlusOperator(a, b)
    assert plus.calculate() == expected


def test_only_additions():
    calculator = YearDigits(2025)
    calculator.possible_operators = [PlusOperator,]
    
    assert calculator.calculate_for(9) == "9 = 2 + 0 + 2 + 5" 


def test_recursive_formula():
    formula = PlusOperator(1, PlusOperator(2, 3))
    assert formula.calculate() == 6
    

class YearDigits:
    """For a given year, show how to calulate an integer using all the digits of the year"""
    def __init__(self, year):
        self.year = year
        self.digits = [int(d) for d in str(year)]
        self.possible_operators = [PlusOperator,]

    def calculate_for(self, digit):
        formula = PlusOperator(self.digits[0], 
                    PlusOperator(self.digits[1], 
                        PlusOperator(self.digits[2], self.digits[3])
                        )
                    )
        if formula.calculate() == digit:
            return f"{digit} = {sum}"
        else:
            raise ValueError("No solution found")


class PlusOperator:
    def __init__(self, a, b):
        self.a = a
        self.b = b


    def calculate(self):
        a_result = self.a if isinstance(self.a, int) else self.a.calculate()
        b_result = self.b if isinstance(self.b, int) else self.b.calculate()
        return a_result + b_result
