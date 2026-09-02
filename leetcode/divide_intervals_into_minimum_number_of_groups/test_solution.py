import pytest

from leetcode_py import logged_test

from .helpers import assert_min_groups, run_min_groups
from .solution import Solution


class TestDivideIntervalsIntoMinimumNumberOfGroups:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "intervals, expected",
        [
            ([[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]], 3),
            ([[1, 3], [5, 6], [8, 10], [11, 13]], 1),
            ([[1, 1]], 1),
            ([[1, 5], [1, 5]], 2),
            ([[1, 5], [5, 10]], 2),
            ([[1, 5], [6, 10]], 1),
            ([[1, 10], [2, 3], [4, 5], [6, 7]], 2),
            ([[1, 3], [2, 4], [3, 5], [4, 6], [5, 7]], 3),
            ([[1, 1000000], [1, 1000000], [1, 1000000]], 3),
            ([[2, 3], [1, 2], [3, 4], [4, 5], [5, 6]], 2),
            ([[441, 743], [218, 558], [647, 927], [647, 849], [340, 970]], 4),
            ([[10, 12], [5, 9], [10, 13], [2, 5]], 2),
            ([[11, 14], [12, 13], [12, 16], [7, 11]], 3),
            ([[12, 12], [7, 8], [10, 11], [8, 14]], 2),
            ([[2, 6], [5, 11]], 2),
            ([[5, 7]], 1),
            ([[2, 7], [9, 12]], 1),
            ([[8, 8]], 1),
            ([[3, 9], [8, 14], [8, 10], [10, 15], [11, 13]], 3),
            ([[9, 9], [6, 8], [9, 14], [12, 15], [2, 8], [1, 5], [7, 10]], 3),
        ],
    )
    def test_min_groups(self, intervals: list[list[int]], expected: int):
        result = run_min_groups(Solution, intervals)
        assert_min_groups(result, expected)
