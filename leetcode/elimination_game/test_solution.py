import pytest

from leetcode_py import logged_test

from .helpers import assert_last_remaining, run_last_remaining
from .solution import Solution


class TestEliminationGame:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 2),
            (3, 2),
            (4, 2),
            (5, 2),
            (6, 4),
            (7, 4),
            (8, 6),
            (9, 6),
            (10, 8),
            (11, 8),
            (12, 6),
            (13, 6),
            (14, 8),
            (15, 8),
            (16, 6),
            (17, 6),
            (18, 8),
            (19, 8),
            (20, 6),
            (21, 6),
            (22, 8),
            (23, 8),
            (24, 14),
            (30, 16),
            (50, 24),
            (100, 54),
            (500, 246),
            (1000, 510),
            (1234, 472),
            (5000, 2014),
            (100000, 55286),
            (1000000, 481110),
            (1000000000, 534765398),
        ],
    )
    def test_last_remaining(self, n: int, expected: int):
        result = run_last_remaining(Solution, n)
        assert_last_remaining(result, expected)
