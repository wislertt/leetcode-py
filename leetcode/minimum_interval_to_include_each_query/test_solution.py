import pytest

from leetcode_py import logged_test

from .helpers import assert_min_interval, run_min_interval
from .solution import Solution


class TestMinimumIntervalToIncludeEachQuery:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "intervals, queries, expected",
        [
            ([[1, 4], [2, 4], [3, 6], [4, 4]], [2, 3, 4, 5], [3, 3, 1, 4]),
            ([[2, 3], [2, 5], [1, 8], [20, 25]], [2, 19, 5, 22], [2, -1, 4, 6]),
            ([[1, 5]], [3], [5]),
            ([[1, 5]], [6], [-1]),
            ([[1, 1]], [1], [1]),
            ([[1, 10], [2, 3]], [2], [2]),
            ([[5, 10]], [1, 5, 10, 11], [-1, 6, 6, -1]),
            ([[1, 3], [2, 6], [8, 10]], [1, 2, 4, 9, 7], [3, 3, 5, 3, -1]),
            ([[1, 4], [4, 4]], [4], [1]),
            ([[1, 5]], [3, 3, 3], [5, 5, 5]),
            ([[1, 100], [2, 3], [3, 4]], [3], [2]),
            ([[10, 20]], [15], [11]),
            ([[1, 2], [3, 4], [5, 6]], [1, 2, 3, 4, 5, 6, 7], [2, 2, 2, 2, 2, 2, -1]),
            ([[5, 5], [5, 5]], [5], [1]),
        ],
    )
    def test_min_interval(
        self, intervals: list[list[int]], queries: list[int], expected: list[int]
    ):
        result = run_min_interval(Solution, intervals, queries)
        assert_min_interval(result, expected)
