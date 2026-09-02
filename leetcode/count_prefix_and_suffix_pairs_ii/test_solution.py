import pytest

from leetcode_py import logged_test

from .helpers import assert_count_prefix_and_suffix_pairs, run_count_prefix_and_suffix_pairs
from .solution import Solution


class TestCountPrefixAndSuffixPairsII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["a", "aba", "ababa", "aa"], 4),
            (["pa", "papa", "ma", "mama"], 2),
            (["abab", "ab"], 0),
            (["abc"], 0),
            (["aa", "aa", "aa"], 3),
            (["ab", "ab"], 1),
            (["ab", "ba"], 0),
            (["a", "b", "a", "b"], 2),
            (["aba", "a", "aba"], 2),
            (["abcd", "cd", "ab", "abcd"], 1),
            (["abcba", "a", "aba", "abcba"], 3),
            (["zz", "z", "zzz", "z"], 3),
            (["ab", "baa", "a", "aabbb"], 0),
            (["ba", "a", "a", "bb"], 1),
            (["bbab", "ba", "b"], 0),
            (["aba", "abaaa", "bab"], 0),
            (["ab", "abaab", "ababa", "abba", "bbbb", "bbbba"], 1),
            (["b", "bab", "ab", "bab", "bbb", "bbb"], 6),
        ],
    )
    def test_count_prefix_and_suffix_pairs(self, words: list[str], expected: int):
        result = run_count_prefix_and_suffix_pairs(Solution, words)
        assert_count_prefix_and_suffix_pairs(result, expected)
