import pytest

from leetcode_py import logged_test

from .helpers import assert_count_prefix_suffix_pairs, run_count_prefix_suffix_pairs
from .solution import Solution


class TestCountPrefixAndSuffixPairsI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["a", "aba", "ababa", "aa"], 4),
            (["pa", "papa", "ma", "mama"], 2),
            (["abab", "ab"], 0),
            (["a"], 0),
            (["a", "a"], 1),
            (["abc", "abc", "abc"], 3),
            (["ab", "ba"], 0),
            (["aba", "ababa", "aba"], 2),
            (["a", "b", "c", "d"], 0),
            (["aa", "a", "aaa"], 2),
            (["abc", "abcd", "abcde"], 0),
            (["zz", "azz", "aza"], 0),
            (["bb", "baba", "aabb", "b"], 0),
            (["baab", "aba", "a"], 0),
            (["bbaa", "bbaa", "a", "b"], 1),
            (["bb", "bb", "b", "a", "bbab"], 2),
        ],
    )
    def test_count_prefix_suffix_pairs(self, words: list[str], expected: int):
        result = run_count_prefix_suffix_pairs(Solution, words)
        assert_count_prefix_suffix_pairs(result, expected)
