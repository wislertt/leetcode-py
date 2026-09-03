import pytest

from leetcode_py import logged_test

from .helpers import assert_nth_magical_number, run_nth_magical_number
from .solution import Solution


class TestNthMagicalNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, a, b, expected",
        [
            (1, 2, 2, 2),
            (1, 2, 3, 2),
            (2, 2, 4, 4),
            (2, 3, 5, 5),
            (4, 2, 3, 6),
            (5, 2, 4, 10),
            (7, 5, 7, 21),
            (10, 2, 5, 16),
            (13, 4, 6, 40),
            (50, 2, 4, 100),
            (1000, 9, 12, 6000),
            (31415, 2718, 2818, 43479846),
            (100000000, 7, 11, 452941174),
            (123456789, 12, 18, 111111097),
            (999999999, 39999, 40000, 999847507),
            (1000000000, 2, 3, 499999993),
            (1000000000, 40000, 39998, 999860007),
            (1000000000, 40000, 40000, 999720007),
        ],
    )
    def test_nth_magical_number(self, n: int, a: int, b: int, expected: int):
        result = run_nth_magical_number(Solution, n, a, b)
        assert_nth_magical_number(result, expected)
