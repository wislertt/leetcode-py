import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_find_substring_in_wrapround_string,
    run_find_substring_in_wrapround_string,
)
from .solution import Solution


class TestUniqueSubstringsInWraparoundString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("a", 1),
            ("cac", 2),
            ("zab", 6),
            ("z", 1),
            ("aaa", 1),
            ("ba", 2),
            ("za", 3),
            ("yz", 3),
            ("zya", 3),
            ("zabc", 10),
            ("acacbcbb", 4),
            ("popyrsrqrq", 9),
            ("abcdefghijklmnopqrstuvwxyz", 351),
            ("zabzab", 6),
            ("abzab", 6),
            ("pmcand", 6),
            ("jaindufd", 7),
            ("jdhne", 5),
            ("dowblz", 6),
            ("raarawy", 4),
        ],
    )
    def test_find_substring_in_wrapround_string(self, s: str, expected: int):
        result = run_find_substring_in_wrapround_string(Solution, s)
        assert_find_substring_in_wrapround_string(result, expected)
