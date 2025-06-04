import pytest
from year_digits import YearDigits, Operator, ExactMatchOperator, AdditionOperator


# Test to validate the operator classes work correctly
def test_operator_classes_integration():
    """Test that the new operator class structure produces the same results"""
    year_calculator = YearDigits(111)
    
    # Test that operators can be accessed individually  
    exact_match_op = ExactMatchOperator()
    addition_op = AdditionOperator()
    
    year_digits = YearDigits.digits_of(111)  # [1, 1, 1]
    
    # ExactMatchOperator should return None for multiple digits
    assert exact_match_op.try_calculate(3, year_digits, YearDigits) is None
    
    # AdditionOperator should handle the recursive case
    result = addition_op.try_calculate(3, year_digits, YearDigits)
    assert result == "(1+(1+1))"


def test_extensibility_demonstration():
    """Demonstrate that new operators can be easily added"""
    
    # Example of how a new operator could be implemented
    class MultiplicationOperator(Operator):
        def try_calculate(self, target, year_digits, year_digits_calculator):
            # Simple example: multiply all digits together
            if len(year_digits) >= 2:
                product = 1
                for digit in year_digits:
                    product *= digit
                if product == target:
                    return "(" + "*".join([str(x) for x in year_digits]) + ")"
            return None
    
    # Test the new operator
    mult_op = MultiplicationOperator()
    year_digits = [2, 3]  # 2 * 3 = 6
    result = mult_op.try_calculate(6, year_digits, YearDigits)
    assert result == "(2*3)"
    
    # Should return None when not applicable
    assert mult_op.try_calculate(5, year_digits, YearDigits) is None


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



