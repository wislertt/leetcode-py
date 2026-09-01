import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_ideal_string, run_longest_ideal_string
from .solution import Solution


class TestLongestIdealSubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("acfgbd", 2, 4),
            ("abcd", 3, 4),
            ("a", 0, 1),
            ("a", 25, 1),
            ("abc", 0, 1),
            ("aaa", 0, 3),
            ("ab", 0, 1),
            ("ab", 1, 2),
            ("az", 25, 2),
            ("az", 24, 1),
            ("babcd", 1, 5),
            ("acfgbd", 0, 1),
            ("zyxwvu", 2, 6),
            ("zyxwvu", 25, 6),
            ("abcdcba", 2, 7),
            ("eaahoheh", 23, 8),
            ("jjtfoslruajtu", 7, 9),
            ("xxlzdjriwkigni", 6, 7),
            ("atlrxrfvcwbsxd", 15, 9),
            ("pyqqgcquzzlhtb", 6, 8),
            ("qundowfcenl", 7, 6),
            ("giqa", 14, 3),
            ("myfzvkulfw", 22, 10),
            ("bacn", 12, 4),
            ("dstqwqeclgopwp", 5, 8),
            ("vfsmudpwmvllg", 21, 13),
            ("yhnkezxltz", 14, 7),
        ],
    )
    def test_longest_ideal_string(self, s: str, k: int, expected: int):
        result = run_longest_ideal_string(Solution, s, k)
        assert_longest_ideal_string(result, expected)
