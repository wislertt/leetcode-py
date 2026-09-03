import pytest

from leetcode_py import logged_test

from .helpers import assert_broken_calc, run_broken_calc
from .solution import Solution


class TestBrokenCalculator:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "start_value, target, expected",
        [
            (2, 3, 2),
            (5, 8, 2),
            (3, 10, 3),
            (1, 1, 0),
            (2, 2, 0),
            (10, 10, 0),
            (2, 1, 1),
            (1000000000, 1, 999999999),
            (1, 2, 1),
            (1, 3, 3),
            (1, 4, 2),
            (3, 2, 1),
            (7, 21, 5),
            (4, 13, 4),
            (6, 25, 8),
            (1, 1000000000, 39),
            (1000000000, 999999999, 1),
            (5, 1, 4),
            (8, 5, 3),
            (12, 4, 8),
        ],
    )
    def test_broken_calc(self, start_value: int, target: int, expected: int):
        result = run_broken_calc(Solution, start_value, target)
        assert_broken_calc(result, expected)
