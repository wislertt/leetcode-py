import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_vowels, run_reverse_vowels
from .solution import Solution


class TestReverseVowelsOfAString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("IceCreAm", "AceCreIm"),
            ("leetcode", "leotcede"),
            ("a", "a"),
            ("A", "A"),
            ("z", "z"),
            ("ab", "ab"),
            ("hello", "holle"),
            ("aA", "Aa"),
            ("bcdfg", "bcdfg"),
            ("aeiou", "uoiea"),
            ("AEIOU", "UOIEA"),
            ("a.b!c?d", "a.b!c?d"),
            ("!,a?", "!,a?"),
            ("a!b@c#e", "e!b@c#a"),
            ("Queueing", "Qieueung"),
            ("Rhythm", "Rhythm"),
            ("Kav0nyVtKYLgR", "Kav0nyVtKYLgR"),
            ("lRa", "lRa"),
        ],
    )
    def test_reverse_vowels(self, s: str, expected: str):
        result = run_reverse_vowels(Solution, s)
        assert_reverse_vowels(result, expected)
