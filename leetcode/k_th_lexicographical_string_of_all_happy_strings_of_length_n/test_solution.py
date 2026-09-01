import pytest

from leetcode_py import logged_test

from .helpers import assert_get_happy_string, run_get_happy_string
from .solution import Solution


class TestKThLexicographicalStringOfAllHappyStringsOfLengthN:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, expected",
        [
            (1, 3, "c"),
            (1, 4, ""),
            (3, 9, "cab"),
            (1, 1, "a"),
            (1, 2, "b"),
            (2, 1, "ab"),
            (2, 6, "cb"),
            (2, 7, ""),
            (3, 1, "aba"),
            (3, 12, "cbc"),
            (3, 13, ""),
            (4, 1, "abab"),
            (4, 24, "cbcb"),
            (4, 25, ""),
            (5, 48, "cbcbc"),
            (5, 49, ""),
            (6, 96, "cbcbcb"),
            (6, 97, ""),
            (6, 100, ""),
            (10, 1, "ababababab"),
            (10, 100, "abacbabacb"),
            (10, 3, "ababababca"),
            (7, 64, "acbcbcb"),
            (8, 100, "acbabacb"),
            (9, 50, "abacbabac"),
            (2, 3, "ba"),
            (2, 4, "bc"),
            (5, 1, "ababa"),
            (3, 5, "bab"),
            (3, 8, "bcb"),
        ],
    )
    def test_get_happy_string(self, n: int, k: int, expected: str):
        result = run_get_happy_string(Solution, n, k)
        assert_get_happy_string(result, expected)
