import pytest

from leetcode_py import logged_test

from .helpers import assert_is_match, run_is_match
from .solution import Solution


class TestWildcardMatching:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, p, expected",
        [
            ("aa", "a", False),
            ("aa", "*", True),
            ("cb", "?a", False),
            ("", "", True),
            ("", "*", True),
            ("", "?", False),
            ("a", "?", True),
            ("a", "", False),
            ("abc", "abc", True),
            ("abc", "a*", True),
            ("abc", "*c", True),
            ("abc", "a?c", True),
            ("abc", "a?d", False),
            ("abcdef", "a*f", True),
            ("abcdef", "a*g", False),
            ("hi", "*?", True),
            ("aaaa", "**a", True),
            ("acdcb", "a*c?b", False),
            ("mississippi", "m??*ss*?i*pi", False),
            ("abcabczzzde", "*abc???de*", True),
            ("b", "*?*?", False),
            ("aab", "?", False),
            ("", "a", False),
            ("aaab", "**??a", False),
        ],
    )
    def test_is_match(self, s: str, p: str, expected: bool):
        result = run_is_match(Solution, s, p)
        assert_is_match(result, expected)
