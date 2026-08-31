import pytest

from leetcode_py import logged_test

from .helpers import assert_diff_ways_to_compute, run_diff_ways_to_compute
from .solution import Solution


class TestDifferentWaysToAddParentheses:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "expression, expected",
        [
            ("2-1-1", [0, 2]),
            ("2*3-4*5", [-34, -14, -10, -10, 10]),
            ("0", [0]),
            ("5", [5]),
            ("1+1", [2]),
            ("2-1", [1]),
            ("3*3", [9]),
            ("1+2+3", [6, 6]),
            ("2*3+4", [10, 14]),
            ("1-2+3", [2, -4]),
            ("11", [11]),
            ("1*2*3", [6, 6]),
            ("2*2-3*4", [-8, -20, -8, -8, 4]),
            ("10+20", [30]),
            ("99*99", [9801]),
            ("1+2*3-4", [-3, -1, 3, 3, 5]),
        ],
    )
    def test_diff_ways_to_compute(self, expression: str, expected: list[int]):
        result = run_diff_ways_to_compute(Solution, expression)
        assert_diff_ways_to_compute(result, expected)
