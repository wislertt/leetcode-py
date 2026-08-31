import pytest

from leetcode_py import logged_test

from .helpers import assert_new21_game, run_new21_game
from .solution import Solution


class TestNew21Game:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, max_pts, expected",
        [
            (10, 1, 10, 1.0),
            (6, 1, 10, 0.6),
            (21, 17, 10, 0.73278),
            (0, 0, 1, 1.0),
            (5, 0, 3, 1.0),
            (1, 1, 1, 1.0),
            (2, 1, 2, 1.0),
            (3, 2, 2, 1.0),
            (10, 10, 10, 0.23579),
            (6, 2, 10, 0.55),
            (4, 2, 1, 1.0),
            (12, 3, 5, 1.0),
            (500, 300, 100, 1.0),
            (1500, 857, 187, 1.0),
            (4550, 4519, 192, 0.30484),
            (3000, 2517, 833, 0.82445),
            (10000, 9576, 8527, 0.08848),
        ],
    )
    def test_new21_game(self, n: int, k: int, max_pts: int, expected: float):
        result = run_new21_game(Solution, n, k, max_pts)
        assert_new21_game(result, expected)
