import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_time, run_minimum_time
from .solution import Solution


class TestMinimumTimeToVisitACellInAGrid:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 1, 3, 2], [5, 1, 2, 5], [4, 3, 8, 6]], 7),
            ([[0, 2, 4], [3, 2, 1], [1, 0, 4]], -1),
            ([[0, 5], [5, 0]], -1),
            ([[0, 1], [2, 1]], 2),
            ([[0, 1, 1], [1, 1, 1], [1, 1, 1]], 4),
            ([[0, 9, 9], [9, 9, 9], [9, 9, 0]], -1),
            ([[0, 100000], [100000, 0]], -1),
            ([[0, 2], [3, 0]], -1),
            ([[0, 1, 100000], [1, 100000, 1], [1, 1, 0]], 4),
            ([[0, 4, 3], [4, 4, 4], [4, 4, 4]], -1),
            ([[0, 3], [2, 0]], -1),
            ([[0, 1, 2], [3, 4, 5], [6, 7, 0]], 6),
            ([[0, 1, 0], [1, 1, 0], [1, 1, 7]], 8),
            ([[0, 1, 1], [1, 1, 1], [1, 1, 8]], 8),
            ([[0, 9, 3], [1, 1, 9], [5, 0, 3], [12, 2, 11]], 11),
            ([[0, 6], [4, 5]], -1),
            ([[0, 1, 2], [2, 2, 0], [0, 3, 3], [0, 2, 3]], 5),
            ([[0, 1], [0, 1]], 2),
            ([[0, 4], [3, 8]], -1),
            ([[0, 1], [2, 2], [0, 1]], 3),
            ([[0, 2, 2], [0, 1, 1], [2, 1, 1]], 4),
            ([[0, 1], [0, 2], [1, 1]], 3),
        ],
    )
    def test_minimum_time(self, grid: list[list[int]], expected: int):
        result = run_minimum_time(Solution, grid)
        assert_minimum_time(result, expected)
