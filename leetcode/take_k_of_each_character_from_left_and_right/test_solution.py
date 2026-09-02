import pytest

from leetcode_py import logged_test

from .helpers import assert_take_characters, run_take_characters
from .solution import Solution


class TestTakeKOfEachCharacterFromLeftAndRight:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("aabaaaacaabc", 2, 8),
            ("a", 1, -1),
            ("abc", 1, 3),
            ("aabbcc", 1, 4),
            ("aabbcc", 2, 6),
            ("abcabc", 2, 6),
            ("aaa", 0, 0),
            ("abc", 0, 0),
            ("aabbc", 1, 3),
            ("ccbbbaaa", 2, 6),
            ("ac", 1, -1),
            ("bbbbcc", 1, -1),
            ("abccba", 2, 6),
            ("cbacbacba", 3, 9),
            ("abab", 2, -1),
            ("bcbcaa", 4, -1),
            ("b", 0, 0),
            ("bb", 2, -1),
            ("acacabb", 4, -1),
            ("bccabbaac", 3, 9),
        ],
    )
    def test_take_characters(self, s: str, k: int, expected: int):
        result = run_take_characters(Solution, s, k)
        assert_take_characters(result, expected)
