import pytest

from leetcode_py import logged_test

from .helpers import assert_str_str, run_str_str
from .solution import Solution


class TestFindIndexOfFirstOccurrenceInString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "haystack, needle, expected",
        [
            ("sadbutsad", "sad", 0),
            ("leetcode", "leeto", -1),
            ("hello", "ll", 2),
            ("aaaaa", "bba", -1),
            ("a", "a", 0),
            ("abc", "c", 2),
            ("abc", "abc", 0),
            ("abcd", "cd", 2),
            ("mississippi", "issip", 4),
            ("mississippi", "issipi", -1),
            ("aaabaaab", "abaa", 2),
            ("abcdefg", "defg", 3),
            ("baab", "ab", 2),
            ("xxxxxyz", "xyz", 4),
            ("mississippi", "sippi", 6),
            ("abc", "abcd", -1),
            ("aaa", "aaaa", -1),
            ("pitipity", "ity", 5),
        ],
    )
    def test_str_str(self, haystack: str, needle: str, expected: int):
        result = run_str_str(Solution, haystack, needle)
        assert_str_str(result, expected)
