import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_island, run_largest_island
from .solution import Solution


class TestMakingALargeIsland:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 0], [0, 1]], 3),
            ([[1, 1], [1, 0]], 4),
            ([[1, 1], [1, 1]], 4),
            ([[0]], 1),
            ([[1]], 1),
            ([[0, 0], [0, 0]], 1),
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 9),
            ([[0, 1], [1, 0]], 3),
            ([[1, 0, 1], [0, 0, 0], [0, 1, 1]], 4),
            ([[1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 0], [1, 0, 0, 0]], 6),
            ([[1, 0], [0, 0]], 2),
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
        ],
    )
    def test_largest_island(self, grid: list[list[int]], expected: int):
        result = run_largest_island(Solution, grid)
        assert_largest_island(result, expected)
