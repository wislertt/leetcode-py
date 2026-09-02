import pytest

from leetcode_py import logged_test

from .helpers import assert_max_unique_split, run_max_unique_split
from .solution import Solution


class TestSplitAStringIntoTheMaxNumberOfUniqueSubstringsTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("ababccc", 5),
            ("aba", 2),
            ("aa", 1),
            ("a", 1),
            ("ab", 2),
            ("abc", 3),
            ("aaaa", 2),
            ("aaaaaa", 3),
            ("abab", 3),
            ("abcabc", 4),
            ("aabb", 3),
            ("abcde", 5),
            ("aaaaaaaaaaaaaaaa", 5),
            ("abcdefghijklmnop", 16),
            ("cgabbf", 5),
            ("adabggbdbg", 7),
            ("b", 1),
            ("agad", 3),
        ],
    )
    def test_max_unique_split(self, s: str, expected: int):
        result = run_max_unique_split(Solution, s)
        assert_max_unique_split(result, expected)
