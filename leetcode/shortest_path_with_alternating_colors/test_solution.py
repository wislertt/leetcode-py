import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_alternating_paths, run_shortest_alternating_paths
from .solution import Solution


class TestShortestPathWithAlternatingColors:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, red_edges, blue_edges, expected",
        [
            (3, [[0, 1], [1, 2]], [], [0, 1, -1]),
            (3, [[0, 1]], [[2, 1]], [0, 1, -1]),
            (1, [], [], [0]),
            (2, [[0, 1]], [], [0, 1]),
            (2, [], [[0, 1]], [0, 1]),
            (3, [[0, 1], [0, 2]], [[1, 2], [2, 1]], [0, 1, 1]),
            (4, [[0, 1], [1, 2], [2, 3]], [[3, 0]], [0, 1, -1, -1]),
            (3, [[1, 2], [0, 1]], [[1, 0]], [0, 1, -1]),
            (5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[4, 0], [0, 4]], [0, 1, -1, -1, 1]),
            (3, [[0, 1]], [[0, 1]], [0, 1, -1]),
            (2, [[0, 0]], [], [0, -1]),
            (4, [[2, 3]], [[0, 1], [1, 2]], [0, 1, -1, -1]),
            (3, [], [], [0, -1, -1]),
            (4, [[0, 1], [0, 2], [0, 3]], [[1, 2], [2, 3]], [0, 1, 1, 1]),
        ],
    )
    def test_shortest_alternating_paths(
        self, n: int, red_edges: list[list[int]], blue_edges: list[list[int]], expected: list[int]
    ):
        result = run_shortest_alternating_paths(Solution, n, red_edges, blue_edges)
        assert_shortest_alternating_paths(result, expected)
