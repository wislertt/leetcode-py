import pytest

from leetcode_py import logged_test

from .helpers import assert_count_palindromic_subsequence, run_count_palindromic_subsequence
from .solution import Solution


class TestUniqueLength3PalindromicSubsequences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aabca", 3),
            ("adc", 0),
            ("bbcbaba", 4),
            ("aba", 1),
            ("aaa", 1),
            ("abc", 0),
            ("abcba", 3),
            ("abccba", 3),
            ("aaaaa", 1),
            ("aabb", 0),
            ("ababa", 3),
            ("racecar", 6),
            ("abab", 2),
            ("xyzzyx", 3),
            ("zzz", 1),
            ("aazzaa", 2),
            ("abaa", 2),
            ("babb", 2),
            ("bbabb", 2),
            ("bbbaa", 1),
            ("bbaaaa", 1),
            ("ccccab", 1),
            ("aabacabb", 6),
            ("bccbcccb", 4),
            ("baaaabaaba", 4),
            ("abbabbbbbb", 3),
            ("qreobrjrskrk", 8),
            ("plxsgxjepzuq", 8),
            ("elokasjkoljejr", 23),
            ("zmftczwnbqotdx", 11),
            ("babcabbcbbcabcca", 9),
            ("cbacbbccaccbbbab", 9),
            ("cbdbadbdaccaccbadadc", 16),
            ("abdacabaacddadcbaadb", 16),
            ("bcdeabbcdedabbcdbdaeaddbdd", 25),
            ("ecebcdbccbdaaacbadaccaddab", 18),
            ("lqrdfoukqdydnxfgfonizclmgsfgtm", 70),
            ("hipfogykahwapnhijhfkusvbhplckm", 70),
            ("bbcbcacbabbacabbbabcbababcbababcbbab", 9),
            ("caaabaacaccacbaccbabaabbbaacbccccbca", 9),
        ],
    )
    def test_count_palindromic_subsequence(self, s: str, expected: int):
        result = run_count_palindromic_subsequence(Solution, s)
        assert_count_palindromic_subsequence(result, expected)
