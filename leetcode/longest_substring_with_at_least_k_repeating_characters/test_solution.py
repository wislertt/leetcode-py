import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_longest_substring_with_at_least_k_repeating_characters,
    run_longest_substring_with_at_least_k_repeating_characters,
)
from .solution import Solution


class TestLongestSubstringWithAtLeastKRepeatingCharacters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("aaabb", 3, 3),
            ("ababbc", 2, 5),
            ("aaaa", 1, 4),
            ("a", 1, 1),
            ("ab", 1, 2),
            ("ab", 2, 0),
            ("abcde", 5, 0),
            ("aabbcc", 2, 6),
            ("aaabbbccc", 3, 9),
            ("ababacb", 3, 0),
            ("bbaaacbd", 3, 3),
            ("weitaim", 2, 0),
            ("zzzzzzzz", 4, 8),
            ("abcabc", 2, 6),
            ("aabbbaa", 3, 7),
            ("abcdeabcde", 2, 10),
            ("acccab", 1, 6),
            ("dbceec", 2, 4),
            ("bca", 4, 0),
            ("ecdbd", 2, 0),
        ],
    )
    def test_longest_substring_with_at_least_k_repeating_characters(
        self, s: str, k: int, expected: int
    ):
        result = run_longest_substring_with_at_least_k_repeating_characters(Solution, s, k)
        assert_longest_substring_with_at_least_k_repeating_characters(result, expected)
