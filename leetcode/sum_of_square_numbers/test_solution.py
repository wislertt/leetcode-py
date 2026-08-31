import pytest

from leetcode_py import logged_test

from .helpers import assert_judge_square_sum, run_judge_square_sum
from .solution import Solution


class TestSumOfSquareNumbers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "c, expected",
        [
            (5, True),
            (3, False),
            (0, True),
            (1, True),
            (2, True),
            (4, True),
            (8, True),
            (9, True),
            (10, True),
            (18, True),
            (25, True),
            (26, True),
            (49, True),
            (50, True),
            (9999, False),
            (10000, True),
            (65536, True),
            (999999999, False),
            (1000000000, True),
            (2147483646, False),
            (2147483647, False),
        ],
    )
    def test_judge_square_sum(self, c: int, expected: bool):
        result = run_judge_square_sum(Solution, c)
        assert_judge_square_sum(result, expected)
