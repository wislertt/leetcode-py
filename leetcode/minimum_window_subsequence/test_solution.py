import pytest

from leetcode_py import logged_test

from .helpers import assert_min_window, run_min_window
from .solution import Solution


class TestMinimumWindowSubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s1, s2, expected",
        [
            ("abcdebdde", "bde", "bcde"),
            ("jmeqksfrsdcmsiwvaovztaqenprpvnbstl", "u", ""),
            ("a", "a", "a"),
            ("a", "b", ""),
            ("ab", "b", "b"),
            ("abc", "ac", "abc"),
            ("abc", "cb", ""),
            ("ab", "abc", ""),
            ("aa", "aa", "aa"),
            ("abcbc", "bc", "bc"),
            ("axbxcx", "abc", "axbxc"),
            ("babb", "ab", "ab"),
            ("abacbc", "abc", "abac"),
            ("zzzz", "z", "z"),
            ("abab", "ba", "ba"),
            ("xcyzstuv", "xyz", "xcyz"),
            ("abcde", "abcde", "abcde"),
            ("abcabc", "cba", ""),
            ("abcbcb", "bb", "bcb"),
            ("pqpqrpq", "pqr", "pqr"),
        ],
    )
    def test_min_window(self, s1: str, s2: str, expected: str):
        result = run_min_window(Solution, s1, s2)
        assert_min_window(result, expected)
