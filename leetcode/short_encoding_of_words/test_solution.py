import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_length_encoding, run_minimum_length_encoding
from .solution import Solution


class TestShortEncodingOfWords:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "words, expected",
        [
            (["time", "me", "bell"], 10),
            (["t"], 2),
            (["a", "aa", "aaa"], 4),
            (["time", "time"], 5),
            (["abc", "bcd", "cde"], 12),
            (["abcd", "cd", "bcd"], 5),
            (["p", "grahp", "q"], 8),
            (["abcdef", "bcdef", "cdef", "def", "ef", "f"], 7),
            (["like", "gadgets", "gizmos"], 20),
            (["xy", "yx", "xx"], 9),
            (["aaa", "aa", "a", "aaa"], 4),
            (["m", "msg", "msgood"], 13),
            (["baa", "ca"], 7),
            (["bb"], 3),
            (["bab"], 4),
            (["b", "b", "baa", "aaacc"], 12),
            (["b", "ccaacba", "bbbaa", "ab"], 17),
            (["bbb", "bccaab", "a", "c"], 15),
        ],
    )
    def test_minimum_length_encoding(self, words: list[str], expected: int):
        result = run_minimum_length_encoding(Solution, words)
        assert_minimum_length_encoding(result, expected)
