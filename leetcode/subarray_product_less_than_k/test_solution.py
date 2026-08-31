import pytest

from leetcode_py import logged_test

from .helpers import assert_num_subarray_product_less_than_k, run_num_subarray_product_less_than_k
from .solution import Solution


class TestSubarrayProductLessThanK:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([10, 5, 2, 6], 100, 8),
            ([1, 2, 3], 0, 0),
            ([1, 1, 1], 1, 0),
            ([1, 1, 1], 2, 6),
            ([10, 9, 10, 9], 90, 4),
            ([1, 2, 3, 4], 100, 10),
            ([2, 2, 2], 8, 5),
            ([1000], 1000, 0),
            ([1000], 1001, 1),
            ([5, 5, 5, 5], 626, 10),
            ([1], 2, 1),
            ([3, 3, 3], 27, 5),
            ([2, 3, 4], 25, 6),
            ([50, 2, 1, 1, 1], 100, 11),
            ([9, 1, 1, 1, 1, 9], 10, 20),
            ([4, 4, 4, 4], 65, 9),
        ],
    )
    def test_num_subarray_product_less_than_k(self, nums: list[int], k: int, expected: int):
        result = run_num_subarray_product_less_than_k(Solution, nums, k)
        assert_num_subarray_product_less_than_k(result, expected)
