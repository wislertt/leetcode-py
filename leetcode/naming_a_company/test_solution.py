import pytest

from leetcode_py import logged_test

from .helpers import assert_distinct_names, run_distinct_names
from .solution import Solution


class TestNamingACompany:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "ideas, expected",
        [
            (["coffee", "donuts", "time", "toffee"], 6),
            (["lack", "back"], 0),
            (["ab", "cd"], 2),
            (["ab", "ba"], 2),
            (["a", "b"], 0),
            (["aa", "bb"], 2),
            (["aaa", "aba", "aca"], 0),
            (["ab", "cb", "db"], 0),
            (["abc", "abd", "xyz"], 4),
            (["x", "y", "xy"], 0),
            (["time", "coffee"], 2),
            (["bank", "canal", "man"], 6),
            (["aaa", "baa", "caa"], 0),
            (["a", "b", "bab", "bba", "cb"], 8),
            (["a", "aa", "aba", "bb", "ca", "cbc"], 14),
            (["abc", "ba", "bcc"], 4),
            (["a", "aa", "cab"], 4),
            (["a", "b", "bab", "bb", "bbc"], 0),
            (["baa", "bb", "c"], 4),
            (["abc", "ccc"], 2),
            (["a", "aba", "ac", "b", "bc"], 0),
            (["a", "aab", "ac", "b", "ca", "ccb"], 16),
            (["aaa", "aca", "b", "ba", "cbb", "cc"], 24),
            (["ab", "bbc", "c"], 6),
            (["aac", "aca", "b", "baa"], 8),
            (["b", "bcc", "c", "ca"], 2),
            (["bb", "cb"], 0),
        ],
    )
    def test_distinct_names(self, ideas: list[str], expected: int):
        result = run_distinct_names(Solution, ideas)
        assert_distinct_names(result, expected)
