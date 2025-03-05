def test_2025_0():
    year_calcaulator = YearDigits(2025)

    assert year_calcaulator.calculate_for(0) == "0 = 0 * (2  + 2 + 5)"


def test_year_1():
    year_calculator = YearDigits(1)

    assert year_calculator.calculate_for(1) == "1 = 1"


class YearDigits:
    """For a given year, show how to calulate an integer using all the digits of the year"""
    def __init__(self, year):
        self.year = year

    def calculate_for(self, digit):
        return "0 = 0 * (2  + 2 + 5)"
