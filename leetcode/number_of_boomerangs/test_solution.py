import pytest

from leetcode_py import logged_test

from .helpers import assert_number_of_boomerangs, run_number_of_boomerangs
from .solution import Solution


class TestNumberOfBoomerangs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "points, expected",
        [
            ([[0, 0], [1, 0], [2, 0]], 2),
            ([[1, 1], [2, 2], [3, 3]], 2),
            ([[1, 1]], 0),
            ([[0, 0], [1, 0]], 0),
            ([[0, 0], [1, 0], [0, 1]], 2),
            ([[0, 0], [3, 4]], 0),
            ([[0, 0], [1, 0], [2, 0], [3, 0]], 4),
            ([[0, 0], [0, 1], [0, 2], [0, 3]], 4),
            ([[0, 0], [1, 0], [0, 1], [1, 1]], 8),
            ([[0, 0], [1, 0], [-1, 0]], 2),
            ([[0, 0], [1, 1], [2, 2], [3, 3], [4, 4]], 8),
            ([[0, 0], [1, 1], [-1, -1], [2, 2]], 4),
            ([[5, 5], [5, 6], [6, 5], [4, 5], [5, 4]], 20),
            ([[0, 0], [2, 1], [4, 2], [6, 3]], 4),
            ([[5, 3], [-5, 4], [1, 1], [5, -3], [-4, -1]], 0),
            ([[2, 2], [3, -2]], 0),
            ([[3, 4], [-3, 5]], 0),
            ([[-2, -4], [0, 5], [-5, 4], [-3, 1]], 0),
            ([[5, -2], [5, 1], [1, -3], [1, 2], [-2, 1], [-3, 1]], 6),
            ([[-2, -5], [2, -5], [-4, 5], [-4, 0], [0, -3]], 4),
            ([[5, -1], [1, -1], [3, -4], [-2, -1], [-1, -3]], 2),
            ([[2, 4], [-2, 4], [4, 2], [-4, 1], [4, -4]], 0),
            ([[5, 4], [4, 2], [1, -3], [-4, -3]], 0),
            ([[4, 5], [3, -5], [2, -2]], 0),
        ],
    )
    def test_number_of_boomerangs(self, points: list[list[int]], expected: int):
        result = run_number_of_boomerangs(Solution, points)
        assert_number_of_boomerangs(result, expected)
