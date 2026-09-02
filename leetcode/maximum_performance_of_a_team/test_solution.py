import pytest

from leetcode_py import logged_test

from .helpers import assert_max_performance, run_max_performance
from .solution import Solution


class TestMaximumPerformanceOfATeam:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, speed, efficiency, k, expected",
        [
            (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2, 60),
            (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 3, 68),
            (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 4, 72),
            (6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 6, 72),
            (1, [5], [7], 1, 35),
            (2, [3, 4], [1, 2], 1, 8),
            (2, [3, 4], [1, 2], 2, 8),
            (3, [1, 1, 1], [5, 5, 5], 2, 10),
            (4, [4, 2, 3, 5], [1, 8, 6, 2], 2, 30),
            (4, [10, 10, 10, 1], [9, 8, 1, 8], 3, 168),
            (5, [7, 1, 9, 3, 5], [2, 6, 4, 8, 3], 2, 48),
            (5, [7, 1, 9, 3, 5], [2, 6, 4, 8, 3], 5, 54),
            (3, [100000, 100000, 100000], [100000000, 1, 1], 1, 999930007),
            (3, [100000, 100000, 100000], [100000000, 100000000, 100000000], 3, 999790007),
            (2, [1, 100000], [100000000, 1], 2, 100000000),
            (1, [10], [23], 1, 230),
            (1, [18], [8], 1, 144),
            (6, [8, 13, 14, 12, 13, 5], [20, 12, 17, 15, 29, 24], 6, 780),
            (3, [3, 14, 13], [6, 12, 16], 2, 324),
            (3, [3, 18, 3], [9, 21, 4], 3, 378),
        ],
    )
    def test_max_performance(
        self, n: int, speed: list[int], efficiency: list[int], k: int, expected: int
    ):
        result = run_max_performance(Solution, n, speed, efficiency, k)
        assert_max_performance(result, expected)
