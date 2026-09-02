import pytest

from leetcode_py import logged_test

from .helpers import assert_super_pow, run_super_pow
from .solution import Solution


class TestSuperPow:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, [3], 8),
            (2, [1, 0], 1024),
            (1, [4, 3, 3, 8, 5, 2], 1),
            (2, [1], 2),
            (3, [1], 3),
            (2, [0], 1),
            (2147483647, [2, 0, 0], 1198),
            (2, [9, 9, 9, 9], 540),
            (12, [1, 2, 3], 818),
            (7, [1, 0, 0], 574),
            (100, [5], 753),
            (1337, [1], 0),
            (2, [2, 0, 0, 0], 32),
            (5, [6], 918),
            (10, [1, 5], 160),
            (9, [8, 7, 6, 5], 25),
        ],
    )
    def test_super_pow(self, a: int, b: list[int], expected: int):
        result = run_super_pow(Solution, a, b)
        assert_super_pow(result, expected)
