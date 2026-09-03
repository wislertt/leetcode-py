import pytest

from leetcode_py import logged_test

from .helpers import assert_construct_maximum_binary_tree, run_construct_maximum_binary_tree
from .solution import Solution


class TestMaximumBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected_list",
        [
            ([3, 2, 1, 6, 0, 5], [6, 3, 5, None, 2, 0, None, None, 1]),
            ([3, 2, 1], [3, None, 2, None, 1]),
            ([1], [1]),
            ([1, 2], [2, 1]),
            ([2, 1], [2, None, 1]),
            ([2, 1, 3], [3, 2, None, None, 1]),
            ([5, 4, 3, 2, 1], [5, None, 4, None, 3, None, 2, None, 1]),
            ([1, 2, 3, 4, 5], [5, 4, None, 3, None, 2, None, 1]),
            ([4, 6, 2, 7, 1, 5, 3], [7, 6, 5, 4, 2, 1, 3]),
            ([10, 3, 7, 1, 8, 2, 9], [10, None, 9, 8, None, 7, 2, 3, 1]),
            ([0, 1000, 1], [1000, 0, 1]),
            ([1000, 0, 999, 1, 998, 2], [1000, None, 999, 0, 998, None, None, 1, 2]),
            ([393, 641, 322, 747, 651], [747, 641, 651, 393, 322]),
            ([620], [620]),
            ([501, 959, 967, 256], [967, 959, 256, 501]),
            ([859, 470], [859, None, 470]),
        ],
    )
    def test_construct_maximum_binary_tree(self, nums: list[int], expected_list: list[int | None]):
        result = run_construct_maximum_binary_tree(Solution, nums)
        assert_construct_maximum_binary_tree(result, expected_list)
