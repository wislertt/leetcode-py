import pytest

from leetcode_py import logged_test

from .helpers import assert_max_points, run_max_points
from .solution import Solution


class TestMaxPointsOnALine:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "points, expected",
        [
            ([[1, 1], [2, 2], [3, 3]], 3),
            ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
            ([[1, 1]], 1),
            ([[1, 1], [1, 2], [1, 3]], 3),
            ([[1, 1], [2, 1], [3, 1]], 3),
            ([[0, 0], [1, 1], [2, 2], [3, 3], [3, 2]], 4),
            ([[0, 0], [1, 0], [2, 0], [0, 1], [0, 2]], 3),
            ([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 8]], 4),
            ([[0, 0], [1, 1], [0, 1], [1, 0], [2, 2], [2, 0]], 3),
            ([[1, 1], [1, 1], [1, 1]], 3),
            ([[0, 0], [1, 1], [2, 4], [3, 9], [4, 16]], 2),
            ([[1, 1], [2, 3], [3, 5], [4, 7]], 4),
            ([[0, 0], [1, 2], [2, 4], [3, 6], [0, 1]], 4),
            ([[1, 0], [2, 0], [3, 0], [0, 1], [0, 2], [0, 3]], 3),
            ([[0, 0], [1, 1], [1, -1], [2, 2], [2, -2]], 3),
        ],
    )
    def test_max_points(self, points: list[list[int]], expected: int):
        result = run_max_points(Solution, points)
        assert_max_points(result, expected)
