import pytest

from leetcode_py import logged_test

from .helpers import assert_max_killed_enemies, run_max_killed_enemies
from .solution import Solution


class TestBombEnemy:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]], 3),
            ([["W", "W", "W"], ["0", "0", "0"], ["E", "E", "E"]], 1),
            ([["E"]], 0),
            ([["0"]], 0),
            ([["W"]], 0),
            ([["E", "E", "E"]], 0),
            ([["E", "W", "E"]], 0),
            ([["E"], ["E"], ["W"], ["E"]], 0),
            ([["0", "E"], ["E", "0"]], 2),
            ([["0", "0"], ["0", "0"]], 0),
            ([["E", "0", "E"], ["0", "E", "0"], ["E", "0", "E"]], 3),
            ([["0", "E", "W", "E"], ["E", "0", "0", "E"]], 3),
            ([["E", "0"], ["E", "0"]], 1),
            ([["W", "0", "E"], ["E", "0", "W"], ["0", "E", "0"]], 2),
            ([["0", "W", "0", "E"], ["E", "0", "W", "0"]], 1),
            ([["E", "E"], ["E", "0"]], 2),
        ],
    )
    def test_max_killed_enemies(self, grid: list[list[str]], expected: int):
        result = run_max_killed_enemies(Solution, grid)
        assert_max_killed_enemies(result, expected)
