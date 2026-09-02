import pytest

from leetcode_py import logged_test

from .helpers import assert_find_unsorted_subarray, run_find_unsorted_subarray
from .solution import Solution


class TestShortestUnsortedContinuousSubarray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 6, 4, 8, 10, 9, 15], 5),
            ([1, 2, 3, 4], 0),
            ([1], 0),
            ([2, 1], 2),
            ([1, 3, 2, 2, 2], 4),
            ([1, 2, 3, 3, 3], 0),
            ([1, 2, 3, 5, 4], 2),
            ([5, 4, 3, 2, 1], 5),
            ([1, 3, 5, 4, 7], 2),
            ([1, 2, 4, 5, 3], 3),
            ([2, 2, 2, 2], 0),
            ([-1, -3, 2, -5], 4),
            ([1, 3, 2, 4, 5, 6, 7, 8, 9], 2),
            ([1, 2, 3, 4, 8, 7, 6, 9, 10], 3),
            ([-3], 0),
            ([-1, 1, -5, 4, 1], 5),
            ([2, 3, 3, -5, -1], 5),
            ([-5, 0, 4, 5, 2], 3),
            ([2, -3, -5, 2, -5], 5),
            ([4, 3, -2], 3),
            ([-5, 0, 1, -3, -3, 5, -5, 5], 6),
            ([1, -2, -2, -2], 4),
        ],
    )
    def test_find_unsorted_subarray(self, nums: list[int], expected: int):
        result = run_find_unsorted_subarray(Solution, nums)
        assert_find_unsorted_subarray(result, expected)
