import pytest

from leetcode_py import logged_test

from .helpers import assert_valid_palindrome, run_valid_palindrome
from .solution import Solution


class TestValidPalindromeII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aba", True),
            ("abca", True),
            ("abc", False),
            ("a", True),
            ("aa", True),
            ("ab", True),
            ("aba", True),
            ("abccbda", True),
            ("deeee", True),
            ("racecar", True),
            ("raceecar", True),
            ("abcdef", False),
            ("abcdedcba", True),
            ("abcdxcba", True),
            ("abcddcba", True),
            ("lcupuucul", False),
            ("lcupuupcul", False),
            (
                "aguokepatgbnvfqmgmlcupuufxoohdfpgjfmysgvhmvffcnqxjjxqncffomhvoxymzgpfdohooxfuupuculmgmqfvnbgtapekouga",
                False,
            ),
        ],
    )
    def test_valid_palindrome(self, s: str, expected: bool):
        result = run_valid_palindrome(Solution, s)
        assert_valid_palindrome(result, expected)
