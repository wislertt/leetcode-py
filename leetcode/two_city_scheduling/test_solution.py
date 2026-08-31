import pytest

from leetcode_py import logged_test

from .helpers import assert_two_city_sched_cost, run_two_city_sched_cost
from .solution import Solution


class TestTwoCityScheduling:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "costs, expected",
        [
            ([[10, 20], [30, 200], [400, 50], [30, 20]], 110),
            ([[259, 770], [448, 54], [926, 667], [184, 139], [840, 118], [577, 469]], 1859),
            (
                [
                    [515, 563],
                    [451, 713],
                    [537, 709],
                    [343, 819],
                    [855, 779],
                    [457, 60],
                    [650, 359],
                    [631, 42],
                ],
                3086,
            ),
            ([[10, 20], [30, 200]], 50),
            ([[5, 5], [6, 6], [7, 7], [8, 8]], 26),
            ([[1, 100], [100, 1], [1, 100], [100, 1]], 4),
            ([[500, 100], [100, 500], [500, 100], [100, 500]], 400),
            ([[10, 10], [10, 10]], 20),
            ([[1, 2], [3, 4], [5, 6], [7, 8]], 18),
            ([[999, 1], [1, 999], [999, 1], [1, 999], [999, 1], [1, 999]], 6),
            ([[50, 10], [10, 50], [60, 20], [20, 60], [70, 30], [30, 70]], 120),
            ([[1, 1000], [1000, 1]], 2),
        ],
    )
    def test_two_city_sched_cost(self, costs: list[list[int]], expected: int):
        result = run_two_city_sched_cost(Solution, costs)
        assert_two_city_sched_cost(result, expected)
