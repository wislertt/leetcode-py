import pytest

from leetcode_py import logged_test

from .helpers import assert_partition, run_partition
from .solution import Solution


class TestPalindromePartitioning:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aab", [["a", "a", "b"], ["aa", "b"]]),
            ("a", [["a"]]),
            ("ab", [["a", "b"]]),
            ("aa", [["a", "a"], ["aa"]]),
            ("abc", [["a", "b", "c"]]),
            ("aba", [["a", "b", "a"], ["aba"]]),
            ("aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]]),
            ("abba", [["a", "b", "b", "a"], ["a", "bb", "a"], ["abba"]]),
            ("zz", [["z", "z"], ["zz"]]),
            ("efe", [["e", "f", "e"], ["efe"]]),
            ("xyx", [["x", "y", "x"], ["xyx"]]),
            ("noon", [["n", "o", "o", "n"], ["n", "oo", "n"], ["noon"]]),
        ],
    )
    def test_partition(self, s: str, expected: list[list[str]]):
        result = run_partition(Solution, s)
        assert_partition(result, expected)
