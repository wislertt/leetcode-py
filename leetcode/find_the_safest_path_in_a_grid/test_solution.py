import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_safeness_factor, run_maximum_safeness_factor
from .solution import Solution


class TestTestFindTheSafestPathInAGrid:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 0, 0], [0, 0, 0], [0, 0, 1]], 0),
            ([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 2),
            ([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 2),
            ([[1]], 0),
            ([[0, 1], [1, 0]], 0),
            ([[1, 0], [0, 0]], 0),
            ([[0, 0], [0, 1]], 0),
            ([[0, 1, 0], [0, 0, 0], [0, 1, 0]], 1),
            ([[1, 1], [1, 1]], 0),
            ([[1, 1, 0, 1], [0, 1, 0, 0], [1, 0, 1, 0], [0, 0, 0, 1]], 0),
            ([[1, 0], [0, 1]], 0),
            ([[0, 0, 0, 0], [1, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]], 1),
            ([[0, 1, 0], [1, 0, 0], [0, 0, 1]], 0),
            ([[0, 0, 1, 0], [0, 1, 0, 1], [0, 1, 1, 1], [0, 0, 0, 1]], 0),
            ([[1, 0, 0], [0, 0, 0], [0, 1, 1]], 0),
            ([[0, 0, 0], [0, 1, 0], [0, 1, 0]], 1),
        ],
    )
    def test_maximum_safeness_factor(self, grid: list[list[int]], expected: int):
        result = run_maximum_safeness_factor(Solution, grid)
        assert_maximum_safeness_factor(result, expected)
