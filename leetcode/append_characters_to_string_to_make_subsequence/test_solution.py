import pytest

from leetcode_py import logged_test

from .helpers import assert_append_characters, run_append_characters
from .solution import Solution


class TestAppendCharactersToStringToMakeSubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, t, expected",
        [
            ("coaching", "coding", 4),
            ("abcde", "a", 0),
            ("z", "abcde", 5),
            ("a", "a", 0),
            ("a", "b", 1),
            ("ab", "ba", 1),
            ("abc", "abc", 0),
            ("abc", "cba", 2),
            ("xyz", "xyzxyz", 3),
            ("aaabbbccc", "abc", 0),
            ("abababab", "abba", 0),
            ("leetcode", "code", 0),
            ("lbg", "z", 1),
            ("vwxyz", "abcdef", 6),
            ("vwy", "vwxyz", 3),
            ("hijheklmn", "hello", 2),
            ("qfkcrzrsse", "fhd", 2),
            ("blyfmqunh", "yaxgjcbpzo", 9),
            ("rc", "jkqasuwv", 8),
            ("bgsojfwexbee", "qpfbrpgy", 8),
            ("eopuaqik", "afmf", 3),
            ("dtqaqyrja", "zhunvulgnp", 10),
        ],
    )
    def test_append_characters(self, s: str, t: str, expected: int):
        result = run_append_characters(Solution, s, t)
        assert_append_characters(result, expected)
