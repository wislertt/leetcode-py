import pytest

from leetcode_py import logged_test

from .helpers import assert_expand, run_expand
from .solution import Solution


class TestBraceExpansion:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("{a,b}c{d,e}f", ["acdf", "acef", "bcdf", "bcef"]),
            ("abcd", ["abcd"]),
            ("{a,b}{x,y}", ["ax", "ay", "bx", "by"]),
            ("a", ["a"]),
            ("{b,a}", ["a", "b"]),
            ("k{a,b,c}z", ["kaz", "kbz", "kcz"]),
            (
                "{x,y}a{b,c}d{e,f}",
                ["xabde", "xabdf", "xacde", "xacdf", "yabde", "yabdf", "yacde", "yacdf"],
            ),
            ("ab{q,r}cd", ["abqcd", "abrcd"]),
            ("{m,n}{o,p}", ["mo", "mp", "no", "np"]),
            ("zzz", ["zzz"]),
            (
                "a{b,c}d{e,f}g{h,i}",
                ["abdegh", "abdegi", "abdfgh", "abdfgi", "acdegh", "acdegi", "acdfgh", "acdfgi"],
            ),
            ("{u,v}w", ["uw", "vw"]),
        ],
    )
    def test_expand(self, s: str, expected: list[str]):
        result = run_expand(Solution, s)
        assert_expand(result, expected)
