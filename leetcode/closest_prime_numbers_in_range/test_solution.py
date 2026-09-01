import pytest

from leetcode_py import logged_test

from .helpers import assert_closest_primes, run_closest_primes
from .solution import Solution


class TestClosestPrimeNumbersInRange:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "left, right, expected",
        [
            (10, 19, [11, 13]),
            (4, 6, [-1, -1]),
            (1, 1, [-1, -1]),
            (1, 2, [-1, -1]),
            (1, 3, [2, 3]),
            (2, 2, [-1, -1]),
            (2, 4, [2, 3]),
            (3, 3, [-1, -1]),
            (3, 5, [3, 5]),
            (4, 5, [-1, -1]),
            (8, 12, [-1, -1]),
            (8, 13, [11, 13]),
            (14, 16, [-1, -1]),
            (19, 23, [19, 23]),
            (20, 30, [23, 29]),
            (88, 100, [89, 97]),
            (100, 200, [101, 103]),
            (1, 100, [2, 3]),
            (990, 1010, [991, 997]),
            (999983, 1000000, [-1, -1]),
            (999999, 1000000, [-1, -1]),
            (1, 1000000, [2, 3]),
        ],
    )
    def test_closest_primes(self, left: int, right: int, expected: list[int]):
        result = run_closest_primes(Solution, left, right)
        assert_closest_primes(result, expected)
