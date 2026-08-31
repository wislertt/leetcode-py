import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_generate_palindromes,
    assert_generate_palindromes_count,
    run_generate_palindromes,
)
from .solution import Solution


class TestPalindromePermutationII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aabb", ["abba", "baab"]),
            ("abc", []),
            ("a", ["a"]),
            ("aa", ["aa"]),
            ("ab", []),
            ("aab", ["aba"]),
            ("aaa", ["aaa"]),
            ("abab", ["abba", "baab"]),
            ("aaaabb", ["aabbaa", "abaaba", "baaaab"]),
            ("aabbcc", ["abccba", "acbbca", "baccab", "bcaacb", "cabbac", "cbaabc"]),
        ],
    )
    def test_generate_palindromes(self, s: str, expected: list[str]):
        result = run_generate_palindromes(Solution, s)
        assert_generate_palindromes(result, expected)

    @logged_test
    @pytest.mark.parametrize(
        "s, expected_count",
        [
            ("aabbccdd", 24),
            ("aaaabbbb", 6),
            ("aaaaaabbbbbb", 20),
            ("aaaabbbbcccc", 90),
            ("aabbccddeeff", 720),
        ],
    )
    def test_generate_palindromes_count(self, s: str, expected_count: int):
        result = run_generate_palindromes(Solution, s)
        assert_generate_palindromes_count(result, expected_count)
