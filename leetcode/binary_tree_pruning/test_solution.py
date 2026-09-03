import pytest

from leetcode_py import logged_test

from .helpers import assert_prune_tree, run_prune_tree
from .solution import Solution


class TestBinaryTreePruning:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([1, None, 0, 0, 1], [1, None, 0, None, 1]),
            ([1, 0, 1, 0, 0, 0, 1], [1, None, 1, None, 1]),
            ([1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, None, 1]),
            ([0], []),
            ([1], [1]),
            ([0, 0, 0], []),
            ([1, 0, 0], [1]),
            ([0, 1, 1], [0, 1, 1]),
            ([1, 1, 0], [1, 1]),
            ([1, 1, 1], [1, 1, 1]),
            ([0, 0, None, 0, 1], [0, 0, None, None, 1]),
            ([1, 0, 1, None, 1, 0, 1], [1, 0, 1, None, 1, None, 1]),
            ([1, 0, 0, 0, 0, 0, 0], [1]),
            ([0, 0, None, 1], [0, 0, None, 1]),
            ([1, 1], [1, 1]),
            ([0, 1, None, 1, None, 1], [0, 1, None, 1, None, 1]),
            ([0, 1, None, 1, None, 0], [0, 1, None, 1]),
            ([0, 1, None, 1, None, 0, None, 0], [0, 1, None, 1]),
            ([1, 0], [1]),
            ([0, None, 0, None, 0, 1], [0, None, 0, None, 0, 1]),
        ],
    )
    def test_prune_tree(self, root_list: list[int | None], expected_list: list[int | None]):
        result = run_prune_tree(Solution, root_list)
        assert_prune_tree(result, expected_list)
