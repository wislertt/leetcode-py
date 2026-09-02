import pytest

from leetcode_py import logged_test

from .helpers import assert_nth_super_ugly_number, run_nth_super_ugly_number
from .solution import Solution


class TestSuperUglyNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, primes, expected",
        [
            (1, [2, 3, 5], 1),
            (12, [2, 7, 13, 19], 32),
            (1, [2], 1),
            (2, [2], 2),
            (5, [2], 16),
            (10, [2], 512),
            (1, [3, 11, 13], 1),
            (2, [3, 11, 13], 3),
            (3, [3, 11, 13], 9),
            (7, [3, 11, 13], 33),
            (4, [2, 3, 5], 4),
            (10, [2, 3, 5], 12),
            (11, [2, 3, 5], 15),
            (25, [2, 3, 5], 54),
            (50, [2, 3, 5, 7], 120),
            (100, [2, 3, 5, 7, 11, 13], 210),
            (300, [2, 7, 13, 19], 268912),
            (1000, [2, 3, 5, 7, 11, 13, 17, 19], 7350),
            (6, [2, 5, 7, 11, 13], 8),
            (15, [5, 7], 2401),
        ],
    )
    def test_nth_super_ugly_number(self, n: int, primes: list[int], expected: int):
        result = run_nth_super_ugly_number(Solution, n, primes)
        assert_nth_super_ugly_number(result, expected)
