import pytest

from leetcode_py import logged_test

from .helpers import assert_dot_product, run_dot_product
from .solution import SparseVector


class TestDotProductOfTwoSparseVectors:
    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([1, 0, 0, 2, 3], [0, 3, 0, 4, 0], 8),
            ([0, 1, 0, 0, 0], [0, 0, 0, 0, 2], 0),
            ([0, 1, 0, 0, 2, 0, 0], [1, 0, 0, 0, 3, 0, 4], 6),
            ([5], [7], 35),
            ([0], [9], 0),
            ([0, 0, 0], [0, 0, 0], 0),
            ([100, 0, 100], [100, 100, 0], 10000),
            ([1, 2, 3, 4], [1, 2, 3, 4], 30),
            ([0, 0, 0, 0, 1], [1, 0, 0, 0, 0], 0),
            ([0, 7, 0, 7, 0, 7], [7, 7, 0, 0, 7, 0], 49),
            ([3, 0, 4], [0, 5, 0], 0),
            ([2, 0, 0, 9, 0, 0, 1, 0], [0, 0, 3, 9, 0, 8, 0, 0], 81),
            ([10, 20, 0, 0, 30], [0, 20, 0, 10, 30], 1300),
            ([1, 0, 2, 0, 3, 0, 4, 0, 5], [0, 6, 0, 7, 3, 0, 1, 0, 2], 23),
            ([0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1], [2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0], 0),
            ([0, 1, 2, 0, 4, 5, 0, 7], [7, 0, 5, 4, 0, 2, 1, 0], 20),
        ],
    )
    def test_dot_product(self, nums1: list[int], nums2: list[int], expected: int):
        result = run_dot_product(SparseVector, nums1, nums2)
        assert_dot_product(result, expected)
