import pytest

from leetcode_py import logged_test

from .helpers import assert_find_smallest_set_of_vertices, run_find_smallest_set_of_vertices
from .solution import Solution


class TestMinimumNumberOfVerticesToReachAllNodes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, expected",
        [
            (6, [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]], [0, 3]),
            (5, [[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]], [0, 2, 3]),
            (2, [[0, 1]], [0]),
            (2, [[1, 0]], [1]),
            (3, [[0, 1], [1, 2]], [0]),
            (3, [[0, 1], [0, 2]], [0]),
            (4, [[0, 1], [2, 1], [2, 3]], [0, 2]),
            (5, [[1, 0], [2, 0], [3, 0], [4, 1]], [2, 3, 4]),
            (4, [[1, 2], [2, 3], [0, 3], [0, 1]], [0]),
            (3, [[0, 1], [2, 1]], [0, 2]),
            (5, [[1, 0], [1, 2], [1, 3], [1, 4]], [1]),
            (4, [[0, 1], [1, 2], [2, 3], [0, 3]], [0]),
            (8, [[0, 1]], [0, 2, 3, 4, 5, 6, 7]),
            (4, [[2, 0], [1, 0], [0, 3]], [1, 2]),
            (5, [[3, 0], [2, 1], [4, 3], [4, 0], [4, 1]], [2, 4]),
            (7, [[1, 6]], [0, 1, 2, 3, 4, 5]),
            (8, [[1, 0], [7, 3], [0, 3], [5, 7]], [1, 2, 4, 5, 6]),
        ],
    )
    def test_find_smallest_set_of_vertices(
        self, n: int, edges: list[list[int]], expected: list[int]
    ):
        result = run_find_smallest_set_of_vertices(Solution, n, edges)
        assert_find_smallest_set_of_vertices(result, expected)
