import pytest

from leetcode_py import logged_test

from .helpers import assert_profitable_schemes, run_profitable_schemes
from .solution import Solution


class TestProfitableSchemes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, min_profit, group, profit, expected",
        [
            (5, 3, [2, 2], [2, 3], 2),
            (10, 5, [2, 3, 5], [6, 7, 8], 7),
            (1, 1, [1], [1], 1),
            (1, 2, [1], [1], 0),
            (3, 0, [2, 2], [1, 2], 3),
            (4, 3, [2, 2], [2, 3], 2),
            (2, 1, [1, 1], [1, 1], 3),
            (3, 2, [1, 1, 1], [1, 1, 1], 4),
            (10, 10, [5, 5, 5], [4, 4, 4], 0),
            (100, 100, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 1),
            (1, 0, [1, 1, 1], [0, 0, 0], 4),
            (8, 5, [2, 3, 5, 1], [6, 7, 8, 0], 11),
            (6, 4, [1, 2, 3, 4], [3, 2, 1, 4], 6),
        ],
    )
    def test_profitable_schemes(
        self, n: int, min_profit: int, group: list[int], profit: list[int], expected: int
    ):
        result = run_profitable_schemes(Solution, n, min_profit, group, profit)
        assert_profitable_schemes(result, expected)
