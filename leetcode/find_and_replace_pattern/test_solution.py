import pytest

from leetcode_py import logged_test

from .helpers import assert_find_and_replace_pattern, run_find_and_replace_pattern
from .solution import Solution


class TestFindAndReplacePattern:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, pattern, expected",
        [
            (["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb", ["mee", "aqq"]),
            (["a", "b", "c"], "a", ["a", "b", "c"]),
            (["aa", "bb"], "aa", ["aa", "bb"]),
            (["ab", "ba"], "ab", ["ab", "ba"]),
            (["abc", "cba"], "abc", ["abc", "cba"]),
            (["aaa", "bbb"], "aab", []),
            (["aba", "cdc"], "aba", ["aba", "cdc"]),
            (["ab", "xy", "aa"], "zz", ["aa"]),
            (["mno", "moo", "omm"], "moo", ["moo", "omm"]),
            (["abab", "abcd", "aaaa", "aabb"], "abab", ["abab"]),
            (["pep", "pip", "pop"], "pep", ["pep", "pip", "pop"]),
            (["badc", "baba", "abcd"], "baba", ["baba"]),
            (["i", "x", "q"], "j", ["i", "x", "q"]),
            (["k"], "n", ["k"]),
            (["ytv", "lvj"], "spb", ["ytv", "lvj"]),
            (["s", "a", "i", "z"], "z", ["s", "a", "i", "z"]),
            (["jcjz", "nfgo", "avnt", "heyv"], "odzy", ["nfgo", "avnt", "heyv"]),
            (["pvj", "dmi"], "mnp", ["pvj", "dmi"]),
        ],
    )
    def test_find_and_replace_pattern(self, words: list[str], pattern: str, expected: list[str]):
        result = run_find_and_replace_pattern(Solution, words, pattern)
        assert_find_and_replace_pattern(result, expected)
