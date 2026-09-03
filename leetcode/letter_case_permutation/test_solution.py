import pytest

from leetcode_py import logged_test

from .helpers import assert_letter_case_permutation, run_letter_case_permutation
from .solution import Solution


class TestLetterCasePermutation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("a1b2", ["A1B2", "A1b2", "a1B2", "a1b2"]),
            ("3z4", ["3Z4", "3z4"]),
            ("a", ["A", "a"]),
            ("C", ["C", "c"]),
            ("7", ["7"]),
            ("123", ["123"]),
            ("a1", ["A1", "a1"]),
            ("ab", ["AB", "Ab", "aB", "ab"]),
            ("aB", ["AB", "Ab", "aB", "ab"]),
            ("zZ", ["ZZ", "Zz", "zZ", "zz"]),
            ("abc", ["ABC", "ABc", "AbC", "Abc", "aBC", "aBc", "abC", "abc"]),
            ("Ab3", ["AB3", "Ab3", "aB3", "ab3"]),
            ("1a2b", ["1A2B", "1A2b", "1a2B", "1a2b"]),
            ("xy", ["XY", "Xy", "xY", "xy"]),
            ("q9r", ["Q9R", "Q9r", "q9R", "q9r"]),
            ("m0n0", ["M0N0", "M0n0", "m0N0", "m0n0"]),
            ("Zz9", ["ZZ9", "Zz9", "zZ9", "zz9"]),
            ("A1b2C", ["A1B2C", "A1B2c", "A1b2C", "A1b2c", "a1B2C", "a1B2c", "a1b2C", "a1b2c"]),
        ],
    )
    def test_letter_case_permutation(self, s: str, expected: list[str]):
        result = run_letter_case_permutation(Solution, s)
        assert_letter_case_permutation(result, expected)
