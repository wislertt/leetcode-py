import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_duplicate_letters, run_remove_duplicate_letters
from .solution import Solution


class TestRemoveDuplicateLetters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("bcabc", "abc"),
            ("cbacdcbc", "acdb"),
            ("abacb", "abc"),
            ("bcac", "bac"),
            ("cdadabcc", "adbc"),
            ("abacbdc", "abcd"),
            ("cbabc", "abc"),
            ("abacbda", "abcd"),
            ("edebbed", "bed"),
            ("bcabcba", "abc"),
            ("cba", "cba"),
            ("aaa", "a"),
            ("a", "a"),
            ("bcbcbcbcbcacbda", "acbd"),
            ("b", "b"),
            ("abab", "ab"),
            ("db", "db"),
            ("cbcc", "bc"),
        ],
    )
    def test_remove_duplicate_letters(self, s: str, expected: str):
        result = run_remove_duplicate_letters(Solution, s)
        assert_remove_duplicate_letters(result, expected)
