import pytest

from leetcode_py import logged_test

from .helpers import assert_num_distinct, run_num_distinct
from .solution import Solution


class TestDistinctSubsequences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, t, expected",
        [
            ("rabbbit", "rabbit", 3),
            ("babgbag", "bag", 5),
            ("a", "a", 1),
            ("a", "b", 0),
            ("aaa", "a", 3),
            ("aaa", "aa", 3),
            ("aaaa", "aa", 6),
            ("abc", "abc", 1),
            ("abc", "abcd", 0),
            ("abab", "ab", 3),
            ("abab", "bab", 1),
            ("abcabc", "abc", 4),
            ("dddd", "dd", 6),
            ("aab", "ab", 2),
            ("bbb", "bb", 3),
        ],
    )
    def test_num_distinct(self, s: str, t: str, expected: int):
        result = run_num_distinct(Solution, s, t)
        assert_num_distinct(result, expected)
