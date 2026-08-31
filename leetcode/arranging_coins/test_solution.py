import pytest

from leetcode_py import logged_test

from .helpers import assert_arrange_coins, run_arrange_coins
from .solution import Solution


class TestArrangingCoins:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (5, 2),
            (8, 3),
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 2),
            (6, 3),
            (7, 3),
            (9, 3),
            (10, 4),
            (15, 5),
            (20, 5),
            (21, 6),
            (22, 6),
            (54, 9),
            (55, 10),
            (100, 13),
            (1804289384, 60070),
            (2147483647, 65535),
        ],
    )
    def test_arrange_coins(self, n: int, expected: int):
        result = run_arrange_coins(Solution, n)
        assert_arrange_coins(result, expected)
