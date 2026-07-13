import pytest

from leetcode_py import logged_test

from .helpers import assert_tribonacci, run_tribonacci
from .solution import Solution


class TestNThTribonacciNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (0, 0),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 4),
            (5, 7),
            (6, 13),
            (7, 24),
            (8, 44),
            (9, 81),
            (10, 149),
            (12, 504),
            (15, 3136),
            (20, 66012),
            (25, 1389537),
            (30, 29249425),
            (37, 2082876103),
        ],
    )
    def test_tribonacci(self, n: int, expected: int):
        result = run_tribonacci(Solution, n)
        assert_tribonacci(result, expected)
