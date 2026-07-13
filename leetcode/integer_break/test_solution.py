import pytest

from leetcode_py import logged_test

from .helpers import assert_integer_break, run_integer_break
from .solution import Solution


class TestIntegerBreak:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (2, 1),
            (3, 2),
            (4, 4),
            (5, 6),
            (6, 9),
            (7, 12),
            (8, 18),
            (9, 27),
            (10, 36),
            (11, 54),
            (12, 81),
            (13, 108),
            (14, 162),
            (15, 243),
            (58, 1549681956),
        ],
    )
    def test_integer_break(self, n: int, expected: int):
        result = run_integer_break(Solution, n)
        assert_integer_break(result, expected)
