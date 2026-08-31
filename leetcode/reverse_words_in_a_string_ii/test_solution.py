import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_words, run_reverse_words
from .solution import Solution


class TestReverseWordsInAStringII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            (
                ["t", "h", "e", " ", "s", "k", "y", " ", "i", "s", " ", "b", "l", "u", "e"],
                ["b", "l", "u", "e", " ", "i", "s", " ", "s", "k", "y", " ", "t", "h", "e"],
            ),
            (["a"], ["a"]),
            (["a", "b"], ["a", "b"]),
            (["h", "i"], ["h", "i"]),
            (["a", " ", "b"], ["b", " ", "a"]),
            (["a", "b", " ", "c", "d"], ["c", "d", " ", "a", "b"]),
            (["a", "b", "c", " ", "d"], ["d", " ", "a", "b", "c"]),
            (
                ["h", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"],
                ["w", "o", "r", "l", "d", " ", "h", "e", "l", "l", "o"],
            ),
            (
                ["o", "n", "e", " ", "t", "w", "o", " ", "t", "h", "r", "e", "e"],
                ["t", "h", "r", "e", "e", " ", "t", "w", "o", " ", "o", "n", "e"],
            ),
            (["f", "o", "o", " ", "b", "a", "r"], ["b", "a", "r", " ", "f", "o", "o"]),
            (["1", "2", " ", "3"], ["3", " ", "1", "2"]),
            (["a", " ", "b", " ", "c"], ["c", " ", "b", " ", "a"]),
            (["a", "b", "c"], ["a", "b", "c"]),
            (["w", "o", "r", "d"], ["w", "o", "r", "d"]),
        ],
    )
    def test_reverse_words(self, s: list[str], expected: list[str]):
        result = run_reverse_words(Solution, s)
        assert_reverse_words(result, expected)
