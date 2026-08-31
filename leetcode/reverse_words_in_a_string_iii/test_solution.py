import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_words, run_reverse_words
from .solution import Solution


class TestReverseWordsInAStringIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("Let's take LeetCode contest", "s'teL ekat edoCteeL tsetnoc"),
            ("Mr Ding", "rM gniD"),
            ("a", "a"),
            ("ab", "ba"),
            ("abc def", "cba fed"),
            ("hello world", "olleh dlrow"),
            ("racecar", "racecar"),
            ("a b c d", "a b c d"),
            ("Python is fun", "nohtyP si nuf"),
            ("x", "x"),
            ("123 456", "321 654"),
            ("Ab! Cd?", "!bA ?dC"),
            ("ab cd ef gh", "ba dc fe hg"),
            ("LeetCode", "edoCteeL"),
        ],
    )
    def test_reverse_words(self, s: str, expected: str):
        result = run_reverse_words(Solution, s)
        assert_reverse_words(result, expected)
