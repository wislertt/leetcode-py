import pytest

from leetcode_py import logged_test

from .helpers import assert_find_leaves, run_find_leaves
from .solution import Solution


class TestFindLeavesOfBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 2, 3, 4, 5], [[4, 5, 3], [2], [1]]),
            ([1], [[1]]),
            ([1, 2], [[2], [1]]),
            ([1, 2, 3], [[2, 3], [1]]),
            ([1, 2, 3, 4, 5, 6, 7], [[4, 5, 6, 7], [2, 3], [1]]),
            ([1, 2, 3, None, None, 6, 7], [[2, 6, 7], [3], [1]]),
            ([1, 2, None, 3], [[3], [2], [1]]),
            ([1, None, 2, None, 3], [[3], [2], [1]]),
            ([-1, -2, -3, -4, -5], [[-4, -5, -3], [-2], [-1]]),
            ([1, None, 2, 3], [[3], [2], [1]]),
            ([0, 0, 0, 0, 0, 0, 0, 0], [[0, 0, 0, 0], [0, 0], [0], [0]]),
            ([5, 4, 8, 11, None, 13, 4, 7, 2], [[7, 2, 13, 4], [11, 8], [4], [5]]),
            ([1, 2, 3, None, 4, 5, 6, None, None, 7], [[4, 7, 6], [2, 5], [3], [1]]),
            ([10], [[10]]),
        ],
    )
    def test_find_leaves(self, root_list: list[int | None], expected: list[list[int]]):
        result = run_find_leaves(Solution, root_list)
        assert_find_leaves(result, expected)
