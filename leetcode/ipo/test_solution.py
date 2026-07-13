import pytest

from leetcode_py import logged_test

from .helpers import assert_find_maximized_capital, run_find_maximized_capital
from .solution import Solution


class TestIPO:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "k, w, profits, capital, expected",
        [
            (2, 0, [1, 2, 3], [0, 1, 1], 4),
            (3, 0, [1, 2, 3], [0, 1, 2], 6),
            (1, 0, [1, 2, 3], [0, 1, 1], 1),
            (2, 2, [1, 2, 3], [0, 1, 1], 7),
            (3, 10, [1, 2, 3], [1, 2, 3], 16),
            (1, 5, [10, 20], [10, 1], 25),
            (2, 0, [1, 2, 3], [5, 5, 5], 0),
            (2, 0, [3, 2, 1], [0, 0, 0], 5),
            (10, 0, [1], [0], 1),
            (2, 3, [5, 5, 5], [1, 2, 3], 13),
            (2, 1, [1, 2, 3, 4], [2, 2, 2, 2], 1),
            (3, 0, [1, 2, 3, 4, 5], [0, 1, 2, 3, 4], 7),
            (2, 0, [2, 1, 3], [0, 0, 0], 5),
            (3, 0, [1, 1, 1, 1], [0, 0, 0, 0], 3),
            (1, 0, [5], [0], 5),
        ],
    )
    def test_find_maximized_capital(
        self, k: int, w: int, profits: list[int], capital: list[int], expected: int
    ):
        result = run_find_maximized_capital(Solution, k, w, profits, capital)
        assert_find_maximized_capital(result, expected)
