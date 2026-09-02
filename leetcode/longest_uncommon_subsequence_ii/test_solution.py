import pytest

from leetcode_py import logged_test

from .helpers import assert_find_lus_length, run_find_lus_length
from .solution import Solution


class TestLongestUncommonSubsequenceII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "strs, expected",
        [
            (["aba", "cdc", "eae"], 3),
            (["aaa", "aaa", "aa"], -1),
            (["a", "b"], 1),
            (["a", "a"], -1),
            (["abc", "abd", "cdcd"], 4),
            (["abcd", "abc"], 4),
            (["abc", "abc"], -1),
            (["ab", "ba", "abc"], 3),
            (["aabbcc", "aabbcc"], -1),
            (["aa", "aaa", "aaaa"], 4),
            (["xyz", "abc"], 3),
            (["m", "m", "m"], -1),
            (["abcde", "abcd", "abc"], 5),
            (["ab", "cd", "abcd"], 4),
            (["abc", "abc", "abd"], 3),
            (["bc", "a"], 2),
            (["ca", "c", "cccb", "abc"], 4),
            (["b", "acbb"], 4),
        ],
    )
    def test_find_lus_length(self, strs: list[str], expected: int):
        result = run_find_lus_length(Solution, strs)
        assert_find_lus_length(result, expected)
