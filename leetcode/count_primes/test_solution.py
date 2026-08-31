import pytest

from leetcode_py import logged_test

from .helpers import assert_count_primes, run_count_primes
from .solution import Solution


class TestCountPrimes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (10, 4),
            (0, 0),
            (1, 0),
            (2, 0),
            (3, 1),
            (4, 2),
            (5, 2),
            (6, 3),
            (7, 3),
            (8, 4),
            (9, 4),
            (20, 8),
            (30, 10),
            (50, 15),
            (100, 25),
            (150, 35),
            (1000, 168),
            (4999, 668),
        ],
    )
    def test_count_primes(self, n: int, expected: int):
        result = run_count_primes(Solution, n)
        assert_count_primes(result, expected)
