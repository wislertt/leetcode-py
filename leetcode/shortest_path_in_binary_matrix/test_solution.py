import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_path_binary_matrix, run_shortest_path_binary_matrix
from .solution import Solution


class TestTestShortestPathInBinaryMatrix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 1], [1, 0]], 2),
            ([[0, 0, 0], [1, 1, 0], [1, 1, 0]], 4),
            ([[1, 0, 0], [1, 1, 0], [1, 1, 0]], -1),
            ([[0]], 1),
            ([[1]], -1),
            ([[0, 0], [0, 0]], 2),
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 4),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 3),
            ([[0, 1, 1], [1, 1, 1], [1, 1, 0]], -1),
            ([[0, 0], [1, 0]], 2),
            ([[0, 1], [0, 0]], 2),
            ([[0, 0], [0, 1]], -1),
            ([[0, 1, 1], [0, 1, 1], [0, 0, 0]], 4),
        ],
    )
    def test_shortest_path_binary_matrix(self, grid: list[list[int]], expected: int):
        result = run_shortest_path_binary_matrix(Solution, grid)
        assert_shortest_path_binary_matrix(result, expected)
