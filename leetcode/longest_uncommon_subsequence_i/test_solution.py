import pytest

from leetcode_py import logged_test

from .helpers import assert_find_luslength, run_find_luslength
from .solution import Solution


class TestLongestUncommonSubsequenceI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "a, b, expected",
        [
            ("aba", "cdc", 3),
            ("aaa", "bbb", 3),
            ("aaa", "aaa", -1),
            ("a", "a", -1),
            ("a", "b", 1),
            ("ab", "a", 2),
            ("a", "ab", 2),
            ("abc", "abc", -1),
            ("abc", "abd", 3),
            ("abcd", "abc", 4),
            ("aabb", "abab", 4),
            ("xyz", "xyzabc", 6),
            ("aa", "aa", -1),
            ("abcdef", "abc", 6),
            ("aba", "aba", -1),
            ("abcabc", "abc", 6),
            ("z", "zz", 2),
            ("abab", "baba", 4),
            ("ba", "ccca", 4),
            ("bccbbc", "abac", 6),
            ("bb", "aaacca", 6),
            ("c", "bcc", 3),
        ],
    )
    def test_find_luslength(self, a: str, b: str, expected: int):
        result = run_find_luslength(Solution, a, b)
        assert_find_luslength(result, expected)
