import pytest

from leetcode_py import logged_test

from .helpers import assert_total_money, run_total_money
from .solution import Solution


class TestCalculateMoneyInLeetcodeBank:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (4, 10),
            (10, 37),
            (20, 96),
            (1, 1),
            (2, 3),
            (3, 6),
            (5, 15),
            (6, 21),
            (7, 28),
            (8, 30),
            (9, 33),
            (13, 55),
            (14, 63),
            (15, 66),
            (21, 105),
            (26, 135),
            (27, 144),
            (28, 154),
            (29, 159),
            (49, 343),
            (50, 351),
            (51, 360),
            (100, 1060),
            (101, 1077),
            (500, 19602),
            (999, 74778),
            (1000, 74926),
            (23, 114),
            (46, 307),
            (63, 504),
            (70, 595),
        ],
    )
    def test_total_money(self, n: int, expected: int):
        result = run_total_money(Solution, n)
        assert_total_money(result, expected)
