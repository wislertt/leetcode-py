import pytest

from leetcode_py import logged_test

from .helpers import assert_string_matching, run_string_matching
from .solution import Solution


class TestStringMatchingInAnArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["mass", "as", "hero", "superhero"], ["as", "hero"]),
            (["leetcode", "et", "code"], ["code", "et"]),
            (["blue", "green", "bu"], []),
            (["a", "ab", "abc"], ["a", "ab"]),
            (["abc", "bcd", "cde"], []),
            (["u", "ux", "uxn", "uxnz"], ["u", "ux", "uxn"]),
            (["super", "sup", "s", "upe"], ["s", "sup", "upe"]),
            (["xy", "yx", "xyz"], ["xy"]),
            (["cat", "dog", "bird"], []),
            (["aaa"], []),
            (["z"], []),
            (["abcdef", "bcdef", "cdef", "def", "ef"], ["bcdef", "cdef", "def", "ef"]),
            (["hello", "hell", "hel", "he", "h"], ["h", "he", "hel", "hell"]),
            (["one", "two", "three"], []),
            (["aac", "c", "cb", "ac"], ["ac", "c"]),
            (["c", "ace", "d", "cb", "e", "ec"], ["c", "e"]),
            (["dc", "c", "edc", "d", "b", "adea"], ["c", "d", "dc"]),
            (["dcb", "ebca"], []),
            (["bc", "ede", "c", "ee", "bbde", "dad"], ["c"]),
            (["d"], []),
            (["cc", "d", "b", "cd", "a"], ["d"]),
            (["bae", "dda", "cddb", "addb", "cbaa", "aa"], ["aa"]),
        ],
    )
    def test_string_matching(self, words: list[str], expected: list[str]):
        result = run_string_matching(Solution, words)
        assert_string_matching(result, expected)
