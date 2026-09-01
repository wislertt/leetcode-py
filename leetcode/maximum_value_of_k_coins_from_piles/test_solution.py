import pytest

from leetcode_py import logged_test

from .helpers import assert_max_value_of_coins, run_max_value_of_coins
from .solution import Solution


class TestMaximumValueOfKCoinsFromPiles:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "piles, k, expected",
        [
            ([[1, 100, 3], [7, 8, 9]], 2, 101),
            ([[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 7, 706),
            ([[1, 2, 3]], 1, 1),
            ([[1, 2, 3]], 2, 3),
            ([[1, 2, 3]], 3, 6),
            ([[10]], 1, 10),
            ([[5], [6]], 1, 6),
            ([[5], [6]], 2, 11),
            ([[1, 1], [1, 1]], 2, 2),
            ([[1, 1], [1, 1]], 3, 3),
            ([[1, 1], [1, 1]], 4, 4),
            ([[2, 1000, 2], [1000, 2]], 3, 2002),
            ([[7]], 1, 7),
            ([[1], [2], [3], [4]], 4, 10),
            ([[3, 1], [2, 5], [4, 2]], 3, 11),
            ([[9, 9, 9, 9]], 4, 36),
            ([[18, 17, 12]], 2, 35),
            ([[17, 6], [12, 2, 17, 2]], 2, 29),
            ([[4, 14, 16, 14], [4, 13, 15, 12]], 1, 4),
            ([[16, 3, 6]], 1, 16),
            ([[8, 4, 5], [10], [8], [12, 11, 9, 16]], 8, 78),
            ([[18]], 1, 18),
            ([[11]], 1, 11),
            ([[20, 17, 7, 1], [3]], 3, 44),
        ],
    )
    def test_max_value_of_coins(self, piles: list[list[int]], k: int, expected: int):
        result = run_max_value_of_coins(Solution, piles, k)
        assert_max_value_of_coins(result, expected)
