import pytest

from leetcode_py import logged_test

from .helpers import assert_ship_within_days, run_ship_within_days
from .solution import Solution


class TestCapacityToShipPackagesWithinDDays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "weights, days, expected",
        [
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15),
            ([3, 2, 2, 4, 1, 4], 3, 6),
            ([1, 2, 3, 1, 1], 4, 3),
            ([1], 1, 1),
            ([5, 5, 5], 1, 15),
            ([5, 5, 5], 3, 5),
            ([5, 5, 5], 2, 10),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, 55),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10),
            ([100], 1, 100),
            ([7, 8, 9], 3, 9),
            ([7, 8, 9], 1, 24),
            ([7, 8, 9], 2, 15),
            ([1, 1, 1, 1, 1], 5, 1),
            ([1, 1, 1, 1, 1], 1, 5),
            ([10, 9, 8, 7, 6], 3, 17),
            ([1, 2, 3, 4, 5, 6], 2, 11),
            ([10, 50, 100, 50, 10], 1, 220),
        ],
    )
    def test_ship_within_days(self, weights: list[int], days: int, expected: int):
        result = run_ship_within_days(Solution, weights, days)
        assert_ship_within_days(result, expected)
