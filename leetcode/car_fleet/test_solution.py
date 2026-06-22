import pytest

from leetcode_py import logged_test

from .helpers import assert_car_fleet, run_car_fleet
from .solution import Solution


class TestCarFleet:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "target, position, speed, expected",
        [
            (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
            (10, [3], [3], 1),
            (100, [0, 2, 4], [4, 2, 1], 1),
            (10, [0], [1], 1),
            (20, [10, 15], [5, 1], 1),
            (100, [0, 1, 2], [1, 1, 1], 3),
            (10, [0, 2, 4, 6, 8], [1, 1, 1, 1, 1], 5),
            (10, [8, 6, 4, 2, 0], [2, 4, 6, 8, 10], 1),
            (15, [1, 5, 10], [4, 2, 1], 1),
            (20, [6, 10, 15], [2, 3, 1], 2),
            (5, [1, 3], [1, 2], 2),
            (20, [5, 10], [5, 5], 2),
            (50, [10, 20, 30, 40], [1, 1, 1, 1], 4),
        ],
    )
    def test_car_fleet(self, target: int, position: list[int], speed: list[int], expected: int):
        result = run_car_fleet(Solution, target, position, speed)
        assert_car_fleet(result, expected)
