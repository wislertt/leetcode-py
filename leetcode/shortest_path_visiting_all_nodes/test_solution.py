import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_path_length, run_shortest_path_length
from .solution import Solution


class TestShortestPathVisitingAllNodes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "graph, expected",
        [
            ([[1, 2, 3], [0], [0], [0]], 4),
            ([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]], 4),
            ([[]], 0),
            ([[1], [0]], 1),
            ([[1, 2], [0], [0]], 2),
            ([[1], [0, 2], [1]], 2),
            ([[1, 2], [0], [0, 3], [2]], 3),
            ([[1, 3], [0, 2], [1, 3], [0, 2]], 3),
            ([[1], [0, 2], [1, 3], [2, 4], [3, 5], [4]], 5),
            ([[1, 2], [0, 2], [0, 1]], 2),
            ([[1, 4], [0, 2], [1, 3], [2, 4], [3, 0]], 4),
            ([[1, 2], [0, 3], [0, 4], [1, 5], [2, 5], [3, 4]], 5),
            ([[1, 2], [0], [0, 3, 4], [2], [2]], 5),
            ([[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]], 3),
            ([[1, 2], [0, 3], [0, 3], [1, 2]], 3),
            ([[1, 3], [0, 2, 3], [1, 3], [0, 1, 2]], 3),
            ([[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]], 3),
        ],
    )
    def test_shortest_path_length(self, graph: list[list[int]], expected: int):
        result = run_shortest_path_length(Solution, graph)
        assert_shortest_path_length(result, expected)
