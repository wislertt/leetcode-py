import pytest

from leetcode_py import logged_test

from .helpers import assert_find_missing_ranges, run_find_missing_ranges
from .solution import Solution


class TestMissingRanges:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, lower, upper, expected",
        [
            ([0, 1, 3, 50, 75], 0, 99, [[2, 2], [4, 49], [51, 74], [76, 99]]),
            ([-1], -1, -1, []),
            ([], 1, 1, [[1, 1]]),
            ([], -3, -1, [[-3, -1]]),
            ([1], 1, 1, []),
            ([2], 0, 4, [[0, 1], [3, 4]]),
            ([0, 1, 2, 3], 0, 3, []),
            ([-5, -3, -1], -5, 0, [[-4, -4], [-2, -2], [0, 0]]),
            ([5], 0, 5, [[0, 4]]),
            ([0], 0, 5, [[1, 5]]),
            ([1, 2], 0, 9, [[0, 0], [3, 9]]),
            ([-1000000000], -1000000000, 1000000000, [[-999999999, 1000000000]]),
            ([0, 1000000000], -1000000000, 1000000000, [[-1000000000, -1], [1, 999999999]]),
            ([], 0, 0, [[0, 0]]),
            ([3], 1, 5, [[1, 2], [4, 5]]),
        ],
    )
    def test_find_missing_ranges(
        self, nums: list[int], lower: int, upper: int, expected: list[list[int]]
    ):
        result = run_find_missing_ranges(Solution, nums, lower, upper)
        assert_find_missing_ranges(result, expected)
