import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_palindrome_subseq, run_longest_palindrome_subseq
from .solution import Solution


class TestLongestPalindromicSubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("bbbab", 4),
            ("cbbd", 2),
            ("a", 1),
            ("ab", 1),
            ("aa", 2),
            ("aba", 3),
            ("abba", 4),
            ("abcde", 1),
            ("abcba", 5),
            ("racecar", 7),
            ("agbdba", 5),
            ("zzazz", 5),
            ("abcdefedcba", 11),
            ("aaaa", 4),
            ("abca", 3),
            ("aabcd", 2),
        ],
    )
    def test_longest_palindrome_subseq(self, s: str, expected: int):
        result = run_longest_palindrome_subseq(Solution, s)
        assert_longest_palindrome_subseq(result, expected)
