import pytest

from leetcode_py import logged_test

from .helpers import assert_change, run_change
from .solution import Solution


class TestCoinChangeII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "amount, coins, expected",
        [
            (5, [1, 2, 5], 4),
            (3, [2], 0),
            (10, [10], 1),
            (0, [1, 2, 5], 1),
            (4, [1, 2], 3),
            (5, [2], 0),
            (1, [2], 0),
            (3, [1, 2], 2),
            (6, [1, 2, 3], 7),
            (2, [1], 1),
            (100, [1, 2, 5], 541),
            (7, [2, 3, 6], 1),
            (8, [2, 3, 5], 3),
            (500, [3, 5, 7], 1227),
        ],
    )
    def test_change(self, amount: int, coins: list[int], expected: int):
        result = run_change(Solution, amount, coins)
        assert_change(result, expected)
