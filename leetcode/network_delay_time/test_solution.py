import pytest

from leetcode_py import logged_test

from .helpers import assert_network_delay_time, run_network_delay_time
from .solution import Solution


class TestNetworkDelayTime:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "times, n, k, expected",
        [
            ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),
            ([[1, 2, 1]], 2, 1, 1),
            ([[1, 2, 1]], 2, 2, -1),
            ([], 1, 1, 0),
            ([[1, 2, 1], [2, 3, 1], [3, 4, 1]], 4, 1, 3),
            ([[1, 2, 1]], 3, 1, -1),
            ([[1, 2, 5], [2, 3, 2], [1, 3, 10]], 3, 1, 7),
            ([[1, 2, 1], [2, 3, 1], [3, 1, 1]], 3, 1, 2),
            ([[1, 2, 1], [1, 3, 5], [2, 3, 1]], 3, 1, 2),
            ([[2, 1, 1], [2, 3, 1], [3, 4, 1], [4, 5, 1]], 5, 2, 3),
            ([[1, 2, 2]], 2, 1, 2),
            ([[1, 3, 1], [3, 2, 1]], 3, 2, -1),
            ([[1, 2, 0], [2, 3, 0]], 3, 1, 0),
        ],
    )
    def test_network_delay_time(self, times: list[list[int]], n: int, k: int, expected: int):
        result = run_network_delay_time(Solution, times, n, k)
        assert_network_delay_time(result, expected)
