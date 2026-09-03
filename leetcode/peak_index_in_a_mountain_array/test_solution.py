import pytest

from leetcode_py import logged_test

from .helpers import assert_peak_index_in_mountain_array, run_peak_index_in_mountain_array
from .solution import Solution


class TestPeakIndexInAMountainArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([0, 1, 0], 1),
            ([0, 2, 1, 0], 1),
            ([0, 10, 5, 2], 1),
            ([3, 4, 5, 1], 2),
            ([24, 69, 100, 99, 79, 78, 67, 36, 26, 19], 2),
            ([0, 1, 2, 3, 2, 1, 0], 3),
            ([3, 9, 4], 1),
            ([1, 2, 1], 1),
            ([0, 3, 2, 1], 1),
            ([18, 29, 38, 59, 98, 100, 74, 23, 17, 5], 5),
            ([999999, 1000000, 0], 1),
            ([0, 1000000, 999999], 1),
            ([30, 46, 57, 63, 72, 77, 97, 98, 67, 51, 34, 12], 7),
            ([56, 90, 14], 1),
            ([25, 32, 91, 92, 96, 53, 47, 41, 29, 2], 4),
            ([4, 21, 47, 57, 78, 61, 43, 19, 11], 4),
            ([21, 91, 18], 1),
            ([26, 73, 77, 91, 23, 22], 3),
        ],
    )
    def test_peak_index_in_mountain_array(self, arr: list[int], expected: int):
        result = run_peak_index_in_mountain_array(Solution, arr)
        assert_peak_index_in_mountain_array(result, expected)
