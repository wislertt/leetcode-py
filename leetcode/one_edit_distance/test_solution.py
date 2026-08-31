import pytest

from leetcode_py import logged_test

from .helpers import assert_is_one_edit_distance, run_is_one_edit_distance
from .solution import Solution


class TestOneEditDistance:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, t, expected",
        [
            ("ab", "acb", True),
            ("cab", "ad", False),
            ("1203", "1213", True),
            ("", "", False),
            ("", "a", True),
            ("a", "", True),
            ("a", "a", False),
            ("abc", "abc", False),
            ("abc", "ab", True),
            ("ab", "abc", True),
            ("abc", "abcd", True),
            ("abcd", "abc", True),
            ("abc", "axcy", False),
            ("abcdef", "abc", False),
            ("x", "y", True),
            ("xy", "xz", True),
            ("xy", "xzy", True),
            ("teacher", "taecher", False),
            ("a", "ba", True),
            ("ba", "a", True),
            ("1234", "1234", False),
            ("kitten", "sitten", True),
            ("abc", "abd", True),
            ("abcd", "abdc", False),
            ("abcd", "acbd", False),
        ],
    )
    def test_is_one_edit_distance(self, s: str, t: str, expected: bool):
        result = run_is_one_edit_distance(Solution, s, t)
        assert_is_one_edit_distance(result, expected)
