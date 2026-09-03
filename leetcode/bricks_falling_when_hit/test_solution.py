import pytest

from leetcode_py import logged_test

from .helpers import assert_hit_bricks, run_hit_bricks
from .solution import Solution


class TestBricksFallingWhenHit:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, hits, expected",
        [
            ([[1, 0, 0, 0], [1, 1, 1, 0]], [[1, 0]], [2]),
            ([[1, 0, 0, 0], [1, 1, 0, 0]], [[1, 1], [1, 0]], [0, 0]),
            ([[1, 1], [1, 1]], [[0, 0]], [0]),
            ([[1, 1], [1, 1]], [[0, 0], [0, 1], [1, 0]], [0, 2, 0]),
            ([[0, 1], [0, 1]], [[0, 0]], [0]),
            ([[1, 0], [0, 1]], [[1, 1]], [0]),
            ([[1, 0], [1, 0]], [[0, 0]], [1]),
            ([[1, 0, 1], [1, 0, 1]], [[1, 2]], [0]),
            ([[1, 1], [1, 1]], [[0, 1]], [0]),
            ([[0, 0], [0, 0]], [[0, 0], [1, 1]], [0, 0]),
            ([[0, 1], [0, 1], [0, 1]], [[0, 1]], [2]),
            ([[1, 0], [1, 0], [1, 0]], [[1, 0]], [1]),
            ([[1, 0, 0], [1, 1, 0], [1, 1, 1]], [[0, 0]], [5]),
            ([[1, 1]], [[0, 1]], [0]),
            ([[1, 0], [1, 0]], [[0, 1], [1, 1]], [0, 0]),
            ([[1, 1, 0], [1, 1, 0], [0, 1, 1], [1, 1, 1]], [[1, 0], [2, 0], [3, 0]], [0, 0, 0]),
            ([[0, 1], [0, 1], [1, 1]], [[0, 0]], [0]),
            ([[1, 1, 0], [1, 1, 0], [1, 0, 1]], [[2, 2]], [0]),
            ([[1], [0]], [[1, 0]], [0]),
            ([[1, 0], [1, 0], [1, 0]], [[0, 0], [0, 1], [1, 0], [1, 1]], [2, 0, 0, 0]),
        ],
    )
    def test_hit_bricks(self, grid: list[list[int]], hits: list[list[int]], expected: list[int]):
        result = run_hit_bricks(Solution, grid, hits)
        assert_hit_bricks(result, expected)
