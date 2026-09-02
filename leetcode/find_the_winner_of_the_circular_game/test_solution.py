import pytest

from leetcode_py import logged_test

from .helpers import assert_find_the_winner, run_find_the_winner
from .solution import Solution


class TestFindTheWinnerOfTheCircularGame:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, expected",
        [
            (5, 2, 3),
            (6, 5, 1),
            (1, 1, 1),
            (2, 1, 2),
            (2, 2, 1),
            (3, 1, 3),
            (3, 2, 3),
            (3, 3, 2),
            (4, 2, 1),
            (4, 4, 2),
            (5, 3, 4),
            (7, 3, 4),
            (8, 6, 1),
            (10, 4, 5),
            (12, 6, 3),
            (100, 7, 50),
            (499, 250, 134),
            (500, 1, 500),
            (500, 500, 69),
            (9, 6, 7),
        ],
    )
    def test_find_the_winner(self, n: int, k: int, expected: int):
        result = run_find_the_winner(Solution, n, k)
        assert_find_the_winner(result, expected)
