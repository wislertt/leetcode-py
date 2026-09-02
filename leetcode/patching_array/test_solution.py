import pytest

from leetcode_py import logged_test

from .helpers import assert_min_patches, run_min_patches
from .solution import Solution


class TestPatchingArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, n, expected",
        [
            ([1, 3], 6, 1),
            ([1, 5, 10], 20, 2),
            ([1, 2, 2], 5, 0),
            ([1], 1, 0),
            ([1], 2, 1),
            ([2], 1, 1),
            ([1, 2, 4, 8, 16], 31, 0),
            ([1, 3], 100, 5),
            ([2, 4, 6], 30, 3),
            ([1, 10, 100, 1000], 5000, 9),
            ([1, 2, 31, 33], 2147483647, 28),
            ([1, 2, 4, 13, 43], 100, 2),
            ([10000, 10000, 10000], 10000, 14),
            ([1], 2147483647, 30),
            ([2, 3, 13, 18, 30], 5, 1),
            ([11, 17, 20], 190, 6),
            ([3, 4, 5, 8, 19, 27], 109, 3),
            ([18, 28], 129, 6),
            ([17], 147, 7),
            ([2], 142, 7),
            ([15], 102, 6),
            ([6, 8, 19, 23, 24, 28], 122, 4),
            ([13, 17, 17, 19, 29, 30], 143, 5),
            ([6, 9, 15, 15, 20, 29], 88, 3),
            ([1], 199, 7),
            ([1, 13, 15], 140, 5),
        ],
    )
    def test_min_patches(self, nums: list[int], n: int, expected: int):
        result = run_min_patches(Solution, nums, n)
        assert_min_patches(result, expected)
