import pytest

from leetcode_py import logged_test

from .helpers import assert_is_palindrome, run_is_palindrome
from .solution import Solution


class TestPalindromeNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "x, expected",
        [
            (121, True),
            (-121, False),
            (10, False),
            (0, True),
            (1, True),
            (11, True),
            (12, False),
            (1001, True),
            (12321, True),
            (12345, False),
            (-1, False),
            (1000021, False),
            (1234321, True),
            (2147447412, True),
            (2147483647, False),
            (100, False),
        ],
    )
    def test_is_palindrome(self, x: int, expected: bool):
        result = run_is_palindrome(Solution, x)
        assert_is_palindrome(result, expected)
