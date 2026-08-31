import pytest

from leetcode_py import logged_test

from .helpers import assert_least_bricks, run_least_bricks
from .solution import Solution


class TestBrickWall:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "wall, expected",
        [
            ([[1, 2, 2, 1], [3, 1, 2], [1, 3, 2], [2, 4], [3, 1, 2], [1, 3, 1, 1]], 2),
            ([[1], [1], [1]], 3),
            ([[1, 1], [2], [1, 1]], 1),
            ([[1000000000], [1000000000]], 2),
            ([[1, 2], [2, 1], [3]], 2),
            ([[1, 1, 1], [1, 1, 1], [3]], 1),
            ([[5]], 1),
            ([[2, 2], [2, 2], [2, 2], [4]], 1),
            ([[1, 3], [2, 2], [3, 1], [4]], 3),
            ([[7, 1, 2], [3, 5, 2], [8, 2], [6, 4]], 1),
            ([[1, 1, 1, 1], [1, 1, 1, 1]], 0),
            ([[3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3], [3, 3, 3]], 0),
        ],
    )
    def test_least_bricks(self, wall: list[list[int]], expected: int):
        result = run_least_bricks(Solution, wall)
        assert_least_bricks(result, expected)
