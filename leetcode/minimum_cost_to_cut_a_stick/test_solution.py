import pytest

from leetcode_py import logged_test

from .helpers import assert_min_cost, run_min_cost
from .solution import Solution


class TestMinimumCostToCutAStick:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, cuts, expected",
        [
            (7, [1, 3, 4, 5], 16),
            (9, [5, 6, 1, 4, 2], 22),
            (7, [3, 5, 1, 4], 16),
            (9, [4, 6, 5, 2, 1], 22),
            (4, [1, 3], 7),
            (5, [1, 3, 4], 10),
            (6, [1, 5], 11),
            (10, [2, 4, 6, 8], 24),
            (3, [1], 3),
            (3, [2], 3),
            (1000000, [500000], 1000000),
            (100, [50], 100),
            (1000000, [1, 999999], 1999999),
            (30, [5, 10, 15, 20, 25], 80),
            (7, [5, 3, 1, 4], 16),
            (50, [49, 1, 25, 12], 112),
            (29, [12], 29),
            (16, [4, 1], 20),
            (15, [5, 11, 4, 3], 32),
            (22, [6, 18, 19, 7, 11], 53),
            (21, [1, 8, 6, 4], 37),
            (18, [1, 14, 8, 15], 40),
            (14, [8, 3, 12, 11, 5], 36),
            (24, [2, 17], 41),
        ],
    )
    def test_min_cost(self, n: int, cuts: list[int], expected: int):
        result = run_min_cost(Solution, n, cuts)
        assert_min_cost(result, expected)
