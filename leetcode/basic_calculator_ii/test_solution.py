import pytest

from leetcode_py import logged_test

from .helpers import assert_calculate, run_calculate
from .solution import Solution


class TestBasicCalculatorII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("3+2*2", 7),
            (" 3/2 ", 1),
            (" 3+5 / 2 ", 5),
            ("1+1", 2),
            ("1-1", 0),
            ("2*3+4", 10),
            ("10/2", 5),
            ("14-3/2", 13),
            ("0", 0),
            ("100000000/1/1", 100000000),
            ("1*2*3*4*5", 120),
            ("3+2*2*2", 11),
            (" 5 ", 5),
            ("1-1+1", 1),
            ("2/3", 0),
            ("100-10-10", 80),
        ],
    )
    def test_calculate(self, s: str, expected: int):
        result = run_calculate(Solution, s)
        assert_calculate(result, expected)
