import pytest

from leetcode_py import logged_test

from .helpers import assert_sorted_array_to_bst, run_sorted_array_to_bst
from .solution import Solution


class TestConvertSortedArrayToBinarySearchTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums",
        [
            ([-10, -3, 0, 5, 9]),
            ([1, 3]),
            ([1]),
            ([1, 2, 3]),
            ([1, 2, 3, 4]),
            ([1, 2, 3, 4, 5, 6, 7]),
            ([0]),
            ([-1, 0, 1]),
            ([1, 2, 3, 4, 5]),
            ([-5, -4, -3, -2, -1]),
            ([1, 2, 3, 4, 5, 6]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ([-100, 100]),
            ([1, 2, 3, 4, 5, 6, 7, 8]),
            ([-9, -7, -5, -3, -1, 1, 3, 5, 7]),
        ],
    )
    def test_sorted_array_to_bst(self, nums: list[int]):
        result = run_sorted_array_to_bst(Solution, nums)
        assert_sorted_array_to_bst(result, nums)
