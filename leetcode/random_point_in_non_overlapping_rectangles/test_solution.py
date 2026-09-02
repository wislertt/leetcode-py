import pytest

from leetcode_py import logged_test

from .helpers import assert_pick, run_pick
from .solution import Solution


class TestRandomPointInNonOverlappingRectangles:
    @logged_test
    @pytest.mark.parametrize(
        "rects, seed, n",
        [
            ([[-2, -2, 1, 1], [2, 2, 4, 6]], 0, 2000),
            ([[-2, -2, 1, 1], [2, 2, 4, 6]], 1, 31),
            ([[1, 1, 2, 2]], 2, 100),
            ([[1, 1, 5, 5]], 3, 500),
            ([[0, 0, 3, 3]], 4, 400),
            ([[-5, -4, 5, 4]], 5, 2000),
            ([[0, 0, 1, 1], [-3, -3, -1, -1]], 6, 2000),
            ([[0, 0, 2, 2], [3, 3, 5, 7]], 7, 2000),
            ([[-100, -100, 100, 100]], 8, 2000),
            ([[1, 2, 3, 4]], 9, 20),
            ([[0, 0, 2000, 2000]], 10, 50),
            ([[0, 0, 1, 1], [2, 2, 3, 3], [5, 5, 9, 9]], 11, 2000),
            ([[1, 1, 2, 5], [-1, -1, 0, 3]], 12, 2000),
            ([[-1000, -1000, 1000, 1000]], 13, 10),
            ([[0, 0, 1, 1], [-3, -1, -2, 0], [2, -1, 3, 0]], 14, 2000),
        ],
    )
    def test_pick(self, rects: list[list[int]], seed: int, n: int):
        result = run_pick(Solution, rects, seed, n)
        assert_pick(result, rects, n)
