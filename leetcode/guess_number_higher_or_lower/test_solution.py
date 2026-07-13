import pytest

from leetcode_py import logged_test

from .helpers import assert_guess_number, run_guess_number
from .solution import Solution


class TestGuessNumberHigherOrLower:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, pick, expected",
        [
            (10, 6, 6),
            (1, 1, 1),
            (2, 1, 1),
            (10, 1, 1),
            (10, 10, 10),
            (100, 50, 50),
            (1000, 1, 1),
            (1000, 1000, 1000),
            (5, 3, 3),
            (2, 2, 2),
            (2126753390, 1702766719, 1702766719),
            (100000, 99999, 99999),
            (100000, 1, 1),
            (3, 2, 2),
            (100, 99, 99),
        ],
    )
    def test_guess_number(self, n: int, pick: int, expected: int):
        result = run_guess_number(Solution, n, pick)
        assert_guess_number(result, expected)
