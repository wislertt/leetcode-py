import pytest

from leetcode_py import logged_test

from .helpers import assert_min_days, run_min_days
from .solution import Solution


class TestMinimumNumberOfDaysToEatNOranges:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (10, 4),
            (6, 3),
            (1, 1),
            (2, 2),
            (3, 2),
            (4, 3),
            (5, 4),
            (7, 4),
            (8, 4),
            (9, 3),
            (11, 5),
            (12, 4),
            (56, 6),
            (100, 8),
            (999, 9),
            (1000000, 20),
            (2000000000, 32),
        ],
    )
    def test_min_days(self, n: int, expected: int):
        result = run_min_days(Solution, n)
        assert_min_days(result, expected)
