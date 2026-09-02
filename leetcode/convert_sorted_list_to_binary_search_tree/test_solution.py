import pytest

from leetcode_py import logged_test

from .helpers import assert_sorted_list_to_bst, run_sorted_list_to_bst
from .solution import Solution


class TestConvertSortedListToBinarySearchTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_vals",
        [
            ([-10, -3, 0, 5, 9]),
            ([]),
            ([0]),
            ([1, 3]),
            ([1, 2, 3]),
            ([1, 2, 3, 4]),
            ([1, 2, 3, 4, 5]),
            ([-5, -4, -3, -2, -1]),
            ([-1, 0, 1]),
            ([1, 2, 3, 4, 5, 6]),
            ([1, 2, 3, 4, 5, 6, 7, 8]),
            ([-9, -7, -5, -3, -1, 1, 3, 5, 7]),
            ([-100, 100]),
            ([1, 1, 1, 1]),
            ([0, 0, 1, 1, 2, 2]),
            ([-100000, 0, 100000]),
            ([-8, -2, 5, 5, 8]),
            ([-2, 7]),
        ],
    )
    def test_sorted_list_to_bst(self, head_vals: list[int]):
        result = run_sorted_list_to_bst(Solution, head_vals)
        assert_sorted_list_to_bst(result, head_vals)
