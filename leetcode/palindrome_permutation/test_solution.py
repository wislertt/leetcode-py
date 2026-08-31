import pytest

from leetcode_py import logged_test

from .helpers import assert_can_permute_palindrome, run_can_permute_palindrome
from .solution import Solution


class TestPalindromePermutation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("code", False),
            ("aab", True),
            ("carerac", True),
            ("a", True),
            ("ab", False),
            ("aa", True),
            ("abba", True),
            ("abc", False),
            ("aabb", True),
            ("aabbc", True),
            ("aabbcc", True),
            ("abcabc", True),
            ("racecar", True),
            ("zz", True),
            ("abcde", False),
        ],
    )
    def test_can_permute_palindrome(self, s: str, expected: bool):
        result = run_can_permute_palindrome(Solution, s)
        assert_can_permute_palindrome(result, expected)
