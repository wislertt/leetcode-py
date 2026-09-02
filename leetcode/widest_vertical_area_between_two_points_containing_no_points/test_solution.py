import pytest

from leetcode_py import logged_test

from .helpers import assert_max_width_of_vertical_area, run_max_width_of_vertical_area
from .solution import Solution


class TestWidestVerticalAreaBetweenTwoPointsContainingNoPoints:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "points, expected",
        [
            ([[8, 7], [9, 9], [7, 4], [9, 7]], 1),
            ([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]], 3),
            ([[1, 1], [1, 2]], 0),
            ([[1, 5], [1, 5], [1, 5]], 0),
            ([[7, 4], [7, 1], [7, 9]], 0),
            ([[0, 0], [0, 0]], 0),
            ([[0, 0], [1000000000, 1]], 1000000000),
            ([[1000000000, 0], [0, 1000000000]], 1000000000),
            ([[1, 3], [2, 2], [4, 1]], 2),
            ([[2, 1], [1, 1], [4, 1], [6, 1]], 2),
            ([[5, 5], [1, 1], [9, 9], [3, 3]], 4),
            ([[10, 0], [1, 0], [3, 0], [7, 0], [2, 0]], 4),
            ([[1, 1], [3, 1], [3, 2], [6, 1]], 3),
            ([[4, 0], [8, 0], [2, 0], [6, 0], [0, 0], [10, 0]], 2),
            ([[10, 9], [3, 6], [6, 4], [2, 0], [13, 2], [17, 6], [12, 3], [5, 5]], 4),
            ([[19, 0], [13, 1], [3, 0]], 10),
            ([[0, 4], [2, 1], [16, 4], [12, 3], [3, 5]], 9),
            ([[11, 5], [5, 8], [13, 7], [4, 9], [16, 6]], 6),
            ([[8, 3], [1, 1], [14, 7], [15, 0], [3, 8], [9, 6], [18, 3], [10, 1]], 5),
            ([[15, 8], [18, 5], [10, 6], [8, 4], [11, 5]], 4),
            ([[16, 6], [6, 9], [3, 8]], 10),
            ([[8, 2], [11, 9], [3, 7]], 5),
        ],
    )
    def test_max_width_of_vertical_area(self, points: list[list[int]], expected: int):
        result = run_max_width_of_vertical_area(Solution, points)
        assert_max_width_of_vertical_area(result, expected)
