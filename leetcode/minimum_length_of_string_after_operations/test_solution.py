import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_length, run_minimum_length
from .solution import Solution


class TestMinimumLengthOfStringAfterOperations:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abaacbcbb", 5),
            ("aa", 2),
            ("a", 1),
            ("ab", 2),
            ("abc", 3),
            ("aaa", 1),
            ("aaaa", 2),
            ("aaaaa", 1),
            ("aaaaaa", 2),
            ("aabb", 4),
            ("aabbcc", 6),
            ("aaabbb", 2),
            ("aaabbbccc", 3),
            ("abcabcabc", 3),
            ("aabbccdd", 8),
            ("aabbaabbcc", 6),
            ("abcba", 5),
            ("zzzyyxxx", 4),
            ("aaab", 2),
            ("baaa", 2),
            ("ababab", 2),
            ("aabbaabbaa", 4),
            ("fddbbfbffe", 6),
            ("fffeb", 3),
        ],
    )
    def test_minimum_length(self, s: str, expected: int):
        result = run_minimum_length(Solution, s)
        assert_minimum_length(result, expected)
