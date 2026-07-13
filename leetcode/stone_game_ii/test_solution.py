import pytest

from leetcode_py import logged_test

from .helpers import assert_stone_game_ii, run_stone_game_ii
from .solution import Solution


class TestStoneGameII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "piles, expected",
        [
            ([2, 7, 9, 4, 4], 10),
            ([1, 2, 3, 4, 5, 100], 104),
            ([1], 1),
            ([5], 5),
            ([1, 1], 2),
            ([1, 2], 3),
            ([2, 2], 4),
            ([1, 2, 3], 3),
            ([1, 2, 3, 4], 5),
            ([1, 1, 1, 1, 1, 1], 3),
            ([10, 100], 110),
            ([100, 10], 110),
            ([1, 2, 3, 4, 5], 8),
            ([5, 4, 3, 2, 1], 9),
            ([1, 1, 1, 1], 2),
            ([7, 7, 7, 7], 14),
        ],
    )
    def test_stone_game_ii(self, piles: list[int], expected: int):
        result = run_stone_game_ii(Solution, piles)
        assert_stone_game_ii(result, expected)
