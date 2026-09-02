import pytest

from leetcode_py import logged_test

from .helpers import assert_min_cut, run_min_cut
from .solution import Solution


class TestPalindromePartitioningII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aab", 1),
            ("a", 0),
            ("ab", 1),
            ("aa", 0),
            ("abc", 2),
            ("aba", 0),
            ("aaa", 0),
            ("abba", 0),
            ("abbab", 1),
            ("abcba", 0),
            ("abcde", 4),
            ("aabbcc", 2),
            ("ababbbabbababa", 3),
            ("leet", 2),
            ("racecar", 0),
            ("banana", 1),
            ("abaaabaaabbabab", 2),
            ("bbbbaaaba", 2),
            ("ababbbaabaabaaabbbaa", 4),
            ("babbabaaaaabaabbabbaaaaa", 4),
        ],
    )
    def test_min_cut(self, s: str, expected: int):
        result = run_min_cut(Solution, s)
        assert_min_cut(result, expected)
