import pytest

from leetcode_py import logged_test

from .helpers import assert_buddy_strings, run_buddy_strings
from .solution import Solution


class TestBuddyStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, goal, expected",
        [
            ("ab", "ba", True),
            ("ab", "ab", False),
            ("aa", "aa", True),
            ("abcd", "cbad", True),
            ("a", "a", False),
            ("a", "b", False),
            ("ab", "abc", False),
            ("abc", "acb", True),
            ("abc", "bac", True),
            ("abc", "abc", False),
            ("aab", "aab", True),
            ("abc", "abd", False),
            ("ab", "cd", False),
            ("abcd", "badc", False),
            ("aa", "ab", False),
            ("abcabc", "abcabc", True),
            ("abc", "abcd", False),
            ("abab", "abab", True),
            ("aabb", "bbaa", False),
            ("abc", "cba", True),
            ("abcde", "abced", True),
            ("ab", "aa", False),
        ],
    )
    def test_buddy_strings(self, s: str, goal: str, expected: bool):
        result = run_buddy_strings(Solution, s, goal)
        assert_buddy_strings(result, expected)
