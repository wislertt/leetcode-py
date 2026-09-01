import pytest

from leetcode_py import logged_test

from .helpers import assert_are_almost_equal, run_are_almost_equal
from .solution import Solution


class TestCheckIfOneStringSwapCanMakeStringsEqual:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s1, s2, expected",
        [
            ("bank", "kanb", True),
            ("attack", "defend", False),
            ("kelb", "kelb", True),
            ("a", "a", True),
            ("a", "b", False),
            ("ab", "ba", True),
            ("ab", "cd", False),
            ("aa", "aa", True),
            ("ab", "aa", False),
            ("abcd", "dcba", False),
            ("abcd", "badc", False),
            ("abcd", "abcd", True),
            ("abcd", "abce", False),
            ("aab", "aba", True),
            ("aab", "baa", True),
            ("abc", "cba", True),
            ("abcd", "cbad", True),
            ("aaab", "aaba", True),
            ("aaab", "aabb", False),
            ("abcde", "abced", True),
            ("converse", "conserve", True),
            ("longerstring", "longerstrnig", True),
            ("bb", "ab", False),
            ("ababb", "babba", False),
        ],
    )
    def test_are_almost_equal(self, s1: str, s2: str, expected: bool):
        result = run_are_almost_equal(Solution, s1, s2)
        assert_are_almost_equal(result, expected)
