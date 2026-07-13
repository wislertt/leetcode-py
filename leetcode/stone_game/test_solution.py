import pytest

from leetcode_py import logged_test

from .helpers import assert_stone_game, run_stone_game
from .solution import Solution


class TestStoneGame:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "piles, expected",
        [
            ([5, 3, 4, 5], True),
            ([3, 7, 2, 3], True),
            ([1, 2], True),
            ([2, 1], True),
            ([1, 2, 3, 4], True),
            ([4, 3, 2, 1], True),
            ([5, 1, 5, 1], True),
            ([1, 5, 1, 5], True),
            ([3, 9, 1, 2], True),
            ([10, 20, 30, 40], True),
            ([100, 50, 200, 75], True),
            ([7, 7, 7, 7, 7, 8], True),
            ([9, 8, 7, 6, 5, 4], True),
            ([1, 100, 2, 99], True),
            ([500, 1, 500, 1], True),
            ([2, 4, 6, 8, 10, 12], True),
            ([13, 11, 9, 7, 5, 3], True),
            ([1, 3, 5, 7, 9, 11], True),
        ],
    )
    def test_stone_game(self, piles: list[int], expected: bool):
        result = run_stone_game(Solution, piles)
        assert_stone_game(result, expected)
