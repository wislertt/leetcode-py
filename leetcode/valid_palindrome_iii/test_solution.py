import pytest

from leetcode_py import logged_test

from .helpers import assert_is_valid_palindrome, run_is_valid_palindrome
from .solution import Solution


class TestValidPalindromeIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("abcdeca", 2, True),
            ("abbababa", 1, True),
            ("a", 1, True),
            ("ab", 1, True),
            ("abc", 1, False),
            ("abc", 2, True),
            ("abcd", 2, False),
            ("abcd", 4, True),
            ("racecar", 1, True),
            ("abca", 1, True),
            ("abcb", 1, True),
            ("abab", 1, True),
            ("aabb", 1, False),
            ("aabb", 2, True),
            ("abcdba", 1, True),
            ("abcdba", 3, True),
            ("abcdcba", 1, True),
            ("aaabbb", 3, True),
            ("aaabbb", 4, True),
            ("abcba", 1, True),
            ("aaaabcaa", 2, True),
            ("accb", 2, True),
            ("bcbab", 3, True),
            ("bccccc", 1, True),
        ],
    )
    def test_is_valid_palindrome(self, s: str, k: int, expected: bool):
        result = run_is_valid_palindrome(Solution, s, k)
        assert_is_valid_palindrome(result, expected)
