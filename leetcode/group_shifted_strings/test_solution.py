import pytest

from leetcode_py import logged_test

from .helpers import assert_group_strings, run_group_strings
from .solution import Solution


class TestGroupShiftedStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "strings, expected",
        [
            (["abc", "bcd"], [["abc", "bcd"]]),
            (["az", "ba"], [["az", "ba"]]),
            (["a", "z"], [["a", "z"]]),
            (["a"], [["a"]]),
            (["abc", "xyz"], [["abc", "xyz"]]),
            (["acef", "bdfg"], [["acef", "bdfg"]]),
            (["abc", "bcd", "xyz"], [["abc", "bcd", "xyz"]]),
            (["ab", "ba", "cd"], [["ab", "cd"], ["ba"]]),
            (["a", "b", "y", "z"], [["a", "b", "y", "z"]]),
            (["yz", "za"], [["yz", "za"]]),
            (["abc", "bcd", "acef"], [["abc", "bcd"], ["acef"]]),
            (["pqrs", "qrst"], [["pqrs", "qrst"]]),
            (["aa", "bb"], [["aa", "bb"]]),
            (["zy", "ab"], [["zy"], ["ab"]]),
            (["abc", "def", "ghi"], [["abc", "def", "ghi"]]),
        ],
    )
    def test_group_strings(self, strings: list[str], expected: list[list[str]]):
        result = run_group_strings(Solution, strings)
        assert_group_strings(result, expected)
