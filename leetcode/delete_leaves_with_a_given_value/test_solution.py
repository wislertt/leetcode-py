import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_leaf_nodes, run_remove_leaf_nodes
from .solution import Solution


class TestDeleteLeavesWithAGivenValue:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, target, expected_list",
        [
            ([1, 2, 3, 2, None, 2, 4], 2, [1, None, 3, None, 4]),
            ([1, 3, 3, 3, 2], 3, [1, 3, None, None, 2]),
            ([1, 2, None, 2, None, 2], 2, [1]),
            ([1], 1, []),
            ([1], 2, [1]),
            ([2, 2, 2], 2, []),
            ([1, 2, 3], 2, [1, None, 3]),
            ([1, 2, 3], 1, [1, 2, 3]),
            ([1, 2, 2], 2, [1]),
            ([2], 2, []),
            ([1, 2, None, 3], 3, [1, 2]),
            ([1, 1, 1], 1, []),
            ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4]),
            ([5, 3, 8, 2, 4, 7, 9], 9, [5, 3, 8, 2, 4, 7]),
            ([1, 2, 2], 1, [1, 2, 2]),
            ([1, 2, 3, 2, None, None, 2], 2, [1, None, 3]),
        ],
    )
    def test_remove_leaf_nodes(
        self, root_list: list[int | None], target: int, expected_list: list[int | None]
    ):
        result = run_remove_leaf_nodes(Solution, root_list, target)
        assert_remove_leaf_nodes(result, expected_list)
