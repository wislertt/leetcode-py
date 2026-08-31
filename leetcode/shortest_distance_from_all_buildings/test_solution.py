import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_distance, run_shortest_distance
from .solution import Solution


class TestShortestDistanceFromAllBuildings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], 7),
            ([[1, 0]], 1),
            ([[1]], -1),
            ([[1, 0, 0]], 1),
            ([[1, 2, 0]], -1),
            ([[0, 1], [1, 0]], 2),
            ([[1, 0], [2, 0], [1, 0]], 4),
            ([[1, 0, 0, 0, 1]], 4),
            ([[1, 2], [2, 1]], -1),
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 1),
            ([[1, 0, 2], [0, 0, 0], [2, 0, 1]], 4),
            ([[1, 1], [0, 0]], 3),
            ([[2, 0, 1]], 1),
            ([[1, 0, 0], [0, 2, 0], [0, 0, 1]], 4),
            ([[1, 0, 0, 0]], 1),
        ],
    )
    def test_shortest_distance(self, grid: list[list[int]], expected: int):
        result = run_shortest_distance(Solution, grid)
        assert_shortest_distance(result, expected)
