import pytest

from leetcode_py import logged_test

from .helpers import assert_min_refuel_stops, run_min_refuel_stops
from .solution import Solution


class TestMinimumNumberOfRefuelingStops:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "target, start_fuel, stations, expected",
        [
            (1, 1, [], 0),
            (100, 1, [[10, 100]], -1),
            (100, 10, [[10, 60], [20, 30], [30, 30], [60, 40]], 2),
            (10, 1, [[5, 100]], -1),
            (10, 10, [], 0),
            (10, 9, [[5, 1]], 1),
            (1000, 1, [[1, 1], [2, 1], [3, 1]], -1),
            (100, 25, [[25, 25], [50, 50], [75, 25]], 2),
            (100, 50, [[25, 50], [50, 25]], 1),
            (1000000000, 1000000000, [], 0),
            (1000000000, 1, [[999999999, 10]], -1),
            (30, 10, [[10, 5], [14, 6], [20, 8], [25, 3]], 4),
            (100, 10, [[10, 20], [30, 40], [60, 40], [90, 100]], 3),
            (50, 20, [[10, 10], [20, 10], [30, 10], [40, 10]], 3),
            (500, 100, [[100, 100], [200, 100], [300, 100], [400, 100]], 4),
            (20, 5, [[4, 6], [10, 10], [15, 5]], 2),
            (48, 4, [[8, 28], [36, 15]], -1),
            (28, 13, [[17, 12], [18, 25]], -1),
            (50, 26, [[30, 15], [33, 28]], -1),
            (38, 20, [[3, 22], [5, 10], [22, 24], [33, 12], [37, 5]], 1),
            (19, 22, [], 0),
            (49, 11, [[9, 22], [20, 26], [32, 8], [36, 26]], 2),
            (47, 28, [], -1),
            (39, 22, [[29, 20], [38, 10]], -1),
        ],
    )
    def test_min_refuel_stops(
        self, target: int, start_fuel: int, stations: list[list[int]], expected: int
    ):
        result = run_min_refuel_stops(Solution, target, start_fuel, stations)
        assert_min_refuel_stops(result, expected)
