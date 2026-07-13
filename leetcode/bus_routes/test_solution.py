import pytest

from leetcode_py import logged_test

from .helpers import assert_num_buses_to_destination, run_num_buses_to_destination
from .solution import Solution


class TestBusRoutes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "routes, source, target, expected",
        [
            ([[1, 2, 7], [3, 6, 7]], 1, 6, 2),
            ([[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12, -1),
            ([[1, 2, 3]], 1, 3, 1),
            ([[1, 2, 3]], 1, 1, 0),
            ([[1], [2], [3]], 1, 3, -1),
            ([[1, 2, 3], [4, 5, 6]], 1, 6, -1),
            ([[1, 2, 3], [3, 4, 5]], 1, 5, 2),
            ([[1, 2, 3], [3, 4, 5]], 2, 4, 2),
            ([[1, 5], [5, 10]], 1, 10, 2),
            ([[1, 2, 3, 4]], 1, 4, 1),
            ([[1], [1, 2], [2]], 1, 2, 1),
            ([[1, 2], [2, 3], [3, 4]], 1, 4, 3),
            ([[1, 2], [3, 4], [5, 6]], 1, 6, -1),
            ([[1, 2, 3]], 5, 1, -1),
            ([[1, 7], [3, 6, 7], [1, 2, 3]], 1, 6, 2),
        ],
    )
    def test_num_buses_to_destination(
        self, routes: list[list[int]], source: int, target: int, expected: int
    ):
        result = run_num_buses_to_destination(Solution, routes, source, target)
        assert_num_buses_to_destination(result, expected)
