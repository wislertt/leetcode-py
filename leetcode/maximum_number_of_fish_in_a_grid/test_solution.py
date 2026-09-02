import pytest

from leetcode_py import logged_test

from .helpers import assert_find_max_fish, run_find_max_fish
from .solution import Solution


class TestMaximumNumberOfFishInAGrid:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]], 7),
            ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 1),
            ([[0]], 0),
            ([[5]], 5),
            ([[0, 0], [0, 0]], 0),
            ([[10, 10], [10, 10]], 40),
            ([[1, 0], [0, 1]], 1),
            ([[1, 1], [1, 0]], 3),
            ([[0, 3], [4, 0]], 4),
            ([[7, 0, 7]], 7),
            ([[2], [0], [2]], 2),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0),
            ([[1, 2], [3, 4]], 10),
            ([[0, 4, 0, 0], [2, 0, 5, 0], [0, 0, 0, 0], [1, 0, 3, 6]], 9),
            ([[0, 1, 0, 0, 0], [0, 2, 0, 3, 0], [0, 0, 4, 0, 0]], 4),
            ([[9, 0, 0, 9], [0, 0, 0, 0], [9, 0, 0, 9]], 9),
            ([[8, 2, 10, 5]], 25),
            ([[5, 5, 6], [4, 8, 4], [0, 1, 1], [0, 2, 8], [8, 2, 7]], 61),
        ],
    )
    def test_find_max_fish(self, grid: list[list[int]], expected: int):
        result = run_find_max_fish(Solution, grid)
        assert_find_max_fish(result, expected)
