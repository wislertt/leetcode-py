import pytest

from leetcode_py import logged_test

from .helpers import assert_valid_word_abbreviation, run_valid_word_abbreviation
from .solution import Solution


class TestValidWordAbbreviation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "word, abbr, expected",
        [
            ("internationalization", "i12iz4n", True),
            ("apple", "a2e", False),
            ("apple", "5", True),
            ("apple", "4e", True),
            ("apple", "1pple", True),
            ("internationalization", "20", True),
            ("internationalization", "i18n", True),
            ("apple", "a3e", True),
            ("apple", "ap2e", True),
            ("apple", "01", False),
            ("apple", "a01", False),
            ("a", "1", True),
            ("a", "a", True),
            ("a", "2", False),
            ("hi", "2", True),
            ("hi", "1i", True),
            ("hi", "1", False),
            ("abbreviation", "a10n", True),
            ("abbreviation", "a010n", False),
            ("word", "w2d", True),
            ("word", "wo2", True),
            ("word", "2d", False),
            ("word", "4", True),
            ("word", "3", False),
            ("word", "w1r1", True),
            ("substitution", "s10n", True),
            ("substitution", "sub4u4", True),
            ("substitution", "12", True),
            ("substitution", "s55n", False),
            ("substitution", "s010n", False),
            ("substitution", "su3i1u2on", True),
            ("substitution", "sub5tion", True),
        ],
    )
    def test_valid_word_abbreviation(self, word: str, abbr: str, expected: bool):
        result = run_valid_word_abbreviation(Solution, word, abbr)
        assert_valid_word_abbreviation(result, expected)
