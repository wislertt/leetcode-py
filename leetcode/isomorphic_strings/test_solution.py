import pytest

from leetcode_py import logged_test

from .helpers import assert_is_isomorphic, run_is_isomorphic
from .solution import Solution


class TestIsomorphicStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, t, expected",
        [
            ("egg", "add", True),
            ("foo", "bar", False),
            ("paper", "title", True),
            ("f11", "b23", False),
            ("badc", "baba", False),
            ("ab", "aa", False),
            ("aa", "ab", False),
            ("a", "a", True),
            ("a", "b", True),
            ("ab", "ca", True),
            ("abc", "def", True),
            ("aa", "aa", True),
            ("abab", "baba", True),
            ("abab", "cdcd", True),
            ("egg", "edd", True),
            ("abcd", "abab", False),
            ("13", "42", True),
            ("!!", "?!", False),
        ],
    )
    def test_is_isomorphic(self, s: str, t: str, expected: bool):
        result = run_is_isomorphic(Solution, s, t)
        assert_is_isomorphic(result, expected)
