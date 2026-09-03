import pytest

from leetcode_py import logged_test

from .helpers import assert_rotate_string, run_rotate_string
from .solution import Solution


class TestRotateString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, goal, expected",
        [
            ("abcde", "cdeab", True),
            ("abcde", "abced", False),
            ("a", "a", True),
            ("a", "b", False),
            ("m", "f", False),
            ("ab", "ba", True),
            ("ab", "aa", False),
            ("abc", "abc", True),
            ("abc", "cab", True),
            ("abc", "bca", True),
            ("abc", "acb", False),
            ("aaaa", "aaaa", True),
            ("abab", "baba", True),
            ("abab", "abba", False),
            ("waterbottle", "erbottlewat", True),
            ("waterbottle", "erbottlewta", False),
            ("gcmbfll", "llgcmbf", True),
            ("gcmbfll", "fllgcmb", True),
            ("gcmbfll", "gcmbfll", True),
            ("bbbbaabb", "bbbbaaba", False),
            ("xyxxy", "yxxyx", True),
            ("xyxxy", "xyxyx", True),
            ("bbbbbbbaa", "bbaababab", False),
            ("baabbbb", "bbbbbaa", True),
            ("bbaab", "aaaab", False),
            ("bbbaabbb", "aabbbbbb", True),
            ("baabaaa", "bbbbbab", False),
            ("baa", "aba", True),
            ("abbbaaabba", "abbaabbbaa", True),
            ("bbaabab", "aabaabb", False),
        ],
    )
    def test_rotate_string(self, s: str, goal: str, expected: bool):
        result = run_rotate_string(Solution, s, goal)
        assert_rotate_string(result, expected)
