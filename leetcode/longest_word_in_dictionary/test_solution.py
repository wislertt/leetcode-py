import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_word, run_longest_word
from .solution import Solution


class TestLongestWordInDictionary:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["w", "wo", "wor", "worl", "world"], "world"),
            (["a", "banana", "app", "appl", "ap", "apply", "apple"], "apple"),
            (["a"], "a"),
            (["b", "br", "bre", "brea", "break", "breaks"], "breaks"),
            (["ts", "e", "t", "tea", "teas", "eat"], "ts"),
            (["yo", "ew", "fc", "zc", "zl", "peh", "tj"], ""),
            (["m", "mo", "moc", "moch", "mocha"], "mocha"),
            (["a", "ab", "abc", "abd"], "abc"),
            (["z", "zy", "zyx", "zyxw"], "zyxw"),
            (["ab", "abc"], ""),
            (["b", "br", "bre", "brea", "bread"], "bread"),
            (["c", "cd", "cdf", "cdfg", "cdfgh", "cdfghi"], "cdfghi"),
            (["a", "ab", "ba", "bab", "baba"], "ab"),
            (["d", "do", "dog", "o", "og", "ogg"], "dog"),
            (["ap", "a", "app", "appl", "apple", "apply"], "apple"),
            (["q", "qq", "qqq", "qqqq", "qqqqq"], "qqqqq"),
            (["x", "yo", "cpbt"], "x"),
            (["njjjl", "zoh", "jpx", "qzio", "f", "uo", "hyrs", "km"], "f"),
            (["nq", "jxb", "y", "dg", "ptv"], "y"),
            (["yts", "uetxd", "edob", "lid", "qbnh", "joi", "cj"], ""),
            (["je", "bc"], ""),
            (["sse", "gk", "b", "wf", "c"], "b"),
            (["zm", "nml", "g", "a", "lcgw"], "a"),
            (["u", "ytlps"], "u"),
        ],
    )
    def test_longest_word(self, words: list[str], expected: str):
        result = run_longest_word(Solution, words)
        assert_longest_word(result, expected)
