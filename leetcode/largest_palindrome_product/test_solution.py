import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_palindrome, run_largest_palindrome
from .solution import Solution


class TestLargestPalindromeProduct:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 9),
            (2, 987),
            (3, 123),
            (4, 597),
            (5, 677),
            (6, 1218),
            (7, 877),
            (8, 475),
            (1, 9),
            (2, 987),
            (4, 597),
            (8, 475),
        ],
    )
    def test_largest_palindrome(self, n: int, expected: int):
        result = run_largest_palindrome(Solution, n)
        assert_largest_palindrome(result, expected)
