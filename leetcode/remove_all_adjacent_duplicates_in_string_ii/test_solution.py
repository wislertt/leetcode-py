import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_duplicates, run_remove_duplicates
from .solution import Solution


class TestRemoveAllAdjacentDuplicatesInStringIiTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("abcd", 2, "abcd"),
            ("deeedbbcccbdaa", 3, "aa"),
            ("pbbcggttciiippooaais", 2, "ps"),
            ("aa", 2, ""),
            ("aaa", 2, "a"),
            ("aaa", 3, ""),
            ("aabb", 2, ""),
            ("aabbaa", 2, ""),
            ("abccba", 2, ""),
            ("mississippi", 2, "m"),
            ("aaaa", 3, "a"),
            ("aaaaa", 3, "aa"),
            ("abbcc", 2, "a"),
            ("abcddcba", 2, ""),
            ("yyyyyyy", 4, "yyy"),
            ("abcdeedcba", 2, ""),
        ],
    )
    def test_remove_duplicates(self, s: str, k: int, expected: str):
        result = run_remove_duplicates(Solution, s, k)
        assert_remove_duplicates(result, expected)
