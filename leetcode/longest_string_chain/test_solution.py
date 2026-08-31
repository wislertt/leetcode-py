import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_str_chain, run_longest_str_chain
from .solution import Solution


class TestLongestStringChain:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["a", "b", "ba", "bca", "bda", "bdca"], 4),
            (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
            (["abcd", "dbqca"], 1),
            (["a"], 1),
            (["ab", "a"], 2),
            (["a", "b", "c"], 1),
            (["abc", "ab", "a"], 3),
            (["a", "ab", "abc", "abcd"], 4),
            (["abcd", "abc", "ab", "a", "dcba"], 4),
            (["xyz", "xy", "x", "yx"], 3),
            (["aa", "aaa", "aaaa", "aaaaa"], 4),
            (["q", "qq", "qqq", "ab", "abb"], 3),
        ],
    )
    def test_longest_str_chain(self, words: list[str], expected: int):
        result = run_longest_str_chain(Solution, words)
        assert_longest_str_chain(result, expected)
