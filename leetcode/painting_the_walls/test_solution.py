import pytest

from leetcode_py import logged_test

from .helpers import assert_paint_walls, run_paint_walls
from .solution import Solution


class TestPaintingTheWalls:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "cost, time, expected",
        [
            ([1, 2, 3, 2], [1, 2, 3, 2], 3),
            ([2, 3, 4, 2], [1, 1, 1, 1], 4),
            ([1], [1], 1),
            ([5], [3], 5),
            ([1, 2], [2, 1], 1),
            ([2, 1], [1, 2], 1),
            ([1, 1, 1], [1, 1, 1], 2),
            ([2, 2, 2], [3, 3, 3], 2),
            ([1, 2, 3], [1, 1, 1], 3),
            ([3, 1, 2], [1, 2, 1], 1),
            ([1, 1000000], [1, 500], 1),
            ([1000000, 1], [500, 1], 1),
            ([4, 2, 1], [1, 1, 1], 3),
            ([2, 3, 1, 1], [1, 2, 3, 4], 1),
            ([1, 2, 1, 3, 2], [1, 2, 3, 1, 2], 2),
            ([5, 1, 3, 2, 4], [2, 1, 3, 1, 2], 4),
            ([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], 3),
            ([7, 2, 9, 1, 3, 5], [3, 1, 2, 1, 4, 2], 4),
            ([10, 1, 1, 1], [1, 1, 5, 1], 1),
        ],
    )
    def test_paint_walls(self, cost: list[int], time: list[int], expected: int):
        result = run_paint_walls(Solution, cost, time)
        assert_paint_walls(result, expected)
