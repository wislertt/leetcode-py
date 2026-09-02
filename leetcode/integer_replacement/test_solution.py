import pytest

from leetcode_py import logged_test

from .helpers import assert_integer_replacement, run_integer_replacement
from .solution import Solution


class TestIntegerReplacement:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 0),
            (2, 1),
            (3, 2),
            (4, 2),
            (5, 3),
            (6, 3),
            (7, 4),
            (8, 3),
            (9, 4),
            (10, 4),
            (11, 5),
            (15, 5),
            (16, 4),
            (17, 5),
            (31, 6),
            (63, 7),
            (1023, 11),
            (65535, 17),
            (1073741824, 30),
            (2147483647, 32),
            (2147483646, 32),
            (123456789, 37),
        ],
    )
    def test_integer_replacement(self, n: int, expected: int):
        result = run_integer_replacement(Solution, n)
        assert_integer_replacement(result, expected)
