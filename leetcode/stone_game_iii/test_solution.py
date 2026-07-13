import pytest

from leetcode_py import logged_test

from .helpers import assert_stone_game_iii, run_stone_game_iii
from .solution import Solution


class TestStoneGameIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "stone_value, expected",
        [
            ([1, 2, 3, 7], "Bob"),
            ([1, 2, 3, -9], "Alice"),
            ([1, 2, 3, 6], "Tie"),
            ([1], "Alice"),
            ([1, 2, 3], "Alice"),
            ([-1], "Bob"),
            ([-1, -2, -3], "Tie"),
            ([0, 0, 0], "Tie"),
            ([-1, 0, 1], "Tie"),
            ([5], "Alice"),
            ([-1, -1, -1], "Bob"),
            ([2, 2, 2], "Alice"),
            ([1, 1, 1, 1, 1, 1], "Tie"),
            ([1, 1, 1, 1, 1], "Alice"),
            ([1, 1], "Alice"),
            ([10, -1, -1, -1], "Alice"),
            ([3, 3, 3, 3], "Alice"),
            ([1, -1, 1, -1, 1, -1], "Alice"),
        ],
    )
    def test_stone_game_iii(self, stone_value: list[int], expected: str):
        result = run_stone_game_iii(Solution, stone_value)
        assert_stone_game_iii(result, expected)
