import pytest

from leetcode_py import logged_test

from .helpers import assert_max_len, run_max_len
from .solution import Solution


class TestMaximumLengthOfAConcatenatedStringWithUniqueCharactersTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            (["un", "iq", "ue"], 4),
            (["cha", "r", "act", "ers"], 6),
            (["abcdefghijklmnopqrstuvwxyz"], 26),
            (["a", "b", "c", "d"], 4),
            (["aa", "bb"], 0),
            (["ab", "cd", "cde", "cdef", "efg", "fgh", "abxyz"], 11),
            (["ab", "ba"], 2),
            (["abcdefghijklmnopqrstuvwxyz", "a", "b"], 26),
            (["ab", "ab"], 2),
            (["yxa", "svub", "aejlfdcykm"], 14),
            (["jxg", "hc", "qziwnpthloyfke"], 17),
            (["wkkeww", "kjdedwk", "eedeccde"], 0),
            (["abcdefghijklm", "nopqrstuvwxyz"], 26),
            (["a", "abc", "d", "de", "fg"], 7),
            (["z"], 1),
            (["opt", "yp", "zumhavpi", "icey", "k", "qnrtuxpqebo"], 9),
        ],
    )
    def test_max_len(self, arr: list[str], expected: int):
        result = run_max_len(Solution, arr)
        assert_max_len(result, expected)
