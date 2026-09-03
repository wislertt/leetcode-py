import pytest

from leetcode_py import logged_test

from .helpers import assert_reachable_nodes, run_reachable_nodes
from .solution import Solution


class TestReachableNodesInSubdividedGraph:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "edges, max_moves, n, expected",
        [
            ([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3, 13),
            ([[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4, 23),
            ([[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], 17, 5, 1),
            ([], 0, 1, 1),
            ([], 1000000000, 5, 1),
            ([[0, 1, 0]], 0, 2, 1),
            ([[0, 1, 0]], 1, 2, 2),
            ([[0, 1, 5]], 3, 2, 4),
            ([[0, 1, 5]], 10, 2, 7),
            ([[0, 1, 2], [1, 2, 2]], 4, 3, 5),
            ([[0, 1, 1], [1, 2, 1], [2, 3, 1]], 5, 4, 6),
            ([[0, 1, 3], [0, 2, 3]], 4, 3, 9),
            ([[0, 1, 10000]], 1000000000, 2, 10002),
            ([[0, 1, 2], [0, 2, 2], [1, 2, 2]], 5, 3, 9),
            ([[1, 2, 3]], 1, 3, 1),
            ([[0, 1, 1], [2, 3, 1]], 10, 6, 3),
            ([[0, 1, 4], [0, 2, 4]], 0, 3, 1),
            ([[0, 1, 3], [1, 2, 3], [2, 3, 3]], 9, 4, 10),
            ([[0, 1, 2], [1, 2, 2], [2, 3, 2]], 5, 4, 6),
            ([[0, 1, 4], [1, 2, 4]], 5, 3, 6),
            ([[0, 1, 3], [0, 2, 3], [1, 2, 3]], 4, 3, 9),
            ([[0, 2, 7], [0, 1, 3], [1, 2, 2], [2, 3, 1]], 6, 4, 13),
        ],
    )
    def test_reachable_nodes(self, edges: list[list[int]], max_moves: int, n: int, expected: int):
        result = run_reachable_nodes(Solution, edges, max_moves, n)
        assert_reachable_nodes(result, expected)
