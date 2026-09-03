import pytest

from leetcode_py import logged_test

from .helpers import assert_word_filter, run_word_filter
from .solution import WordFilter


class TestPrefixAndSuffixSearch:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (["WordFilter", "f"], [[["apple"]], ["a", "e"]], [None, 0]),
            (["WordFilter", "f"], [[["apple"]], ["a", "l"]], [None, -1]),
            (["WordFilter", "f"], [[["apple"]], ["p", "e"]], [None, -1]),
            (["WordFilter", "f"], [[["apple"]], ["apple", "apple"]], [None, 0]),
            (["WordFilter", "f"], [[["apple"]], ["appl", "ple"]], [None, 0]),
            (["WordFilter", "f"], [[["apple"]], ["apples", "e"]], [None, -1]),
            (["WordFilter", "f"], [[["apple"]], ["a", "lephant"]], [None, -1]),
            (
                ["WordFilter", "f", "f", "f"],
                [[["ab", "ab", "ab"]], ["a", "b"], ["a", "b"], ["b", "a"]],
                [None, 2, 2, -1],
            ),
            (
                ["WordFilter", "f", "f", "f"],
                [[["a", "b"]], ["a", "a"], ["b", "a"], ["a", "b"]],
                [None, 0, -1, -1],
            ),
            (
                ["WordFilter", "f", "f", "f"],
                [[["c", "c", "b", "c"]], ["c", "c"], ["c", "b"], ["b", "b"]],
                [None, 3, -1, 2],
            ),
            (
                ["WordFilter", "f", "f", "f"],
                [[["abc", "axc", "abcx"]], ["a", "c"], ["a", "x"], ["abc", "cx"]],
                [None, 1, 2, 2],
            ),
            (
                ["WordFilter", "f", "f", "f"],
                [[["abb", "bab", "bba", "ab"]], ["a", "b"], ["b", "b"], ["b", "a"]],
                [None, 3, 1, 2],
            ),
            (
                ["WordFilter", "f", "f", "f"],
                [[["bab", "aba"]], ["b", "ab"], ["ab", "ba"], ["aba", "aba"]],
                [None, 0, 1, 1],
            ),
            (
                ["WordFilter", "f", "f", "f"],
                [[["bab", "aab", "b", "a", "ab", "aba"]], ["a", "a"], ["aab", "ab"], ["bab", "b"]],
                [None, 5, 1, 0],
            ),
            (["WordFilter", "f"], [[["ba"]], ["ba", "ba"]], [None, 0]),
            (
                ["WordFilter", "f", "f"],
                [[["aba", "aa", "baa"]], ["aba", "aba"], ["ba", "aa"]],
                [None, 0, 2],
            ),
        ],
    )
    def test_word_filter(
        self, operations: list[str], inputs: list[list[str]], expected: list[int | None]
    ):
        result, _ = run_word_filter(WordFilter, operations, inputs)
        assert_word_filter(result, expected)
