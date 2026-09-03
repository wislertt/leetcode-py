import pytest

from leetcode_py import logged_test

from .helpers import assert_max_vacation_days, run_max_vacation_days
from .solution import Solution


class TestTestMaximumVacationDays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "flights, days, expected",
        [
            ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], [[1, 3, 1], [6, 0, 3], [3, 3, 3]], 12),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 1, 1], [7, 7, 7], [7, 7, 7]], 3),
            ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], [[7, 0, 0], [0, 7, 0], [0, 0, 7]], 21),
            ([[0]], [[7]], 7),
            ([[0]], [[1, 2, 3]], 6),
            ([[0, 1], [1, 0]], [[3], [5]], 5),
            ([[0, 0], [0, 0]], [[0, 0], [0, 0]], 0),
            ([[0, 1, 0], [0, 0, 1], [0, 0, 0]], [[1, 1, 1], [2, 2, 2], [3, 3, 3]], 8),
            ([[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[7, 7], [0, 0], [0, 0]], 14),
            ([[0, 1, 1], [1, 0, 0], [1, 0, 0]], [[0, 0], [7, 7], [0, 0]], 14),
            ([[0, 1], [0, 0]], [[7, 7], [7, 7]], 14),
            ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], [[6, 6], [6, 6], [6, 6]], 12),
            ([[0, 1], [1, 0]], [[7, 0], [0, 7]], 14),
            ([[0, 0, 1], [0, 0, 1], [0, 0, 0]], [[2, 2, 2], [3, 3, 3], [4, 4, 4]], 12),
            ([[0, 1], [1, 0]], [[6, 3], [1, 7]], 13),
            ([[0, 1, 1], [0, 0, 1], [0, 0, 0]], [[4, 2, 2], [7, 2, 3], [5, 3, 6]], 16),
            ([[0, 0], [0, 0]], [[7, 7], [0, 0]], 14),
            ([[0, 1, 0], [1, 0, 0], [0, 1, 0]], [[2, 7, 5], [3, 2, 1], [7, 6, 3]], 15),
            ([[0, 1], [1, 0]], [[2, 0], [1, 5]], 7),
            ([[0, 0], [1, 0]], [[4, 3], [2, 7]], 7),
        ],
    )
    def test_max_vacation_days(
        self, flights: list[list[int]], days: list[list[int]], expected: int
    ):
        result = run_max_vacation_days(Solution, flights, days)
        assert_max_vacation_days(result, expected)
