import pytest

from leetcode_py import logged_test

from .helpers import assert_partition, run_partition
from .solution import Solution


class TestPalindromePartitioning:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("s, expected", [("aab", [["a", "a", "b"], ["aa", "b"]]), ("a", [["a"]])])
    def test_partition(self, s: str, expected: list[list[str]]):
        result = run_partition(Solution, s)
        assert_partition(result, expected)
