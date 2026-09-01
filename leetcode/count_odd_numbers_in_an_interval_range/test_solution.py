import pytest

from leetcode_py import logged_test

from .helpers import assert_count_odds, run_count_odds
from .solution import Solution


class TestCountOddNumbersInAnIntervalRange:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "low, high, expected",
        [
            (3, 7, 3),
            (8, 10, 1),
            (0, 0, 0),
            (0, 1, 1),
            (1, 1, 1),
            (2, 2, 0),
            (1, 2, 1),
            (1, 3, 2),
            (2, 4, 1),
            (0, 10, 5),
            (5, 5, 1),
            (4, 4, 0),
            (999999999, 1000000000, 1),
            (0, 1000000000, 500000000),
            (6789, 10000, 1606),
            (123456, 789012, 332778),
            (2718281, 3141592, 211656),
            (100, 100000, 49950),
            (999998, 999999, 1),
            (0, 2, 1),
            (7, 7, 1),
            (12, 1234567, 617278),
        ],
    )
    def test_count_odds(self, low: int, high: int, expected: int):
        result = run_count_odds(Solution, low, high)
        assert_count_odds(result, expected)
