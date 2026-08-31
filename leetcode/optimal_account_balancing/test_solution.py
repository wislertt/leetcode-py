import pytest

from leetcode_py import logged_test

from .helpers import assert_min_transfers, run_min_transfers
from .solution import Solution


class TestOptimalAccountBalancing:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "transactions, expected",
        [
            ([[0, 1, 10], [2, 0, 5]], 2),
            ([[0, 1, 10], [1, 0, 1], [1, 2, 5], [2, 0, 5]], 1),
            ([[0, 1, 5]], 1),
            ([[0, 1, 1], [1, 2, 1], [2, 3, 1]], 1),
            ([[0, 1, 10], [1, 0, 10]], 0),
            ([[0, 1, 10], [2, 3, 5]], 2),
            ([[0, 1, 5], [1, 2, 5], [2, 0, 5]], 0),
            ([[1, 2, 3]], 1),
            ([[0, 1, 2], [1, 2, 1], [1, 2, 2]], 2),
            ([[0, 2, 1], [0, 2, 2], [0, 2, 4]], 1),
            ([[0, 1, 9], [2, 1, 3], [0, 2, 7]], 2),
            ([[1, 0, 5], [0, 1, 3], [2, 3, 4]], 2),
        ],
    )
    def test_min_transfers(self, transactions: list[list[int]], expected: int):
        result = run_min_transfers(Solution, transactions)
        assert_min_transfers(result, expected)
