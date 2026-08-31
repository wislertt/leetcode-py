import pytest

from leetcode_py import logged_test

from .helpers import assert_length_of_last_word, run_length_of_last_word
from .solution import Solution


class TestLengthOfLastWord:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("Hello World", 5),
            ("   fly me   to   the moon  ", 4),
            ("luffy is still joyboy", 6),
            ("a", 1),
            ("a ", 1),
            (" a", 1),
            ("day  ", 3),
            ("hello world  ", 5),
            ("  hello   world ", 5),
            ("ab", 2),
            ("a b c", 1),
            ("aaa bb cc", 2),
            ("single", 6),
            ("   lonely   ", 6),
            ("one two three four", 4),
            ("x", 1),
            ("x y z", 1),
            ("leetcode", 8),
        ],
    )
    def test_length_of_last_word(self, s: str, expected: int):
        result = run_length_of_last_word(Solution, s)
        assert_length_of_last_word(result, expected)
