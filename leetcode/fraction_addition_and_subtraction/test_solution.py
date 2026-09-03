import pytest

from leetcode_py import logged_test

from .helpers import assert_fraction_addition, run_fraction_addition
from .solution import Solution


class TestFractionAdditionAndSubtraction:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "expression, expected",
        [
            ("-1/2+1/2", "0/1"),
            ("-1/2+1/2+1/3", "1/3"),
            ("1/3-1/2", "-1/6"),
            ("1/2", "1/2"),
            ("5/1", "5/1"),
            ("-3/4", "-3/4"),
            ("2/1+3/1", "5/1"),
            ("-1/2-1/2", "-1/1"),
            ("1/1-1/1", "0/1"),
            ("1/3+1/4-1/6", "5/12"),
            ("7/10+1/2-3/5", "3/5"),
            ("1/2-1/3+1/6", "1/3"),
            ("-5/2+5/2-1/7", "-1/7"),
            ("9/10-1/10", "4/5"),
            ("1/1-1/2", "1/2"),
            ("-7/3+2/3", "-5/3"),
            ("5/3-10/3", "-5/3"),
            ("7/6-3/8+8/3", "83/24"),
            ("2/5+7/10-7/3-3/7", "-349/210"),
            ("9/8-1/9", "73/72"),
        ],
    )
    def test_fraction_addition(self, expression: str, expected: str):
        result = run_fraction_addition(Solution, expression)
        assert_fraction_addition(result, expected)
