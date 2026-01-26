import pytest

from leetcode_py import logged_test

from .helpers import assert_postorder_traversal, run_postorder_traversal
from .solution import Solution


class TestBinaryTreePostorderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, None, 2, 3], [3, 2, 1]),
            ([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9], [4, 6, 7, 5, 2, 9, 8, 3, 1]),
            ([], []),
            ([1], [1]),
            ([1, 2], [2, 1]),
            ([1, None, 2], [2, 1]),
            ([1, 2, None], [2, 1]),
            ([1, 2, 3], [2, 3, 1]),
            ([3, 1, 2], [1, 2, 3]),
            ([1, 2, 3, None, 4], [4, 2, 3, 1]),
            ([1, None, 2, None, 3], [3, 2, 1]),
            ([1, 2, None, 3], [3, 2, 1]),
            ([1, None, None, 2, 3], [1]),
            ([10, 5, 15, None, None, 6, 20], [5, 6, 20, 15, 10]),
            ([1, 2, 3, 4, 5], [4, 5, 2, 3, 1]),
        ],
    )
    def test_postorder_traversal(self, root_list: list[int | None], expected: list[int]):
        result = run_postorder_traversal(Solution, root_list)
        assert_postorder_traversal(result, expected)
