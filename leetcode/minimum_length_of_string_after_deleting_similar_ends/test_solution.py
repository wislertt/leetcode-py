import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_length, run_minimum_length
from .solution import Solution


class TestMinimumLengthOfStringAfterDeletingSimilarEnds:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("ca", 2),
            ("cabaabac", 0),
            ("aabccabba", 3),
            ("a", 1),
            ("b", 1),
            ("c", 1),
            ("aa", 0),
            ("ab", 2),
            ("abc", 3),
            ("aba", 1),
            ("abca", 2),
            ("aabaa", 1),
            ("abcba", 1),
            ("abccba", 0),
            ("aaabbb", 6),
            ("aaabbbccc", 9),
            ("aabbcc", 6),
            ("ccbbbaaa", 8),
            ("abcabc", 6),
            ("cabacc", 1),
            ("aabbccaa", 4),
            ("abccbaabc", 9),
            ("cac", 1),
            ("bbacabb", 1),
            ("cccabccc", 2),
            ("abab", 4),
            ("babcac", 6),
            ("baba", 4),
            ("abbacb", 6),
            ("accaacaacc", 10),
        ],
    )
    def test_minimum_length(self, s: str, expected: int):
        result = run_minimum_length(Solution, s)
        assert_minimum_length(result, expected)
