import pytest

from leetcode_py import logged_test

from .helpers import assert_most_common_word, run_most_common_word
from .solution import Solution


class TestMostCommonWord:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "paragraph, banned, expected",
        [
            ("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"], "ball"),
            ("Bob hit a ball, the hit BALL flew far after it was hit.", [], "hit"),
            ("a.", [], "a"),
            ("L, P! X! ..., L", [], "l"),
            ("a, a, a, a, b,b,b,c, c", ["a"], "b"),
            ("Bob", [], "bob"),
            ("banned banned okay", ["banned"], "okay"),
            ("x. y? z! x", ["y", "z"], "x"),
            ("Aa aA AA bb", ["bb"], "aa"),
            ("ball, BALL ball ball", [], "ball"),
            ("one two two three three three", ["three"], "two"),
            ("cat, dog. cat, dog, cat", [], "cat"),
            ("Hello hello HELLO world", ["hello"], "world"),
            ("a!!b..c,,a", ["c"], "a"),
            ("Hi hi HI hI there", [], "hi"),
            ("the quick brown fox jumps over the lazy dog the end", [], "the"),
            ("We, we, WE... will w!ill win", ["will"], "we"),
            ("gray gray grey", ["grey"], "gray"),
            ("spot, spot. spot? Spot! spott", ["spot"], "spott"),
            ("z", [], "z"),
        ],
    )
    def test_most_common_word(self, paragraph: str, banned: list[str], expected: str):
        result = run_most_common_word(Solution, paragraph, banned)
        assert_most_common_word(result, expected)
