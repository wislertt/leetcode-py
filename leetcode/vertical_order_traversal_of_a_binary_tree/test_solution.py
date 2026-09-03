import pytest

from leetcode_py import logged_test

from .helpers import assert_vertical_traversal, run_vertical_traversal
from .solution import Solution


class TestVerticalOrderTraversalOfABinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([3, 9, 20, None, None, 15, 7], [[9], [3, 15], [20], [7]]),
            ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]]),
            ([1, 2, 3, 4, 6, 5, 7], [[4], [2], [1, 5, 6], [3], [7]]),
            ([1], [[1]]),
            ([1, 2], [[2], [1]]),
            ([1, None, 2], [[1], [2]]),
            ([1, 2, None, 3], [[3], [2], [1]]),
            ([1, None, 2, None, 3], [[1], [2], [3]]),
            ([0, 0, 0], [[0], [0], [0]]),
            ([1, 1, 1, 1, 1, 1, 1], [[1], [1], [1, 1, 1], [1], [1]]),
            ([3, 1, 4, None, 2, 1, 5], [[1], [3, 1, 2], [4], [5]]),
            ([7, 4, 9, 2, 5, 8, 10, 1], [[1], [2], [4], [7, 5, 8], [9], [10]]),
            ([3, 7, 0, 6, 4, 2, 2, 2, 7, 2], [[2], [6], [7, 2, 7], [3, 2, 4], [0], [2]]),
            ([8, 7, 1, 6, 4, None, 4, 2, 4], [[2], [6], [7, 4], [8, 4], [1], [4]]),
            ([2], [[2]]),
            ([3, 9, None, 7, 9, 5, 9], [[5], [7], [9, 9], [3, 9]]),
            ([6, 7, None, 6], [[6], [7], [6]]),
            ([9, 1, 3, 3, 3, 7, 4], [[3], [1], [9, 3, 7], [3], [4]]),
            ([4, 9, None, 1, 5, 7, 7, 2], [[7], [1], [9, 2, 7], [4, 5]]),
        ],
    )
    def test_vertical_traversal(self, root_list: list[int | None], expected_list: list[list[int]]):
        result = run_vertical_traversal(Solution, root_list)
        assert_vertical_traversal(result, expected_list)
