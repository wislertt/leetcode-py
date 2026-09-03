import pytest

from leetcode_py import logged_test

from .helpers import assert_find_length, run_find_length
from .solution import Solution


class TestMaximumLengthOfRepeatedSubarray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([1, 2, 3, 2, 1], [3, 2, 1, 4, 7], 3),
            ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0], 5),
            ([1], [1], 1),
            ([1], [2], 0),
            ([1, 2], [2, 1], 1),
            ([1, 2, 3], [1, 2, 3], 3),
            ([1, 2, 3], [3, 2, 1], 1),
            ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10], 0),
            ([70, 39, 41, 42, 43], [39, 41, 42, 43, 70], 4),
            ([0, 1, 1, 1, 1], [1, 0, 1, 0, 1], 2),
            ([1, 0, 0, 0, 1], [1, 0, 0, 0, 1], 5),
            ([5, 5, 5, 5], [5], 1),
            ([3], [1, 2, 3], 1),
            ([2, 2, 2, 2, 2], [2, 2], 2),
            ([1, 2, 1, 2, 1, 2], [2, 1, 2, 1, 2, 1], 5),
            ([100, 99, 98], [98, 99, 100], 1),
            ([0], [0], 1),
            ([1, 2, 3, 4], [5, 1, 2, 3, 4, 6], 4),
            ([1, 3, 3], [1, 3, 3, 2, 3, 2], 3),
            ([3, 3, 0, 1, 0, 2], [0, 2, 1, 0, 0, 3], 2),
            ([1], [3, 0, 0, 1, 3, 3], 1),
            ([2, 3], [2, 0, 3, 2, 3, 0], 2),
            ([0, 0, 3, 3], [3, 1, 2, 2], 1),
            ([0, 1, 1, 0, 3], [3, 1, 3], 1),
        ],
    )
    def test_find_length(self, nums1: list[int], nums2: list[int], expected: int):
        result = run_find_length(Solution, nums1, nums2)
        assert_find_length(result, expected)
