import pytest

from leetcode_py import logged_test

from .helpers import assert_merge_alternately, run_merge_alternately
from .solution import Solution


class TestTestMergeStringsAlternately:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "word1, word2, expected",
        [
            ("abc", "pqr", "apbqcr"),
            ("ab", "pqrs", "apbqrs"),
            ("abcd", "pq", "apbqcd"),
            ("a", "b", "ab"),
            ("a", "xyz", "axyz"),
            ("abc", "d", "adbc"),
            ("hello", "world", "hweolrllod"),
            ("x", "", "x"),
            ("", "y", "y"),
            ("ab", "cd", "acbd"),
            ("abc", "defg", "adbecfg"),
            ("abcde", "fg", "afbgcde"),
            ("12", "345", "13245"),
        ],
    )
    def test_merge_alternately(self, word1: str, word2: str, expected: str):
        result = run_merge_alternately(Solution, word1, word2)
        assert_merge_alternately(result, expected)
