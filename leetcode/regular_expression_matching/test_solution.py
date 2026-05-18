import pytest

from leetcode_py import logged_test

from .helpers import assert_is_match, run_is_match
from .solution import Solution


class TestRegularExpressionMatching:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, p, expected",
        [
            ("aa", "a", False),
            ("aa", "a*", True),
            ("ab", ".*", True),
            ("aab", "c*a*b", True),
            ("mississippi", "mis*is*p*.", False),
            ("a", "ab*", True),
            ("", "a*", True),
            ("", ".*", True),
            ("ab", ".*c", False),
            ("aaa", "a*a", True),
            ("aaa", "aaaa", False),
            ("abc", "a.c", True),
            ("abc", "a.*c", True),
            ("a", ".", True),
            ("abcdef", ".*", True),
            ("abbbbc", "ab*c", True),
            ("abbbbc", "ab*bc", True),
        ],
    )
    def test_is_match(self, s: str, p: str, expected: bool):
        result = run_is_match(Solution, s, p)
        assert_is_match(result, expected)
