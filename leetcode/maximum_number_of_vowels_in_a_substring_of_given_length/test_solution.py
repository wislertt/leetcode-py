import pytest

from leetcode_py import logged_test

from .helpers import assert_max_vowels, run_max_vowels
from .solution import Solution


class TestMaximumNumberOfVowelsInASubstringOfGivenLength:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("abciiidef", 3, 3),
            ("aeiou", 2, 2),
            ("leetcode", 3, 2),
            ("rhythms", 4, 0),
            ("rhythms", 7, 0),
            ("a", 1, 1),
            ("bcd", 2, 0),
            ("ab", 2, 1),
            ("aaa", 1, 1),
            ("aeiou", 5, 5),
            ("bacdef", 4, 2),
            ("queue", 3, 3),
            ("strength", 6, 1),
            ("evanfdjf", 1, 1),
            ("olyl", 4, 1),
            ("gfgmbvsd", 2, 0),
        ],
    )
    def test_max_vowels(self, s: str, k: int, expected: int):
        result = run_max_vowels(Solution, s, k)
        assert_max_vowels(result, expected)
