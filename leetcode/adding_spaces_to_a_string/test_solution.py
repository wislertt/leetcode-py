import pytest

from leetcode_py import logged_test

from .helpers import assert_add_spaces, run_add_spaces
from .solution import Solution


class TestAddingSpacesToString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, spaces, expected",
        [
            ("LeetcodeHelpsMeLearn", [8, 13, 15], "Leetcode Helps Me Learn"),
            ("icodeinpython", [1, 5, 7, 9], "i code in py thon"),
            ("spacing", [0, 1, 2, 3, 4, 5, 6], " s p a c i n g"),
            ("EnjoyYourCoffee", [5, 9], "Enjoy Your Coffee"),
            ("a", [0], " a"),
            ("ab", [0], " ab"),
            ("ab", [1], "a b"),
            ("abc", [0, 1, 2], " a b c"),
            ("abc", [2], "ab c"),
            ("abcdef", [2], "ab cdef"),
            ("hello", [4], "hell o"),
            ("Coding", [3], "Cod ing"),
            ("AbcDefGhi", [3, 6], "Abc Def Ghi"),
            ("aaaaaaaaaaaa", [0, 6, 11], " aaaaaa aaaaa a"),
            ("IBuRcYu", [0, 1, 2, 3], " I B u RcYu"),
            ("mKvXnf", [1, 4, 5], "m KvX n f"),
            ("Ts", [1], "T s"),
            ("ueegFaMEP", [2, 5, 8], "ue egF aME P"),
            ("JYuklzq", [1, 2, 4, 5], "J Y uk l zq"),
            ("r", [0], " r"),
        ],
    )
    def test_add_spaces(self, s: str, spaces: list[int], expected: str):
        result = run_add_spaces(Solution, s, spaces)
        assert_add_spaces(result, expected)
