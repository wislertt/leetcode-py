import pytest

from leetcode_py import logged_test

from .helpers import assert_min_swap, run_min_swap
from .solution import Solution


class TestMinimumSwapsToMakeSequencesIncreasing:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([1, 3, 5, 4], [1, 2, 3, 7], 1),
            ([0, 3, 5, 8, 9], [2, 1, 4, 6, 9], 1),
            ([1, 2, 3], [4, 5, 6], 0),
            ([0, 1], [0, 1], 0),
            ([2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8], 0),
            ([3, 2, 5, 6], [1, 4, 4, 7], 1),
            ([15, 6, 11], [3, 24, 25], 1),
            ([2, 5, 6, 9, 10, 15, 16, 18, 22], [3, 4, 8, 9, 10, 15, 16, 19, 23], 0),
            ([8, 11, 12, 16, 17, 24], [1, 4, 13, 16, 21, 24], 0),
            ([7, 6, 15], [2, 10, 24], 1),
            ([16, 20, 24], [6, 18, 22], 0),
            ([2, 6, 14, 16, 23], [3, 7, 8, 16, 19], 0),
            ([2, 6, 15, 16, 13, 21, 20, 23, 25], [0, 10, 7, 10, 17, 15, 23, 24, 25], 3),
            ([0, 2, 14, 12, 25], [1, 7, 11, 18, 16], 1),
            ([1, 4, 8, 11, 18, 24, 25], [0, 3, 7, 11, 17, 19, 23], 0),
            ([6, 16, 21], [11, 9, 20], 1),
            ([3, 22], [2, 19], 0),
            ([2, 7, 5, 7, 16], [3, 3, 16, 24, 25], 1),
        ],
    )
    def test_min_swap(self, nums1: list[int], nums2: list[int], expected: int):
        result = run_min_swap(Solution, nums1, nums2)
        assert_min_swap(result, expected)
