import pytest

from leetcode_py import logged_test

from .helpers import assert_validate_binary_tree_nodes, run_validate_binary_tree_nodes
from .solution import Solution


class TestValidateBinaryTreeNodes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, left_child, right_child, expected",
        [
            (4, [1, -1, 3, -1], [2, -1, -1, -1], True),
            (4, [1, -1, 3, -1], [2, 3, -1, -1], False),
            (2, [1, 0], [-1, -1], False),
            (1, [-1], [-1], True),
            (2, [-1, 1], [-1, -1], False),
            (3, [1, -1, -1], [-1, 2, -1], True),
            (3, [1, -1, -1], [-1, -1, 2], False),
            (4, [1, 2, 3, -1], [-1, -1, -1, -1], True),
            (3, [1, -1, 1], [-1, -1, -1], False),
            (3, [-1, 2, -1], [2, -1, -1], False),
            (5, [1, -1, 3, -1, -1], [-1, 2, -1, 4, -1], True),
            (6, [1, 3, -1, -1, -1, -1], [2, 4, -1, 5, -1, -1], True),
            (4, [1, -1, -1, -1], [-1, -1, 1, -1], False),
            (3, [1, -1, 0], [-1, 2, -1], False),
            (4, [-1, -1, 3, -1], [1, -1, 0, -1], True),
            (6, [-1, -1, 5, 2, -1, 4], [1, -1, 0, -1, -1, -1], True),
            (6, [-1, 2, -1, -1, -1, 0], [-1, 5, -1, 4, -1, 3], True),
            (3, [-1, 2, -1], [-1, 0, -1], True),
            (6, [-1, -1, 3, -1, 0, 2], [-1, -1, 4, -1, -1, 1], True),
            (5, [3, -1, -1, 2, 1], [-1, -1, -1, -1, 0], True),
        ],
    )
    def test_validate_binary_tree_nodes(
        self, n: int, left_child: list[int], right_child: list[int], expected: bool
    ):
        result = run_validate_binary_tree_nodes(Solution, n, left_child, right_child)
        assert_validate_binary_tree_nodes(result, expected)
