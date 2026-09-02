import pytest

from leetcode_py import logged_test

from .helpers import assert_find_right_interval, run_find_right_interval
from .solution import Solution


class TestFindRightInterval:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "intervals, expected",
        [
            ([[1, 2]], [-1]),
            ([[3, 4], [2, 3], [1, 2]], [-1, 0, 1]),
            ([[1, 4], [2, 3], [3, 4]], [-1, 2, -1]),
            ([[1, 1]], [0]),
            ([[5, 5], [1, 5]], [0, 0]),
            ([[1, 2], [2, 3], [3, 4]], [1, 2, -1]),
            ([[-3, -2], [-1, 0], [0, 1]], [1, 2, -1]),
            ([[1, 12], [2, 9], [3, 10], [13, 14], [15, 16]], [3, 3, 3, 4, -1]),
            ([[-1000000, 1000000]], [-1]),
            ([[4, 5], [2, 3], [1, 2]], [-1, 0, 1]),
            ([[9, 10], [2, 3], [5, 6], [1, 2], [6, 7], [3, 4]], [-1, 5, 4, 1, 0, 2]),
            ([[-5, 0], [4, 8], [-6, -6], [7, 8], [-3, -1]], [1, -1, 2, -1, 1]),
            ([[-7, -4], [8, 11], [-1, 4], [6, 7], [-8, -4], [0, 4]], [2, -1, 3, 1, 2, 3]),
            ([[-7, -3], [-4, -3], [-3, 2], [-6, -1], [-2, 2]], [2, 2, -1, -1, -1]),
            ([[-1, 0], [0, 3], [-2, 3], [-4, 1]], [1, -1, -1, -1]),
            ([[7, 11], [8, 8]], [-1, 1]),
        ],
    )
    def test_find_right_interval(self, intervals: list[list[int]], expected: list[int]):
        result = run_find_right_interval(Solution, intervals)
        assert_find_right_interval(result, expected)
