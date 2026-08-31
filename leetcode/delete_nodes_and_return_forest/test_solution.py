import pytest

from leetcode_py import logged_test

from .helpers import assert_del_nodes, run_del_nodes
from .solution import Solution


class TestDeleteNodesAndReturnForest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, to_delete, expected_forest",
        [
            ([1, 2, 3, 4, 5, 6, 7], [3, 5], [[6], [7], [1, 2, None, 4]]),
            ([1, 2, 4, None, 3], [3], [[1, 2, 4]]),
            ([1, 2, 3, None, None, None, 4], [2], [[1, None, 3, None, 4]]),
            ([1], [], [[1]]),
            ([1], [1], []),
            ([1, 2], [1], [[2]]),
            ([1, 2], [2], [[1]]),
            ([1, 2, 3], [1, 2, 3], []),
            ([1, 2, 3], [], [[1, 2, 3]]),
            ([1, 2, 3, 4, 5], [2, 3], [[1], [4], [5]]),
            ([1, None, 2, None, 3], [2], [[1], [3]]),
            ([1, 2, None, 3], [], [[1, 2, None, 3]]),
            (
                [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1],
                [4, 1],
                [[11, 7, 2], [5, None, 8, 13]],
            ),
        ],
    )
    def test_del_nodes(
        self,
        root_list: list[int | None],
        to_delete: list[int],
        expected_forest: list[list[int | None]],
    ):
        result = run_del_nodes(Solution, root_list, to_delete)
        assert_del_nodes(result, expected_forest)
