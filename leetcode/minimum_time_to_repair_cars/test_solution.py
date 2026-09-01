import pytest

from leetcode_py import logged_test

from .helpers import assert_repair_cars, run_repair_cars
from .solution import Solution


class TestMinimumTimeToRepairCars:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "ranks, cars, expected",
        [
            ([4, 2, 3, 1], 10, 16),
            ([5, 1, 8], 6, 16),
            ([1], 1, 1),
            ([1], 2, 4),
            ([1], 3, 9),
            ([100], 1000000, 100000000000000),
            ([1], 1000000, 1000000000000),
            ([10, 10, 10], 1, 10),
            ([1, 2, 3], 7, 12),
            ([2, 2], 5, 18),
            ([7, 1, 3, 5], 12, 28),
            ([1, 1, 1, 1], 100, 625),
            ([100, 1], 100, 8281),
            ([2, 2, 2, 2, 2], 25, 50),
            ([3], 10, 300),
            ([50, 25, 75], 40, 8100),
            ([4, 4, 4, 4], 3, 4),
            ([6, 2, 8, 4, 1], 11, 18),
        ],
    )
    def test_repair_cars(self, ranks: list[int], cars: int, expected: int):
        result = run_repair_cars(Solution, ranks, cars)
        assert_repair_cars(result, expected)
