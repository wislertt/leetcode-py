import pytest

from leetcode_py import logged_test

from .helpers import assert_first_palindrome, run_first_palindrome
from .solution import Solution


class TestFindFirstPalindromicStringInTheArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["abc", "car", "ada", "racecar", "cool"], "ada"),
            (["notapalindrome", "racecar"], "racecar"),
            (["def", "ghi"], ""),
            (["a"], "a"),
            (["ab", "ba"], ""),
            (["aa", "ab"], "aa"),
            (["x"], "x"),
            (["abc", "aba", "xyz"], "aba"),
            (["racecar"], "racecar"),
            (["ab"], ""),
            (["abc", "def", "ada"], "ada"),
            (["noon", "level", "word"], "noon"),
            (["abcba"], "abcba"),
            (["abccba"], "abccba"),
            (["zz"], "zz"),
            (["abc", "cb", "dd"], "dd"),
            (["abba", "xy"], "abba"),
            (["abc", "abcd", "abcde"], ""),
            (["q", "qq", "qqq"], "q"),
            (["zxyx", "abcba", "hello"], "abcba"),
        ],
    )
    def test_first_palindrome(self, words: list[str], expected: str):
        result = run_first_palindrome(Solution, words)
        assert_first_palindrome(result, expected)
