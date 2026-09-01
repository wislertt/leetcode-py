import pytest

from leetcode_py import logged_test

from .helpers import assert_kth_smallest_product, run_kth_smallest_product
from .solution import Solution


class TestKthSmallestProductOfTwoSortedArrays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, k, expected",
        [
            ([2, 5], [3, 4], 2, 8),
            ([-4, -2, 0, 3], [2, 4], 6, 0),
            ([-2, -1, 0, 1, 2], [-3, -1, 2, 4, 5], 3, -6),
            ([1], [1], 1, 1),
            ([-1], [1], 1, -1),
            ([0], [0], 1, 0),
            ([-5, 5], [-5, 5], 1, -25),
            ([-5, 5], [-5, 5], 4, 25),
            ([2, 3], [-1, 0, 1], 1, -3),
            ([-3, -2], [-1, 2], 3, 2),
            ([1, 2, 3], [-1, 1], 5, 2),
            ([-2, 0, 2], [3], 1, -6),
            ([100000], [-100000], 1, -10000000000),
            ([-1, 1, 3, 6], [-4, -1, 0, 1, 2], 6, -2),
            ([5], [-3], 1, -15),
            ([-1], [-5, -1, -1, 5, 6], 3, 1),
            ([-6, 4], [-2], 2, 12),
            ([-6, -6, 4, 6], [-5, -4], 4, -16),
            ([-6, -5, 0, 3, 4], [-4, -1, 2], 5, -4),
            ([-2, 1], [-5, 0, 3], 1, -6),
        ],
    )
    def test_kth_smallest_product(self, nums1: list[int], nums2: list[int], k: int, expected: int):
        result = run_kth_smallest_product(Solution, nums1, nums2, k)
        assert_kth_smallest_product(result, expected)
