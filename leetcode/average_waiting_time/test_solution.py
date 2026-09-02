import pytest

from leetcode_py import logged_test

from .helpers import assert_average_waiting_time, run_average_waiting_time
from .solution import Solution


class TestAverageWaitingTime:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "customers, expected",
        [
            ([[1, 2], [2, 5], [4, 3]], 5.0),
            ([[5, 2], [5, 4], [10, 3], [20, 1]], 3.25),
            ([[1, 1]], 1.0),
            ([[1, 10000]], 10000.0),
            ([[10000, 1]], 1.0),
            ([[1, 1], [1, 1], [1, 1]], 2.0),
            ([[1, 2], [3, 4], [5, 6]], 4.666666666666667),
            ([[1, 3], [2, 3], [3, 3]], 5.0),
            ([[4, 4], [13, 3], [15, 1], [16, 4], [19, 9]], 5.0),
            ([[9, 3], [13, 1], [20, 3]], 2.3333333333333335),
            ([[6, 4], [6, 5], [7, 10], [7, 4], [19, 2], [20, 8]], 14.0),
            ([[9, 4], [13, 4], [17, 5]], 4.333333333333333),
            ([[6, 1], [10, 8], [11, 8]], 8.0),
            ([[1, 4], [12, 5], [16, 9], [16, 10], [20, 8]], 12.6),
        ],
    )
    def test_average_waiting_time(self, customers: list[list[int]], expected: float):
        result = run_average_waiting_time(Solution, customers)
        assert_average_waiting_time(result, expected)
