import pytest

from leetcode_py import logged_test

from .helpers import assert_level_order_bottom, run_level_order_bottom
from .solution import Solution


class TestBinaryTreeLevelOrderTraversalII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 9, 20, None, None, 15, 7], [[15, 7], [9, 20], [3]]),
            ([1], [[1]]),
            ([], []),
            ([1, 2, 3, 4, 5, 6, 7], [[4, 5, 6, 7], [2, 3], [1]]),
            ([1, 2, None, 3, None, 4, None, 5], [[5], [4], [3], [2], [1]]),
            ([1, None, 2, None, 3], [[3], [2], [1]]),
            ([1, 2, None, 3, None], [[3], [2], [1]]),
            ([0], [[0]]),
            ([-1, -2, -3], [[-2, -3], [-1]]),
            ([1, 2, 3, None, None, None, 4], [[4], [2, 3], [1]]),
            ([5, 4, 8, 11, None, 13, 4], [[11, 13, 4], [4, 8], [5]]),
            ([1, 2, 2, 3, 3, 3, 3], [[3, 3, 3, 3], [2, 2], [1]]),
            ([1, None, None], [[1]]),
            ([3, 9, 20, None, None, 15, 7, 3], [[3], [15, 7], [9, 20], [3]]),
            ([1, 2, 3, 4, None, None, 5, 6], [[6], [4, 5], [2, 3], [1]]),
        ],
    )
    def test_level_order_bottom(self, root_list: list[int | None], expected: list[list[int]]):
        result = run_level_order_bottom(Solution, root_list)
        assert_level_order_bottom(result, expected)
