import pytest

from leetcode_py import logged_test

from .helpers import assert_find_words, run_find_words
from .solution import Solution


class TestKeyboardRow:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["Hello", "Alaska", "Dad", "Peace"], ["Alaska", "Dad"]),
            (["omk"], []),
            (["adsdf", "sfd"], ["adsdf", "sfd"]),
            (["Qwerty"], ["Qwerty"]),
            (["a"], ["a"]),
            (["z"], ["z"]),
            (["Alaska"], ["Alaska"]),
            (["Dad", "Mom"], ["Dad"]),
            (["qwertyuiop"], ["qwertyuiop"]),
            (["asdfghjkl"], ["asdfghjkl"]),
            (["zxcvbnm"], ["zxcvbnm"]),
            (["Teapot"], []),
            (["Fl", "Gd"], ["Fl", "Gd"]),
            (["x", "q"], ["x", "q"]),
            (["Man"], []),
            (["POP"], ["POP"]),
        ],
    )
    def test_find_words(self, words: list[str], expected: list[str]):
        result = run_find_words(Solution, words)
        assert_find_words(result, expected)
