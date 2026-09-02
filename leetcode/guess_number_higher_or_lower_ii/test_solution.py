import pytest

from leetcode_py import logged_test

from .helpers import assert_get_money_amount, run_get_money_amount
from .solution import Solution


class TestGuessNumberHigherOrLowerIi:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 0),
            (2, 1),
            (3, 2),
            (4, 4),
            (5, 6),
            (6, 8),
            (7, 10),
            (8, 12),
            (9, 14),
            (10, 16),
            (11, 18),
            (12, 21),
            (13, 24),
            (14, 27),
            (15, 30),
            (16, 34),
            (17, 38),
            (18, 42),
            (19, 46),
            (20, 49),
            (25, 64),
            (30, 79),
            (40, 119),
            (50, 172),
            (75, 274),
            (100, 400),
            (150, 692),
            (200, 952),
        ],
    )
    def test_get_money_amount(self, n: int, expected: int):
        result = run_get_money_amount(Solution, n)
        assert_get_money_amount(result, expected)
