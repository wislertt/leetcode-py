import pytest

from leetcode_py import logged_test

from .helpers import assert_find_difference, run_find_difference
from .solution import Solution


class TestFindTheDifferenceOfTwoArrays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
            ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
            ([1], [1], [[], []]),
            ([1], [2], [[1], [2]]),
            ([-1000, 1000], [-1000, -1000], [[1000], []]),
            ([0, 0, 0], [0, 0, 0], [[], []]),
            ([1, 2, 3], [4, 5, 6], [[1, 2, 3], [4, 5, 6]]),
            ([1, 1, 1, 1], [1, 1, 1, 1], [[], []]),
            ([-5, -4, -3], [3, 4, 5], [[-5, -4, -3], [3, 4, 5]]),
            ([1, 2, 2, 3], [3, 3, 4], [[1, 2], [4]]),
            ([7], [7, 7, 7], [[], []]),
            ([1000, 999, -1000], [-1000, 0], [[999, 1000], [0]]),
            ([5, 2, -3, 0], [1, -5, -1, 6, -1, 0, 1], [[-3, 2, 5], [-5, -1, 1, 6]]),
            ([-2], [4, 0, 0, 3, -5, -6], [[-2], [-6, -5, 0, 3, 4]]),
            ([-2, 4, -3, 1], [5, -2, 6, 2], [[-3, 1, 4], [2, 5, 6]]),
            ([5, -3, 0, -6, -6, 0, -3], [3, 6, -1], [[-6, -3, 0, 5], [-1, 3, 6]]),
        ],
    )
    def test_find_difference(self, nums1: list[int], nums2: list[int], expected: list[list[int]]):
        result = run_find_difference(Solution, nums1, nums2)
        assert_find_difference(result, expected)
