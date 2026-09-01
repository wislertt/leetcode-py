import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_deletions, run_minimum_deletions
from .solution import Solution


class TestMinimumDeletionsToMakeStringBalanced:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aababbab", 2),
            ("bbaaaaabb", 2),
            ("a", 0),
            ("b", 0),
            ("ab", 0),
            ("ba", 1),
            ("aaaa", 0),
            ("bbbb", 0),
            ("bbaa", 2),
            ("abab", 1),
            ("bbbaaa", 3),
            ("aababb", 1),
            ("bbabbb", 1),
            ("abababab", 3),
            ("baabbaab", 3),
            ("babbbabb", 2),
            ("aabababbba", 3),
            ("aa", 0),
            ("bbabab", 2),
            ("ababaaababaa", 4),
            ("aaababaabaabbaaa", 5),
            ("aabaabbbabaaab", 5),
            ("aaabbbabbb", 1),
        ],
    )
    def test_minimum_deletions(self, s: str, expected: int):
        result = run_minimum_deletions(Solution, s)
        assert_minimum_deletions(result, expected)
