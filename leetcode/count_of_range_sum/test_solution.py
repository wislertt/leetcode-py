import pytest

from leetcode_py import logged_test

from .helpers import assert_count_range_sum, run_count_range_sum
from .solution import Solution


class TestCountOfRangeSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, lower, upper, expected",
        [
            ([-2, 5, -1], -2, 2, 3),
            ([0], 0, 0, 1),
            ([1], 0, 0, 0),
            ([1, 2, 3], 0, 6, 6),
            ([1, 2, 3], 3, 3, 2),
            ([1, 2, 3], 7, 10, 0),
            ([-1, -1, -1], -2, -1, 5),
            ([0, 0, 0], 0, 0, 6),
            ([5], 5, 10, 1),
            ([-5], -10, -5, 1),
            ([-5], -4, 0, 0),
            ([1, -1, 1, -1], 0, 1, 7),
            ([2, -2, 2, -2], -2, 2, 10),
            ([-2, 3, 0, 2, -5, 4], -2, 3, 15),
            ([2147483647, -2147483648, -1, 2], -1, 2, 5),
            ([7], -5, -1, 0),
            ([-5, -3, 6], -9, 8, 6),
            ([-4, -4], -12, -8, 1),
            ([-8, -9, -4, -6], -9, -1, 4),
            ([-8, -9, 3, -3, 9], -2, 10, 6),
            ([9, -9, 3, 7], -8, 7, 6),
            ([-4, 5], 7, 9, 0),
            ([-8], -3, 12, 0),
        ],
    )
    def test_count_range_sum(self, nums: list[int], lower: int, upper: int, expected: int):
        result = run_count_range_sum(Solution, nums, lower, upper)
        assert_count_range_sum(result, expected)
