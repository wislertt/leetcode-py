import pytest

from leetcode_py import logged_test

from .helpers import assert_minmax_gas_dist, run_minmax_gas_dist
from .solution import Solution


class TestMinimizeMaxDistanceToGasStation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "stations, k, expected",
        [
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9, 0.5),
            ([23, 24, 36, 39, 46, 56, 57, 65, 84, 98], 1, 14.0),
            ([1, 2], 1, 0.5),
            ([10, 19, 25, 27, 100], 5, 12.16667),
            ([3, 6, 12, 19, 33, 44, 67, 72, 89, 95], 2, 14.0),
            ([1, 5], 1, 2.0),
            ([1, 100], 3, 24.75),
            ([2, 4, 8, 16], 7, 1.6),
            ([5, 6, 7, 8, 20], 4, 2.4),
            ([0, 100000000], 999999, 100.0),
            ([1, 3, 7, 15], 6, 2.0),
            ([12, 19], 2, 2.33333),
        ],
    )
    def test_minmax_gas_dist(self, stations: list[int], k: int, expected: float):
        result = run_minmax_gas_dist(Solution, stations, k)
        assert_minmax_gas_dist(result, expected)
