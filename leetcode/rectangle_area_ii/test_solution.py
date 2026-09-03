import pytest

from leetcode_py import logged_test

from .helpers import assert_rectangle_area, run_rectangle_area
from .solution import Solution


class TestRectangleAreaII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "rectangles, expected",
        [
            ([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]], 6),
            ([[0, 0, 1000000000, 1000000000]], 49),
            ([[0, 0, 1, 1]], 1),
            ([[0, 0, 1, 1], [2, 2, 3, 3]], 2),
            ([[0, 0, 1, 1], [0, 0, 1, 1], [0, 0, 1, 1]], 1),
            ([[0, 0, 10, 10], [2, 2, 5, 5]], 100),
            ([[0, 0, 1, 1], [1, 0, 2, 1]], 2),
            ([[0, 0, 3, 3], [1, 1, 2, 2]], 9),
            ([[0, 0, 5, 5], [5, 5, 10, 10]], 50),
            ([[0, 0, 2, 2], [2, 0, 4, 2], [4, 0, 6, 2]], 12),
            ([[7, 1, 11, 3], [4, 1, 11, 2], [5, 4, 10, 6], [6, 9, 9, 11]], 27),
            ([[9, 1, 10, 4], [5, 2, 10, 10], [1, 4, 5, 8], [6, 9, 9, 10]], 57),
            ([[5, 3, 10, 6], [1, 3, 11, 6], [2, 6, 6, 11]], 50),
            ([[5, 3, 9, 6], [1, 8, 3, 10], [9, 2, 11, 6]], 24),
            ([[1, 8, 6, 9], [0, 5, 3, 10]], 18),
            ([[10, 6, 11, 9], [6, 4, 8, 11]], 17),
            ([[8, 0, 9, 11], [8, 9, 11, 10], [5, 8, 9, 9], [9, 7, 11, 8]], 18),
            ([[2, 3, 8, 5], [5, 8, 8, 11], [6, 9, 9, 10]], 22),
            ([[0, 0, 1000000000, 1000000000], [0, 0, 1000000000, 500000000]], 49),
        ],
    )
    def test_rectangle_area(self, rectangles: list[list[int]], expected: int):
        result = run_rectangle_area(Solution, rectangles)
        assert_rectangle_area(result, expected)
