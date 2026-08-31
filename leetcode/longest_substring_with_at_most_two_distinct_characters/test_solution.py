import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_length_of_longest_substring_two_distinct,
    run_length_of_longest_substring_two_distinct,
)
from .solution import Solution


class TestLongestSubstringWithAtMostTwoDistinctCharacters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("eceba", 3),
            ("ccaabbb", 5),
            ("a", 1),
            ("aa", 2),
            ("ab", 2),
            ("abc", 2),
            ("abaccc", 4),
            ("aaaaa", 5),
            ("abab", 4),
            ("aabb", 4),
            ("aabc", 3),
            ("abcabc", 2),
            ("abba", 4),
            ("abcdea", 2),
            ("aabbcc", 4),
            ("ececee", 6),
            ("xyzx", 2),
            ("ababa", 5),
            ("abaacabc", 4),
        ],
    )
    def test_length_of_longest_substring_two_distinct(self, s: str, expected: int):
        result = run_length_of_longest_substring_two_distinct(Solution, s)
        assert_length_of_longest_substring_two_distinct(result, expected)
