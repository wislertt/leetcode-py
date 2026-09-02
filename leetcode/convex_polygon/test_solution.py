import pytest

from leetcode_py import logged_test

from .helpers import assert_is_convex, run_is_convex
from .solution import Solution


class TestConvexPolygon:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "points, expected",
        [
            ([[0, 0], [0, 5], [5, 5], [5, 0]], True),
            ([[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]], False),
            ([[0, 0], [5, 0], [5, 5], [0, 5]], True),
            ([[0, 0], [2, 0], [1, 1], [0, 2]], True),
            ([[0, 0], [0, 1], [0, 2], [1, 1]], True),
            ([[0, 0], [1, 1], [2, 0]], True),
            ([[0, 0], [4, 0], [4, 4], [2, 1]], False),
            ([[0, 0], [0, 4], [4, 2], [2, 2]], False),
            ([[1, 1], [5, 1], [5, 5], [3, 7], [1, 5]], True),
            ([[0, 0], [-2, -2], [-4, 0]], True),
            ([[0, 0], [10, 0], [10, 10], [5, 10], [5, 5], [0, 5]], False),
            ([[-5, -5], [-5, 5], [5, 5], [5, -5]], True),
        ],
    )
    def test_is_convex(self, points: list[list[int]], expected: bool):
        result = run_is_convex(Solution, points)
        assert_is_convex(result, expected)
