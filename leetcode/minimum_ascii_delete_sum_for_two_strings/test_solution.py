import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_delete_sum, run_minimum_delete_sum
from .solution import Solution


class TestMinimumAsciiDeleteSumForTwoStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s1, s2, expected",
        [
            ("a", "a", 0),
            ("a", "b", 195),
            ("ab", "ab", 0),
            ("ab", "ba", 194),
            ("abc", "abc", 0),
            ("abc", "def", 597),
            ("abcde", "ace", 198),
            ("leetcode", "etco", 410),
            ("intention", "execution", 878),
            ("xy", "x", 121),
            ("aa", "aaa", 97),
            ("z", "zzzz", 366),
            ("eddad", "acdc", 499),
            ("abcd", "d", 294),
            ("c", "deec", 302),
            ("aabb", "da", 393),
            ("bddccca", "dedecc", 496),
            ("ccdd", "abbab", 886),
            ("aabcedcb", "a", 692),
            ("ddddcc", "bdb", 694),
        ],
    )
    def test_minimum_delete_sum(self, s1: str, s2: str, expected: int):
        result = run_minimum_delete_sum(Solution, s1, s2)
        assert_minimum_delete_sum(result, expected)
