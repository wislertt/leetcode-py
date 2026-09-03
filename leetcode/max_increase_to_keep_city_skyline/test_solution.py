import pytest

from leetcode_py import logged_test

from .helpers import assert_max_increase_keeping_skyline, run_max_increase_keeping_skyline
from .solution import Solution


class TestMaxIncreaseToKeepCitySkyline:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]], 35),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
            ([[1, 2], [3, 4]], 1),
            ([[5, 5], [5, 5]], 0),
            ([[0, 0], [0, 0]], 0),
            ([[10, 0], [0, 10]], 20),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0),
            ([[9, 9, 9], [9, 9, 9], [9, 9, 9]], 0),
            ([[100, 100], [100, 100]], 0),
            ([[0, 100], [100, 0]], 200),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 6),
            ([[9, 8, 7], [6, 5, 4], [3, 2, 1]], 6),
            ([[94, 12, 97], [21, 29, 38], [22, 71, 19]], 186),
            ([[0, 2, 6, 1], [9, 2, 7, 5], [8, 3, 8, 5], [3, 2, 6, 6]], 20),
            ([[0, 7, 3, 7], [5, 2, 0, 5], [5, 7, 6, 9], [7, 6, 0, 4]], 30),
            ([[5, 2, 7, 0], [9, 3, 4, 9], [7, 3, 7, 0], [5, 0, 5, 5]], 23),
            ([[19, 9, 86], [80, 58, 54], [11, 72, 42]], 255),
            ([[46, 13], [68, 86]], 33),
            ([[80, 66, 35], [44, 48, 12], [45, 14, 6]], 87),
            ([[76, 41, 82], [33, 71, 94], [79, 35, 92]], 115),
            ([[60, 39], [74, 2]], 37),
            ([[45, 7, 67], [68, 71, 49], [22, 94, 74]], 150),
        ],
    )
    def test_max_increase_keeping_skyline(self, grid: list[list[int]], expected: int):
        result = run_max_increase_keeping_skyline(Solution, grid)
        assert_max_increase_keeping_skyline(result, expected)
