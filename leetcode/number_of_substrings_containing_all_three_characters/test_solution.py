import pytest

from leetcode_py import logged_test

from .helpers import assert_number_of_substrings, run_number_of_substrings
from .solution import Solution


class TestNumberOfSubstringsContainingAllThreeCharacters:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ["abcabc", 10],
            ["aaacb", 3],
            ["abc", 1],
            ["aaaa", 0],
            ["abca", 3],
            ["cba", 1],
            ["acbbca", 7],
            ["ababcc", 6],
            ["cab", 1],
            ["abcccac", 7],
            ["babca", 5],
            ["cbbbbab", 2],
            ["baccbccc", 10],
            ["acacaabb", 8],
            ["baaabb", 0],
            ["bbcaa", 4],
        ],
    )
    def test_number_of_substrings(self, s: str, expected: int):
        result = run_number_of_substrings(Solution, s)
        assert_number_of_substrings(result, expected)
