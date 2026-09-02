import pytest

from leetcode_py import logged_test

from .helpers import assert_add_digits, run_add_digits
from .solution import Solution


class TestAddDigits:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            (38, 2),
            (0, 0),
            (9, 9),
            (10, 1),
            (18, 9),
            (19, 1),
            (99, 9),
            (100, 1),
            (1234, 1),
            (99999, 9),
            (2147483647, 1),
            (2147483646, 9),
            (1, 1),
            (2, 2),
            (123456789, 9),
            (2024, 8),
            (88888, 4),
        ],
    )
    def test_add_digits(self, num: int, expected: int):
        result = run_add_digits(Solution, num)
        assert_add_digits(result, expected)
