import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_length_of_longest_substring_k_distinct,
    run_length_of_longest_substring_k_distinct,
)
from .solution import Solution


class TestLongestSubstringWithAtMostKDistinctCharacters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("eceba", 2, 3),
            ("aa", 1, 2),
            ("eceba", 1, 1),
            ("eceba", 0, 0),
            ("a", 0, 0),
            ("a", 1, 1),
            ("aaabbb", 1, 3),
            ("aaabbb", 2, 6),
            ("abaccc", 2, 4),
            ("abcabcabc", 3, 9),
            ("abcabcabc", 2, 2),
            ("ccaabbb", 2, 5),
            ("abacatatime", 3, 6),
            ("zzzz", 1, 4),
            ("abcdef", 50, 6),
        ],
    )
    def test_length_of_longest_substring_k_distinct(self, s: str, k: int, expected: int):
        result = run_length_of_longest_substring_k_distinct(Solution, s, k)
        assert_length_of_longest_substring_k_distinct(result, expected)
