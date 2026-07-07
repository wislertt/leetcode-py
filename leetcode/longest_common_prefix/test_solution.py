import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_common_prefix, run_longest_common_prefix
from .solution import Solution


class TestLongestCommonPrefix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "strs, expected",
        [
            (["flower", "flow", "flight"], "fl"),
            (["dog", "racecar", "car"], ""),
            ([""], ""),
            (["a"], "a"),
            (["ab", "a"], "a"),
            (["aaa", "aa", "aaa"], "aa"),
            (["abc", "abc", "abc"], "abc"),
            (["abc", "def", "ghi"], ""),
            (["interspecies", "interstellar", "interstate"], "inters"),
            (["", ""], ""),
            (["ab", "ab", "ab"], "ab"),
            (["a", "a", "a"], "a"),
            (["prefix", "pre", "pref"], "pre"),
            (["xyz", "xyz", "x"], "x"),
            (["abca", "abcab", "abcabc"], "abca"),
            (["cir", "car"], "c"),
        ],
    )
    def test_longest_common_prefix(self, strs: list[str], expected: str):
        result = run_longest_common_prefix(Solution, strs)
        assert_longest_common_prefix(result, expected)
