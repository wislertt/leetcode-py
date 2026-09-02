import pytest

from leetcode_py import logged_test

from .helpers import assert_split_looping_string, run_split_looping_string
from .solution import Solution


class TestSplitConcatenatedStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "strs, expected",
        [
            (["abc", "xyz"], "zyxcba"),
            (["abc"], "cba"),
            (["ab", "ba"], "bbaa"),
            (["a", "b", "c"], "cab"),
            (["aba", "bab"], "bababa"),
            (["zz", "yy", "xx"], "zzyyxx"),
            (["bc", "ab", "cb"], "ccbbab"),
            (["a", "bbb", "baa"], "bbbbaaa"),
            (["aa", "baa", "b"], "bbaaaa"),
            (["b", "aa", "b", "aab"], "bbaabaa"),
            (["bba", "ab", "baa"], "bbbabaaa"),
            (["baa", "a"], "baaa"),
            (["b", "bba", "bb", "ab"], "bbbbbaba"),
        ],
    )
    def test_split_looping_string(self, strs: list[str], expected: str):
        result = run_split_looping_string(Solution, strs)
        assert_split_looping_string(result, expected)
