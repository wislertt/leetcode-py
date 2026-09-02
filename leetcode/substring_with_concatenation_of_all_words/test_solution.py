import pytest

from leetcode_py import logged_test

from .helpers import assert_find_substring, run_find_substring
from .solution import Solution


class TestSubstringWithConcatenationOfAllWords:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, words, expected",
        [
            ("barfoothefoobarman", ["foo", "bar"], [0, 9]),
            ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
            ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
            ("a", ["a"], [0]),
            ("ab", ["ab"], [0]),
            ("abc", ["abd"], []),
            ("aaa", ["aaaa"], []),
            ("aaa", ["a", "b"], []),
            ("aaaa", ["aa"], [0, 1, 2]),
            ("aaa", ["a", "a"], [0, 1]),
            ("abababab", ["ab", "ba"], []),
            ("wordgoodgoodgoodbestword", ["word", "good"], [0]),
            ("aaaaaaaaaa", ["aa", "aa", "aa"], [0, 1, 2, 3, 4]),
            ("mississippi", ["mis", "sis"], [0]),
            ("bcabbcaabb", ["ab", "bc"], [0, 2]),
            ("foobarfoobar", ["foo", "bar"], [0, 3, 6]),
            ("aabbaabb", ["ab", "ba", "aa"], []),
            ("goodgoodbestword", ["good", "good", "best"], [0]),
        ],
    )
    def test_find_substring(self, s: str, words: list[str], expected: list[int]):
        result = run_find_substring(Solution, s, words)
        assert_find_substring(result, expected)
