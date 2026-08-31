import pytest

from leetcode_py import logged_test

from .helpers import assert_valid_word_square, run_valid_word_square
from .solution import Solution


class TestValidWordSquare:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["abcd", "bnrt", "crmy", "dtye"], True),
            (["abcd", "bnrt", "crm", "dt"], True),
            (["ball", "area", "read", "lady"], False),
            (["a"], True),
            (["ab", "ba"], True),
            (["ab", "b"], True),
            (["abc", "de"], False),
            (["abc", "b", "c"], True),
            (["a", "b", "c"], False),
            (["aa", "aa"], True),
            (["ab", "aa"], False),
            (["aaa", "aaa", "aaa"], True),
            (["abcd", "bnrt", "crm"], False),
            (["ball", "asee", "let", "lep"], False),
            (["abcd", "bnrt", "crm", "de"], False),
            (["m"], True),
        ],
    )
    def test_valid_word_square(self, words: list[str], expected: bool):
        result = run_valid_word_square(Solution, words)
        assert_valid_word_square(result, expected)
