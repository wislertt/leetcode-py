import pytest

from leetcode_py import logged_test

from .helpers import assert_find_missing_and_repeated_values, run_find_missing_and_repeated_values
from .solution import Solution


class TestFindMissingAndRepeatedValues:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 3], [2, 2]], [2, 4]),
            ([[9, 1, 7], [8, 9, 2], [3, 4, 6]], [9, 5]),
            ([[1, 3], [1, 2]], [1, 4]),
            ([[2, 4], [4, 3]], [4, 1]),
            ([[1, 2], [4, 2]], [2, 3]),
            ([[3, 1], [4, 3]], [3, 2]),
            ([[7, 5, 1], [3, 8, 2], [6, 4, 1]], [1, 9]),
            ([[5, 8, 9], [9, 6, 4], [2, 3, 7]], [9, 1]),
            ([[12, 11, 14, 7], [4, 13, 8, 5], [3, 6, 16, 9], [15, 10, 2, 16]], [16, 1]),
            ([[6, 3, 14, 1], [9, 4, 2, 5], [1, 7, 11, 12], [13, 15, 10, 8]], [1, 16]),
            ([[5, 9, 3], [2, 5, 8], [6, 4, 1]], [5, 7]),
            ([[9, 2, 7], [5, 3, 1], [4, 6, 2]], [2, 8]),
            ([[2, 6, 5, 3], [9, 15, 16, 10], [1, 6, 13, 4], [7, 8, 12, 14]], [6, 11]),
            ([[10, 8, 14, 15], [3, 13, 7, 12], [6, 16, 5, 11], [9, 15, 1, 4]], [15, 2]),
            ([[9, 11, 12, 15], [5, 9, 1, 6], [8, 7, 3, 4], [10, 2, 14, 13]], [9, 16]),
            ([[3, 7, 10, 5], [6, 14, 1, 3], [4, 11, 16, 9], [2, 12, 8, 15]], [3, 13]),
            ([[3, 2], [4, 2]], [2, 1]),
            ([[4, 3], [1, 3]], [3, 2]),
            ([[7, 4, 9], [2, 6, 9], [1, 5, 3]], [9, 8]),
            ([[1, 3, 6], [9, 2, 7], [4, 6, 8]], [6, 5]),
            ([[12, 13, 11, 16], [4, 3, 5, 1], [15, 9, 2, 11], [7, 14, 6, 8]], [11, 10]),
        ],
    )
    def test_find_missing_and_repeated_values(self, grid: list[list[int]], expected: list[int]):
        result = run_find_missing_and_repeated_values(Solution, grid)
        assert_find_missing_and_repeated_values(result, expected)
