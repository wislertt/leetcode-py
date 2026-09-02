import pytest

from leetcode_py import logged_test

from .helpers import assert_rearrange_array, run_rearrange_array
from .solution import Solution


class TestRearrangeArrayElementsBySign:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 1, -2, -5, 2, -4], [3, -2, 1, -5, 2, -4]),
            ([-1, 1], [1, -1]),
            ([1, -1], [1, -1]),
            ([1, 2, -1, -2], [1, -1, 2, -2]),
            ([5, -3], [5, -3]),
            ([-3, 5], [5, -3]),
            ([1, 2, 3, -1, -2, -3], [1, -1, 2, -2, 3, -3]),
            ([-1, -2, -3, 1, 2, 3], [1, -1, 2, -2, 3, -3]),
            ([4, 5, -6, -7, 8, -9], [4, -6, 5, -7, 8, -9]),
            ([10, -20], [10, -20]),
            ([-20, 10], [10, -20]),
            ([2, 4, 6, -1, -3, -5], [2, -1, 4, -3, 6, -5]),
            ([-2, 4, -6, 8, -10, 12], [4, -2, 8, -6, 12, -10]),
            ([1, -2, 3, -4], [1, -2, 3, -4]),
            ([100000, -100000], [100000, -100000]),
            ([-70, 35], [35, -70]),
            ([-91, 79, -3, 33], [79, -91, 33, -3]),
            ([-25, 77, -73, 13], [77, -25, 13, -73]),
            ([-33, -38, 96, 26], [96, -33, 26, -38]),
            ([-6, 88], [88, -6]),
        ],
    )
    def test_rearrange_array(self, nums: list[int], expected: list[int]):
        result = run_rearrange_array(Solution, nums)
        assert_rearrange_array(result, expected)
