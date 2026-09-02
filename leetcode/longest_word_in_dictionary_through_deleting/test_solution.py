import pytest

from leetcode_py import logged_test

from .helpers import assert_find_longest_word, run_find_longest_word
from .solution import Solution


class TestLongestWordInDictionaryThroughDeleting:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, dictionary, expected",
        [
            ("abpcplea", ["ale", "apple", "monkey", "plea"], "apple"),
            ("abpcplea", ["a", "b", "c"], "a"),
            ("abpcplea", ["ale", "apple", "monkey", "plea", "abpcpl"], "abpcpl"),
            ("abpcplea", ["z", "zz", "zzz"], ""),
            ("a", ["a"], "a"),
            ("a", ["b"], ""),
            ("a", ["a", "b", "ab"], "a"),
            ("bab", ["ba", "ab", "a", "b"], "ab"),
            ("abce", ["abe", "abc", "ac"], "abc"),
            ("abpcplea", ["apple", "plea", "ale", "pcplea"], "pcplea"),
            ("aaa", ["aaa", "aa", "a", "aaaa"], "aaa"),
            ("abcd", ["dcba", "bcda", "cdab"], ""),
            ("abcde", ["ace", "bcd", "abde", "abcde"], "abcde"),
            ("xyz", ["xyz", "xy", "yz", "xz"], "xyz"),
            ("abpcplea", ["apcplea", "bpcplea", "pcplea"], "apcplea"),
            ("bdcba", ["ba", "bc", "bb", "bdcba"], "bdcba"),
            ("abacaba", ["abacaba", "aaaa", "bbb", "abc"], "abacaba"),
            ("abcabc", ["cc", "aa", "bb", "abcabc"], "abcabc"),
        ],
    )
    def test_find_longest_word(self, s: str, dictionary: list[str], expected: str):
        result = run_find_longest_word(Solution, s, dictionary)
        assert_find_longest_word(result, expected)
