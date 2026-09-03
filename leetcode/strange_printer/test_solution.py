import pytest

from leetcode_py import logged_test

from .helpers import assert_strange_printer, run_strange_printer
from .solution import Solution


class TestStrangePrinter:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("aaabbb", 2),
            ("aba", 2),
            ("a", 1),
            ("ab", 2),
            ("abc", 3),
            ("aaa", 1),
            ("aab", 2),
            ("abab", 3),
            ("abcabc", 5),
            ("abcba", 3),
            ("abcbac", 4),
            ("aabbbcc", 3),
            ("abcdefg", 7),
            ("aaabbbccc", 3),
            ("aabbaabb", 3),
            ("aabbccbbaa", 3),
            ("abababab", 5),
            ("zzzzzzzzzz", 1),
            ("abcabcabc", 7),
            ("aabbccddeeff", 6),
            ("ababccbaab", 5),
            ("cbaabcbaabc", 5),
            ("edebddbdaacdae", 8),
            ("ccacbdeedbe", 6),
            ("edddc", 3),
            ("db", 2),
        ],
    )
    def test_strange_printer(self, s: str, expected: int):
        result = run_strange_printer(Solution, s)
        assert_strange_printer(result, expected)
