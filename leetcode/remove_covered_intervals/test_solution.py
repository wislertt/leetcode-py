import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_covered_intervals, run_remove_covered_intervals
from .solution import Solution


class TestRemoveCoveredIntervals:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "intervals, expected",
        [
            [[[1, 4], [3, 6], [2, 8]], 2],
            [[[1, 4], [2, 3]], 1],
            [[[1, 2]], 1],
            [[[1, 4], [2, 4], [3, 4]], 1],
            [[[1, 4], [1, 3], [0, 5]], 1],
            [[[1, 2], [2, 3], [3, 4]], 3],
            [[[0, 10], [1, 2], [3, 4]], 1],
            [[[1, 3], [2, 4]], 2],
            [[[5, 6], [1, 2], [3, 4]], 3],
            [[[0, 1], [0, 2], [0, 3], [0, 4]], 1],
            [[[0, 8], [5, 8], [7, 9], [5, 6], [6, 9], [5, 7]], 2],
            [[[1, 2], [1, 9]], 1],
            [[[0, 1], [2, 10], [7, 8], [4, 10], [1, 7], [9, 10]], 3],
            [[[3, 8], [9, 10]], 2],
            [[[4, 8], [2, 4], [1, 5], [3, 6]], 3],
            [[[5, 7], [2, 8], [2, 5]], 1],
        ],
    )
    def test_remove_covered_intervals(self, intervals: list[list[int]], expected: int):
        result = run_remove_covered_intervals(Solution, intervals)
        assert_remove_covered_intervals(result, expected)
