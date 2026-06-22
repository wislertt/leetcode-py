import pytest

from leetcode_py import logged_test

from .helpers import assert_min_cost_climbing_stairs, run_min_cost_climbing_stairs
from .solution import Solution


class TestMinCostClimbingStairs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "cost, expected",
        [
            ([10, 15, 20], 15),
            ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
            ([1, 2], 1),
            ([0, 0], 0),
            ([999, 999], 999),
            ([1, 2, 3], 2),
            ([10, 1, 1, 10], 2),
            ([0, 100, 0, 100, 0], 0),
            ([5, 5, 5, 5, 5], 10),
            ([3, 2, 1, 4], 3),
            ([10, 5, 10, 5, 10], 10),
            ([2, 3, 4, 5, 6], 8),
            ([100, 100, 100, 100], 200),
        ],
    )
    def test_min_cost_climbing_stairs(self, cost: list[int], expected: int):
        result = run_min_cost_climbing_stairs(Solution, cost)
        assert_min_cost_climbing_stairs(result, expected)
