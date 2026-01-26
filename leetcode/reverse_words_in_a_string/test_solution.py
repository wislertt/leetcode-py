import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_words, run_reverse_words
from .solution import Solution


class TestReverseWordsInAString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("the sky is blue", "blue is sky the"),
            ("  hello world  ", "world hello"),
            ("a good   example", "example good a"),
            ("hello", "hello"),
            ("  hello", "hello"),
            ("hello  ", "hello"),
            ("a   b   c", "c b a"),
            ("the", "the"),
            ("  the   sky  is  blue  ", "blue is sky the"),
            ("one", "one"),
            ("two words", "words two"),
            ("  multiple   spaces   here  ", "here spaces multiple"),
            ("a b c d e", "e d c b a"),
            ("  leading and trailing  ", "trailing and leading"),
            ("word", "word"),
        ],
    )
    def test_reverse_words(self, s: str, expected: str):
        result = run_reverse_words(Solution, s)
        assert_reverse_words(result, expected)
