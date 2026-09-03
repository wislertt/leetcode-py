import pytest

from leetcode_py import logged_test

from .helpers import assert_repeated_string_match, run_repeated_string_match
from .solution import Solution


class TestRepeatedStringMatch:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "a, b, expected",
        [
            ("abcd", "cdabcdab", 3),
            ("a", "aa", 2),
            ("abc", "cabcabca", 4),
            ("abcd", "d", 1),
            ("abcd", "a", 1),
            ("ab", "b", 1),
            ("ab", "ba", 2),
            ("aa", "a", 1),
            ("aaac", "aac", 1),
            ("abab", "ba", 1),
            ("abc", "abcabcabc", 3),
            ("abcd", "efgh", -1),
            ("abc", "abd", -1),
            ("ab", "ac", -1),
            ("bbabb", "baaaabba", -1),
            ("bba", "abbaaaa", -1),
            ("b", "abbbabaaa", -1),
            ("babbb", "aaaabbabb", -1),
            ("b", "aaaaaaaba", -1),
            ("ba", "a", 1),
            ("bbaba", "baabaa", -1),
            ("baa", "aaa", -1),
            ("bb", "baabaab", -1),
            ("ababb", "aababb", -1),
        ],
    )
    def test_repeated_string_match(self, a: str, b: str, expected: int):
        result = run_repeated_string_match(Solution, a, b)
        assert_repeated_string_match(result, expected)
