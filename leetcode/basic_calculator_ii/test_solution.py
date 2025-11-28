import pytest

from leetcode_py import logged_test

from .helpers import assert_calculate, run_calculate
from .solution import Solution


class TestBasicCalculatorIi:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("s, expected", [])
    def test_calculate(self, s: str, expected: int):
        result = run_calculate(Solution, s)
        assert_calculate(result, expected)
