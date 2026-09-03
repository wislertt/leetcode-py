import pytest

from leetcode_py import logged_test

from .helpers import assert_dominant_index, run_dominant_index
from .solution import Solution


class TestLargestNumberAtLeastTwiceOfOthers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 6, 1, 0], 1),
            ([1, 2, 3, 4], -1),
            ([1], 0),
            ([0], 0),
            ([1, 0], 0),
            ([0, 1], 1),
            ([2, 1], 0),
            ([1, 2], 1),
            ([100, 0], 0),
            ([0, 100], 1),
            ([50, 25, 24], 0),
            ([50, 25, 25, 26], -1),
            ([3, 6], 1),
            ([4, 7], -1),
            ([99, 49, 0, 12], 0),
            ([1, 1, 2], 2),
            ([10, 5, 20, 9], 2),
            ([3, 2, 1], -1),
            ([7, 40, 49, 28, 68, 17], -1),
            ([33, 16, 5, 17, 5, 86, 27, 21, 24, 23, 0, 14], 5),
            ([49, 88], -1),
            ([3, 84, 2, 29], 1),
            ([5, 88, 35], 1),
            ([31, 37, 35, 11, 51, 44, 43, 35, 35, 15, 10, 36], -1),
            ([49, 34, 29, 14, 11, 81, 6, 33, 46, 11, 41, 4], -1),
            ([30, 83, 33, 28, 6, 0, 29, 31, 2, 6, 9, 9], 1),
            ([32, 15, 17, 6, 8, 45, 46, 45, 11, 76, 29], -1),
            ([23, 0, 31, 4, 3, 10, 57], -1),
            ([9, 32, 8, 24, 98, 29], 4),
            ([52, 41], -1),
        ],
    )
    def test_dominant_index(self, nums: list[int], expected: int):
        result = run_dominant_index(Solution, nums)
        assert_dominant_index(result, expected)
