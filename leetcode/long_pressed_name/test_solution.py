import pytest

from leetcode_py import logged_test

from .helpers import assert_is_long_pressed_name, run_is_long_pressed_name
from .solution import Solution


class TestLongPressedName:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "name, typed, expected",
        [
            ("alex", "aaleex", True),
            ("saeed", "ssaaedd", False),
            ("leelee", "lleeelee", True),
            ("laiden", "laiden", True),
            ("a", "a", True),
            ("a", "aa", True),
            ("a", "b", False),
            ("ab", "aab", True),
            ("ab", "ba", False),
            ("abc", "aabbcc", True),
            ("abc", "abcc", True),
            ("abc", "ab", False),
            ("aab", "aaa", False),
            ("alex", "aaleexa", False),
            ("vtkgn", "vttkgnn", True),
            ("aac", "bacca", False),
            ("a", "ccb", False),
            ("acc", "caaca", False),
            ("bbb", "cacb", False),
            ("acc", "bcccb", False),
            ("bb", "bcab", False),
            ("bbc", "bbc", True),
            ("cbb", "bbcca", False),
            ("aba", "acacc", False),
            ("aba", "bacbc", False),
        ],
    )
    def test_is_long_pressed_name(self, name: str, typed: str, expected: bool):
        result = run_is_long_pressed_name(Solution, name, typed)
        assert_is_long_pressed_name(result, expected)
