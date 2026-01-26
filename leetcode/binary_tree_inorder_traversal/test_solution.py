import pytest

from leetcode_py import logged_test

from .helpers import assert_inorder_traversal, run_inorder_traversal
from .solution import Solution


class TestBinaryTreeInorderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, None, 2, 3], [1, 3, 2]),
            ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 2, 6, 5, 7, 1, 3, 9, 8]),
            ([], []),
            ([1], [1]),
            ([1, 2], [2, 1]),
            ([1, None, 2], [1, 2]),
            ([3, 1, 2], [1, 3, 2]),
            ([5, 3, 6, 2, 4, None, 7], [2, 3, 4, 5, 6, 7]),
            ([1, None, 2, None, 3], [1, 2, 3]),
            ([2, 1, 3], [1, 2, 3]),
            ([10, 5, 15, None, 8, 12, 20], [5, 8, 10, 12, 15, 20]),
            ([1, 2, None, 3], [3, 2, 1]),
            ([4, 2, 6, 1, 3, 5, 7], [1, 2, 3, 4, 5, 6, 7]),
            ([0], [0]),
            ([-1, -2, -3], [-2, -1, -3]),
        ],
    )
    def test_inorder_traversal(self, root_list: list[int | None], expected: list[int]):
        result = run_inorder_traversal(Solution, root_list)
        assert_inorder_traversal(result, expected)
