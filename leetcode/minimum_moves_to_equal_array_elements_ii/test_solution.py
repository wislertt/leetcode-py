import pytest

from leetcode_py import logged_test

from .helpers import assert_min_moves2, run_min_moves2
from .solution import Solution


class TestMinimumMovesToEqualArrayElementsII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3], 2),
            ([1, 10, 2, 9], 16),
            ([1], 0),
            ([0], 0),
            ([5, 5, 5, 5], 0),
            ([1, 2], 1),
            ([1, 1, 2], 1),
            ([1, 2, 3, 4], 4),
            ([3, 1, 2], 2),
            ([-1, 0, 1], 2),
            ([-5, -3, -1], 4),
            ([-1000000000, 1000000000], 2000000000),
            ([1, 1000000000], 999999999),
            ([-1000000000, 0, 1000000000], 2000000000),
            ([1, 0, 0, 8, 6], 14),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 25),
            ([0, 0, 0, 1], 1),
            ([7, 7, 7, 8], 1),
            ([2, -5], 7),
            ([-7], 0),
            ([8], 0),
            ([-2, -5, 1, -9, -4], 13),
            ([2, 1, -4], 6),
            ([-9, 6, -8, -4, -8, -9, -2], 26),
            ([-2, 1, 1, 3, -1, -5, -1], 13),
            ([-5, -9, -2, -10, 9, -2], 29),
        ],
    )
    def test_min_moves2(self, nums: list[int], expected: int):
        result = run_min_moves2(Solution, nums)
        assert_min_moves2(result, expected)
