import pytest

from leetcode_py import logged_test

from .helpers import assert_divide_players, run_divide_players
from .solution import Solution


class TestDividePlayersIntoTeamsOfEqualSkill:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "skill, expected",
        [
            ([3, 2, 5, 1, 3, 4], 22),
            ([3, 4], 12),
            ([1, 1, 2, 3], -1),
            ([1, 1], 1),
            ([1, 2], 2),
            ([1000, 1000], 1000000),
            ([999, 1], 999),
            ([1, 1, 1, 1], 2),
            ([1, 1, 1, 2], -1),
            ([2, 2, 3, 3], 12),
            ([2, 3, 4, 5], 22),
            ([5, 5, 5, 5, 5, 5], 75),
            ([1, 2, 3, 4, 5, 6], 28),
            ([10, 20, 30, 40], 1000),
            ([1, 4, 3, 2], 10),
            ([3, 5, 1, 7, 2, 6, 4, 8], 60),
            ([2, 2, 2, 2, 2, 3], -1),
            ([1, 1, 4, 6], -1),
            ([2, 2, 2, 3, 3, 3], 18),
            ([1, 3, 3, 1, 2, 2], 10),
        ],
    )
    def test_divide_players(self, skill: list[int], expected: int):
        result = run_divide_players(Solution, skill)
        assert_divide_players(result, expected)
