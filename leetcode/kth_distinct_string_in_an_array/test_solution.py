import pytest

from leetcode_py import logged_test

from .helpers import assert_kth_distinct, run_kth_distinct
from .solution import Solution


class TestKthDistinctStringInAnArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, k, expected",
        [
            (["d", "b", "c", "b", "c", "a"], 2, "a"),
            (["aaa", "aa", "a"], 1, "aaa"),
            (["a", "b", "a"], 3, ""),
            (["a"], 1, "a"),
            (["a", "a"], 1, ""),
            (["a", "a"], 2, ""),
            (["abc", "def"], 2, "def"),
            (["ab", "ab", "cd"], 1, "cd"),
            (["x", "y", "x", "y", "z"], 1, "z"),
            (["e", "e", "e"], 1, ""),
            (["abcd", "efg", "h"], 3, "h"),
            (["aa", "bb", "cc", "aa"], 2, "cc"),
            (["aaaaa", "bbbbb", "aaaaa"], 1, "bbbbb"),
            (["z"], 1, "z"),
            (["a", "b", "a", "c", "d", "b", "e", "f", "g", "h", "i"], 5, "g"),
            (["m", "n", "o", "n", "m", "p", "q"], 2, "p"),
        ],
    )
    def test_kth_distinct(self, arr: list[str], k: int, expected: str):
        result = run_kth_distinct(Solution, arr, k)
        assert_kth_distinct(result, expected)
