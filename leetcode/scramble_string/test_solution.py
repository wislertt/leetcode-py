import pytest

from leetcode_py import logged_test

from .helpers import assert_is_scramble, run_is_scramble
from .solution import Solution


class TestScrambleString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s1, s2, expected",
        [
            ("great", "rgeat", True),
            ("abcde", "caebd", False),
            ("a", "a", True),
            ("a", "b", False),
            ("ab", "ba", True),
            ("ab", "ab", True),
            ("abc", "bac", True),
            ("abc", "cab", True),
            ("abc", "acb", True),
            ("abc", "bca", True),
            ("abc", "cba", True),
            ("abcd", "bdac", False),
            ("abcd", "cdab", True),
            ("abcd", "dcba", True),
            ("great", "great", True),
            ("great", "rgtae", True),
            ("great", "tager", True),
            ("xabcdb", "babcxd", True),
            ("aa", "aa", True),
            ("ab", "aa", False),
            ("abc", "abd", False),
            ("bea", "bae", True),
            ("ca", "ca", True),
            ("de", "de", True),
            ("cbea", "abec", True),
            ("edcdbcb", "eecacac", False),
        ],
    )
    def test_is_scramble(self, s1: str, s2: str, expected: bool):
        result = run_is_scramble(Solution, s1, s2)
        assert_is_scramble(result, expected)
