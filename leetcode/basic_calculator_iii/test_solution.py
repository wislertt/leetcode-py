import pytest

from leetcode_py import logged_test

from .helpers import assert_calculate, run_calculate
from .solution import Solution


class TestBasicCalculatorIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("1+1", 2),
            ("6-4/2", 4),
            ("2*(5+5*2)/3+(6/2+8)", 21),
            ("1", 1),
            ("7", 7),
            ("1+2*3-4", 3),
            ("14/3", 4),
            ("7/2", 3),
            ("1-(-7)", 8),
            ("2*(3+4)", 14),
            ("(1+(4+5+2)-3)+(6+8)", 23),
            ("100/10/2", 5),
            ("5-2*3/6+8/4*2", 8),
            ("3*(4+5*(2+1))/6", 9),
            ("(2+6*3+5-(3*14/7+2)*5)+3", -12),
            ("48/(2*(3+5))", 3),
            ("10-2-3", 5),
            ("(((1)))", 1),
            ("2*3+5/6*3+15", 21),
            ("1*2-3/4+5*6-7*8+9/10", -24),
        ],
    )
    def test_calculate(self, s: str, expected: int):
        result = run_calculate(Solution, s)
        assert_calculate(result, expected)
