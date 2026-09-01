import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_nodes, run_remove_nodes
from .solution import Solution


class TestRemoveNodesFromLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_vals, expected_vals",
        [
            ([5, 2, 13, 3, 8], [13, 8]),
            ([1, 1, 1, 1], [1, 1, 1, 1]),
            ([5], [5]),
            ([1, 2], [2]),
            ([2, 1], [2, 1]),
            ([1, 2, 3], [3]),
            ([3, 2, 1], [3, 2, 1]),
            ([10, 5, 7], [10, 7]),
            ([1, 3, 2, 4], [4]),
            ([9, 1, 9, 1, 9], [9, 9, 9]),
            ([2, 2, 2], [2, 2, 2]),
            ([100000, 1, 100000], [100000, 100000]),
            ([4, 5, 3, 6, 2, 7], [7]),
            ([8, 9, 1, 2, 3, 10, 4, 5], [10, 5]),
            ([5, 8, 3, 1, 8, 8, 8, 3, 7], [8, 8, 8, 8, 7]),
            ([9, 10, 6, 2, 5, 2, 7, 2], [10, 7, 2]),
            ([6, 8, 4, 1, 10, 7, 2], [10, 7, 2]),
            ([2, 5, 4, 6, 6], [6, 6]),
            ([5, 3, 5, 4, 6, 9, 4, 1, 8], [9, 8]),
            ([3, 5, 10, 8, 5, 8, 6], [10, 8, 8, 6]),
        ],
    )
    def test_remove_nodes(self, head_vals: list[int], expected_vals: list[int]):
        result = run_remove_nodes(Solution, head_vals)
        assert_remove_nodes(result, expected_vals)
