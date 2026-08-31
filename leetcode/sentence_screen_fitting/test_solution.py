import pytest

from leetcode_py import logged_test

from .helpers import assert_words_typing, run_words_typing
from .solution import Solution


class TestSentenceScreenFitting:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "sentence, rows, cols, expected",
        [
            (["hello", "world"], 2, 8, 1),
            (["a", "bcd", "e"], 3, 6, 2),
            (["i", "had", "apple", "pie"], 4, 5, 1),
            (["a"], 1, 1, 1),
            (["a"], 5, 3, 10),
            (["ab"], 2, 3, 2),
            (["a"], 2, 2, 2),
            (["hello", "world"], 1, 15, 1),
            (["a", "b"], 3, 5, 4),
            (["f", "p", "a"], 8, 7, 10),
            (["hello"], 1000, 6, 1000),
            (["abc", "de"], 4, 5, 2),
            (["xy"], 3, 2, 3),
            (["ab", "cd"], 2, 2, 1),
            (["a", "bcd"], 4, 4, 2),
            (["ab", "cd", "e"], 5, 4, 2),
        ],
    )
    def test_words_typing(self, sentence: list[str], rows: int, cols: int, expected: int):
        result = run_words_typing(Solution, sentence, rows, cols)
        assert_words_typing(result, expected)
