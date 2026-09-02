import pytest

from leetcode_py import logged_test

from .helpers import assert_min_operations, run_min_operations
from .solution import Solution


class TestMinimumOperationsToMakeAUniValueGrid:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, x, expected",
        [
            ([[2, 4], [6, 8]], 2, 4),
            ([[1, 5], [2, 3]], 1, 5),
            ([[1, 2], [3, 4]], 2, -1),
            ([[5]], 3, 0),
            ([[7, 7, 7], [7, 7, 7]], 4, 0),
            ([[1, 10000], [2, 9999]], 1, 19996),
            ([[3, 9], [15, 21]], 6, 4),
            ([[2]], 10000, 0),
            ([[9, 1], [5, 5]], 4, 2),
            ([[1, 4], [7, 10]], 3, 4),
            ([[9999, 2]], 3, -1),
            ([[5, 5], [5, 2]], 3, 1),
            ([[10, 20, 30], [40, 50, 60]], 10, 9),
            ([[13, 13], [13, 26]], 13, 1),
            ([[13], [15]], 2, 1),
            ([[26, 49, 51], [52, 46, 47]], 6, -1),
            ([[22, 55, 55]], 11, 3),
            ([[5, 5], [11, 5]], 1, 6),
        ],
    )
    def test_min_operations(self, grid: list[list[int]], x: int, expected: int):
        result = run_min_operations(Solution, grid, x)
        assert_min_operations(result, expected)
