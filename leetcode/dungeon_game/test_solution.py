import pytest

from leetcode_py import logged_test

from .helpers import assert_calculate_minimum_hp, run_calculate_minimum_hp
from .solution import Solution


class TestDungeonGame:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "dungeon, expected",
        [
            ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7),
            ([[0]], 1),
            ([[5]], 1),
            ([[-5]], 6),
            ([[-100]], 101),
            ([[100]], 1),
            ([[0, 0], [0, 0]], 1),
            ([[-1, -1], [-1, -1]], 4),
            ([[1, 2], [3, 4]], 1),
            ([[-3, 5], [5, -3]], 4),
            ([[2, 1], [1, -1]], 1),
            ([[1, -3, 3], [0, -2, 0], [-3, -3, -3]], 3),
            ([[-6, 1, -1, -5]], 12),
            ([[-5, 5], [-1, 0]], 6),
            ([[4], [-1], [5]], 1),
            ([[4, 1, -6], [2, 6, 6], [-5, 4, 2]], 1),
            ([[1, 1, -2]], 1),
            ([[-1, 4, 1]], 2),
        ],
    )
    def test_calculate_minimum_hp(self, dungeon: list[list[int]], expected: int):
        result = run_calculate_minimum_hp(Solution, dungeon)
        assert_calculate_minimum_hp(result, expected)
