import pytest

from leetcode_py import logged_test

from .helpers import assert_min_cost_tickets, run_min_cost_tickets
from .solution import Solution


class TestMinimumCostForTickets:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "days, costs, expected",
        [
            ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
            ([1, 4, 6, 7, 8, 20], [7, 2, 15], 6),
            ([1, 365], [2, 7, 15], 4),
            ([1], [5, 3, 10], 3),
            ([1, 2, 3, 4], [5, 6, 7], 6),
            ([2, 5], [1, 4, 25], 2),
            ([1, 3, 7], [1, 4, 20], 3),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 5, 12], 9),
            ([365], [1, 2, 3], 1),
            ([1, 30, 60], [2, 7, 15], 6),
            ([1, 2, 4, 5, 6, 7, 8, 9, 10], [7, 2, 14], 4),
        ],
    )
    def test_min_cost_tickets(self, days: list[int], costs: list[int], expected: int):
        result = run_min_cost_tickets(Solution, days, costs)
        assert_min_cost_tickets(result, expected)
