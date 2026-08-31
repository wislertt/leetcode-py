import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_palindrome, run_shortest_palindrome
from .solution import Solution


class TestShortestPalindrome:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aacecaaa", "aaacecaaa"),
            ("abcd", "dcbabcd"),
            ("", ""),
            ("a", "a"),
            ("aa", "aa"),
            ("ab", "bab"),
            ("aba", "aba"),
            ("abc", "cbabc"),
            ("aabba", "abbaabba"),
            ("race", "ecarace"),
            ("aaa", "aaa"),
            ("abab", "babab"),
            ("abcdcba", "abcdcba"),
            ("aabbaabb", "bbaabbaabb"),
            ("abcda", "adcbabcda"),
            ("abcb", "bcbabcb"),
        ],
    )
    def test_shortest_palindrome(self, s: str, expected: str):
        result = run_shortest_palindrome(Solution, s)
        assert_shortest_palindrome(result, expected)
