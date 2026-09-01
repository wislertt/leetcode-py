import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_fuel_cost, run_minimum_fuel_cost
from .solution import Solution


class TestTestMinimumFuelCost:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "roads, seats, expected",
        [
            ([[0, 1], [0, 2], [0, 3]], 5, 3),
            ([[3, 1], [3, 2], [1, 0], [0, 4], [0, 5], [4, 6]], 2, 7),
            ([], 1, 0),
            ([[0, 1]], 1, 1),
            ([[0, 1]], 5, 1),
            ([[0, 1], [0, 2], [0, 3], [0, 4]], 2, 4),
            ([[0, 1], [1, 2], [2, 3]], 2, 4),
            ([[0, 1], [1, 2], [2, 3], [3, 4]], 2, 6),
            ([[0, 1], [1, 2], [2, 3], [3, 4]], 100, 4),
            ([[0, 1], [1, 2], [2, 3], [3, 4]], 1, 10),
            ([[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], 3, 6),
            ([[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], 2, 8),
            ([[0, 1], [1, 2], [1, 3], [0, 4]], 2, 5),
            ([[4, 1], [4, 0], [4, 2], [3, 4], [5, 4], [6, 4]], 3, 7),
            ([[0, 1], [1, 2]], 3, 2),
            ([[4, 6], [0, 3], [0, 1], [1, 4], [1, 5], [0, 2]], 1, 10),
            ([[1, 2], [1, 3], [0, 4], [3, 5], [3, 6], [0, 1]], 1, 12),
            ([[1, 2], [0, 1], [2, 3], [2, 5], [5, 6], [3, 4]], 3, 8),
            ([[0, 1], [2, 3], [0, 2]], 10, 3),
            ([[0, 1], [3, 4], [2, 3], [1, 2]], 3, 5),
        ],
    )
    def test_minimum_fuel_cost(self, roads: list[list[int]], seats: int, expected: int):
        result = run_minimum_fuel_cost(Solution, roads, seats)
        assert_minimum_fuel_cost(result, expected)
