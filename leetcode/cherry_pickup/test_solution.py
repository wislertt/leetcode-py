import pytest

from leetcode_py import logged_test

from .helpers import assert_cherry_pickup, run_cherry_pickup
from .solution import Solution


class TestCherryPickup:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 1, -1], [1, 0, -1], [1, 1, 1]], 5),
            ([[1, 1, -1], [1, -1, 1], [-1, 1, 1]], 0),
            ([[0]], 0),
            ([[1]], 1),
            ([[0, 1], [1, 0]], 2),
            ([[1, 0], [0, 1]], 2),
            ([[0, 0], [0, 0]], 0),
            ([[1, 1], [1, 1]], 4),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 8),
            ([[1, -1, 1], [1, 1, 1], [-1, 1, 1]], 6),
            ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 6),
            ([[1, -1, 0], [0, 0, 1], [-1, 1, 1]], 4),
            ([[0, 0, 1], [1, 0, 1], [1, 1, 0]], 5),
            ([[0, 1, 0], [0, 0, 0], [0, 0, 0]], 1),
        ],
    )
    def test_cherry_pickup(self, grid: list[list[int]], expected: int):
        result = run_cherry_pickup(Solution, grid)
        assert_cherry_pickup(result, expected)
