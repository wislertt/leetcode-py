import pytest

from leetcode_py import logged_test

from .helpers import assert_trap_rain_water, run_trap_rain_water
from .solution import Solution


class TestTrappingRainWaterII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "height_map, expected",
        [
            ([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]], 4),
            ([[5]], 0),
            ([[3, 3, 3]], 0),
            ([[3], [3], [3]], 0),
            ([[5, 5, 5, 5], [5, 3, 3, 5], [5, 5, 5, 5]], 4),
            ([[5, 5, 5, 5, 5], [5, 1, 1, 1, 5], [5, 5, 5, 5, 5]], 12),
            ([[4, 4, 4, 4, 4], [4, 3, 2, 3, 4], [4, 4, 4, 4, 4]], 4),
            ([[1, 1, 1, 1, 1], [1, 0, 9, 0, 1], [1, 1, 1, 1, 1]], 2),
            ([[9, 9, 9, 9], [9, 2, 2, 9], [9, 2, 2, 9], [9, 9, 9, 9]], 28),
            ([[2, 2, 2], [2, 2, 2], [2, 2, 2]], 0),
            ([[1, 2, 3, 4], [4, 3, 2, 1]], 0),
            ([[5, 5, 5], [5, 1, 5], [5, 5, 5]], 4),
            ([[3, 3, 3, 3], [3, 1, 1, 3], [3, 3, 3, 3], [3, 1, 1, 3], [3, 3, 3, 3]], 8),
            ([[1, 10, 1], [10, 1, 10], [1, 10, 1]], 9),
            ([[9, 9, 9, 9, 9, 9], [9, 1, 9, 9, 1, 9], [9, 9, 9, 9, 9, 9]], 16),
        ],
    )
    def test_trap_rain_water(self, height_map: list[list[int]], expected: int):
        result = run_trap_rain_water(Solution, height_map)
        assert_trap_rain_water(result, expected)
