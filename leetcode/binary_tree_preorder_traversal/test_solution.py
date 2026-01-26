import pytest

from leetcode_py import logged_test

from .helpers import assert_preorder_traversal, run_preorder_traversal
from .solution import Solution


class TestBinaryTreePreorderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, None, 2, 3], [1, 2, 3]),
            ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [1, 2, 4, 5, 6, 7, 3, 8, 9]),
            ([], []),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([1, None, 2], [1, 2]),
            ([1, 2, None], [1, 2]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 1, 2], [3, 1, 2]),
            (
                [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1],
                [5, 4, 11, 7, 5, 1, 2, 8, 13, 4],
            ),
            ([1, None, 2, None, 3], [1, 2, 3]),
            ([1, 2, None, 3], [1, 2, 3]),
            ([1, None, None, 2, 3], [1]),
            ([10, 5, 15, None, None, 6, 20], [10, 5, 15, 6, 20]),
            ([1, 2, 3, None, 4, 5, None, None, None, 6], [1, 2, 4, 3, 5, 6]),
        ],
    )
    def test_preorder_traversal(self, root_list: list[int | None], expected: list[int]):
        result = run_preorder_traversal(Solution, root_list)
        assert_preorder_traversal(result, expected)
