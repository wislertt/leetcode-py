import pytest

from leetcode_py import logged_test

from .helpers import assert_gcd_of_strings, run_gcd_of_strings
from .solution import Solution


class TestGcdOfStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "str1, str2, expected",
        [
            ("ABCABC", "ABC", "ABC"),
            ("ABABAB", "ABAB", "AB"),
            ("LEET", "CODE", ""),
            ("AAAAAB", "AAA", ""),
            ("A", "A", "A"),
            ("A", "B", ""),
            ("AA", "AA", "AA"),
            ("AA", "A", "A"),
            ("ABABABAB", "ABAB", "ABAB"),
            ("ABCABCABC", "ABCABC", "ABC"),
            ("ABCABCABC", "ABC", "ABC"),
            ("ABCDE", "ABCDE", "ABCDE"),
            ("ABABAB", "ABABAB", "ABABAB"),
            ("ABCABCABCABC", "ABCABC", "ABCABC"),
            ("ABCDEF", "ABC", ""),
            ("ABABABAB", "AB", "AB"),
        ],
    )
    def test_gcd_of_strings(self, str1: str, str2: str, expected: str):
        result = run_gcd_of_strings(Solution, str1, str2)
        assert_gcd_of_strings(result, expected)
