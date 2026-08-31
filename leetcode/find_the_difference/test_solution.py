import pytest

from leetcode_py import logged_test

from .helpers import assert_find_the_difference, run_find_the_difference
from .solution import Solution


class TestFindTheDifference:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, t, expected",
        [
            ("abcd", "abcde", "e"),
            ("", "y", "y"),
            ("a", "aa", "a"),
            ("abc", "cbad", "d"),
            ("xyz", "yxxz", "x"),
            ("hello", "oelllh", "l"),
            ("", "a", "a"),
            ("ab", "aba", "a"),
            ("aa", "aaa", "a"),
            ("aab", "abaa", "a"),
            ("abcd", "aebcd", "e"),
            ("z", "zz", "z"),
            ("mn", "mnn", "n"),
            ("pqq", "qqpp", "p"),
        ],
    )
    def test_find_the_difference(self, s: str, t: str, expected: str):
        result = run_find_the_difference(Solution, s, t)
        assert_find_the_difference(result, expected)
