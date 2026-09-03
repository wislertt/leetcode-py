import pytest

from leetcode_py import logged_test

from .helpers import assert_moves_to_stamp, run_moves_to_stamp
from .solution import Solution


class TestStampingTheSequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "stamp, target, expected",
        [
            ("abc", "ababc", [0, 2]),
            ("abca", "aabcaca", [3, 0, 1]),
            ("a", "a", [0]),
            ("a", "aaaa", [3, 2, 1, 0]),
            ("aa", "aaaa", [2, 1, 0]),
            ("abc", "abc", [0]),
            ("ab", "abab", [2, 0]),
            ("he", "hehehe", [4, 2, 0]),
            ("aba", "ababa", [2, 0]),
            ("ab", "ba", []),
            ("abc", "abca", []),
            ("ab", "aa", []),
            ("b", "abab", []),
            ("ab", "aabb", [2, 0, 1]),
            ("ba", "bbaa", [2, 0, 1]),
            ("bcbb", "bbcbb", [0, 1]),
            ("cbab", "cbabb", [1, 0]),
            ("bcca", "bcca", [0]),
            ("aaa", "aaaa", [1, 0]),
            ("acb", "acb", [0]),
            ("ab", "aaab", [0, 1, 2]),
            ("abac", "abac", [0]),
        ],
    )
    def test_moves_to_stamp(self, stamp: str, target: str, expected: list[int]):
        result = run_moves_to_stamp(Solution, stamp, target)
        assert_moves_to_stamp(result, expected, stamp, target)
