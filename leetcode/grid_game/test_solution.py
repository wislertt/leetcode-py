import pytest

from leetcode_py import logged_test

from .helpers import assert_grid_game, run_grid_game
from .solution import Solution


class TestGridGame:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[2, 5, 4], [1, 5, 1]], 4),
            ([[3, 3, 1], [8, 5, 2]], 4),
            ([[1, 3, 1, 15], [1, 3, 3, 1]], 7),
            ([[1], [2]], 0),
            ([[1, 2], [3, 4]], 2),
            ([[100000], [99999]], 0),
            ([[100000, 100000], [100000, 100000]], 100000),
            ([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], 2),
            ([[7289, 5621], [5263, 8369]], 5263),
            ([[1091, 8404], [7511, 8764]], 7511),
            ([[3908], [9844]], 0),
            ([[8634, 3971, 106, 1321], [4384, 4006, 2333, 3144]], 4384),
            ([[4520, 3834], [8540, 8220]], 3834),
            ([[9025, 9665, 1774, 4962], [3594, 8034, 8302, 8600]], 6736),
            ([[4787, 1039, 2270], [1896, 2484, 840]], 2270),
            ([[7342, 8966], [1860, 8057]], 1860),
            ([[6793], [3338]], 0),
            ([[5945, 6889], [5800, 4524]], 5800),
        ],
    )
    def test_grid_game(self, grid: list[list[int]], expected: int):
        result = run_grid_game(Solution, grid)
        assert_grid_game(result, expected)
