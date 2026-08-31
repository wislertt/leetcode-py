import pytest

from leetcode_py import logged_test

from .helpers import assert_is_perfect_square, run_is_perfect_square
from .solution import Solution


class TestValidPerfectSquare:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            (16, True),
            (14, False),
            (1, True),
            (2, False),
            (3, False),
            (4, True),
            (5, False),
            (8, False),
            (9, True),
            (24, False),
            (25, True),
            (80, False),
            (81, True),
            (10000, True),
            (9999, False),
            (2147395600, True),
            (2147483646, False),
            (2147483647, False),
            (2147395601, False),
            (49, True),
            (50, False),
        ],
    )
    def test_is_perfect_square(self, num: int, expected: bool):
        result = run_is_perfect_square(Solution, num)
        assert_is_perfect_square(result, expected)
