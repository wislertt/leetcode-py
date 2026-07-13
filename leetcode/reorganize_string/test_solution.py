import pytest

from leetcode_py import logged_test

from .helpers import assert_reorganize_string, run_reorganize_string
from .solution import Solution


class TestReorganizeString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s",
        [
            "aab",
            "aaab",
            "a",
            "aa",
            "ab",
            "aabb",
            "aabbcc",
            "aaaabbbb",
            "aaabbb",
            "vvvlo",
            "aaaaabbbb",
            "aaaaaab",
            "x",
            "abcabc",
        ],
    )
    def test_reorganize_string(self, s: str):
        result = run_reorganize_string(Solution, s)
        assert_reorganize_string(result, s)
