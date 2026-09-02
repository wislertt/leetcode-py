import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_removals, run_maximum_removals
from .solution import Solution


class TestMaximumNumberOfRemovableCharacters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, p, removable, expected",
        [
            ("abcacb", "ab", [3, 1, 0], 2),
            ("abcbddddd", "abcd", [3, 2, 1, 4, 5, 6], 1),
            ("abcab", "abc", [0, 1, 2, 3, 4], 0),
            ("a", "a", [], 0),
            ("ab", "a", [1], 1),
            ("ab", "ab", [0], 0),
            ("abc", "ac", [1], 1),
            ("abcd", "ad", [1, 2], 2),
            ("abcabc", "abc", [5, 4, 3], 3),
            ("abcabc", "abc", [0, 1, 2], 3),
            ("aaaaa", "aa", [4, 3, 2, 1], 3),
            ("abcdefg", "aceg", [1, 3, 5], 3),
            ("abcdefg", "aceg", [6, 4, 2, 0], 0),
            ("ababab", "aaa", [1, 3, 5], 3),
            ("xyxyxy", "xy", [0, 2, 4], 2),
            ("mississippi", "misis", [0, 2, 4, 6, 8, 10], 0),
            ("ccbbc", "c", [0, 1], 2),
            ("acbacccc", "cc", [2, 0, 4, 1, 3, 7, 6], 6),
            ("aacbc", "aac", [2, 0, 4, 1], 1),
            ("ccbcacca", "ccbcacca", [6], 0),
            ("cbcac", "bc", [2, 4, 0, 1], 1),
            ("cbaababc", "baaab", [7, 0, 1, 4, 5], 2),
        ],
    )
    def test_maximum_removals(self, s: str, p: str, removable: list[int], expected: int):
        result = run_maximum_removals(Solution, s, p, removable)
        assert_maximum_removals(result, expected)
