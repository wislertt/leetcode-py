import pytest

from leetcode_py import logged_test

from .helpers import assert_max_transactions, run_max_transactions
from .solution import Solution


class TestMaximumTransactionsWithoutNegativeBalance:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "transactions, expected",
        [
            ([2, -5, 3, -1, -2], 4),
            ([-1, -2, -3], 0),
            ([3, -2, 3, -2, 1, -1], 6),
            ([5], 1),
            ([-7], 0),
            ([0], 1),
            ([1, -1, 1, -1], 4),
            ([-1, 1], 1),
            ([2, -3, 4], 2),
            ([10, -20, 30], 2),
            ([1, 2, 3], 3),
            ([-5, 5, -5, 5], 3),
            ([0, -1, 0], 2),
            ([4, -10, -3, 6, 1], 4),
            ([1, -2, 3, -4, 5, -6, 7], 5),
            ([1000000000, -1000000000, 1000000000], 3),
        ],
    )
    def test_max_transactions(self, transactions: list[int], expected: int):
        result = run_max_transactions(Solution, transactions)
        assert_max_transactions(result, expected)
