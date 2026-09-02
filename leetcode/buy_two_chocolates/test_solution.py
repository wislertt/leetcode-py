import pytest

from leetcode_py import logged_test

from .helpers import assert_buy_choco, run_buy_choco
from .solution import Solution


class TestBuyTwoChocolates:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "prices, money, expected",
        [
            ([1, 2, 2], 3, 0),
            ([3, 2, 3], 3, 3),
            ([1, 2, 2], 100, 97),
            ([98, 99, 100], 100, 100),
            ([98, 99, 100], 1, 1),
            ([50, 50], 100, 0),
            ([50, 50], 99, 99),
            ([1, 1, 1], 1, 1),
            ([100, 100], 100, 100),
            ([100, 100], 99, 99),
            ([7, 3, 5, 9], 10, 2),
            ([2, 9, 4, 8], 12, 6),
            ([1, 100], 100, 100),
            ([1, 100], 50, 50),
            ([13, 17, 11, 11, 20], 25, 3),
            ([5, 6, 7, 8, 9], 3, 3),
            ([48, 9, 82], 92, 35),
            ([86, 12], 22, 22),
            ([30, 92], 67, 67),
            ([92, 69, 89], 45, 45),
        ],
    )
    def test_buy_choco(self, prices: list[int], money: int, expected: int):
        result = run_buy_choco(Solution, prices, money)
        assert_buy_choco(result, expected)
