import pytest

from leetcode_py import logged_test

from .helpers import assert_equal_substring, run_equal_substring
from .solution import Solution


class TestGetEqualSubstringsWithinBudgetTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, t, max_cost, expected",
        [
            ("abcd", "bcdf", 3, 3),
            ("abcd", "cdef", 3, 1),
            ("abcd", "acde", 0, 1),
            ("abcd", "abcd", 0, 4),
            ("abcd", "abcd", 100, 4),
            ("a", "z", 25, 1),
            ("a", "z", 24, 0),
            ("a", "z", 0, 0),
            ("abcd", "dcba", 6, 3),
            ("abcd", "dcba", 5, 3),
            ("krrgw", "zjzss", 19, 2),
            ("pxezla", "ggjogm", 40, 4),
            ("abcd", "cdef", 100, 4),
            ("abc", "abc", 0, 3),
            ("mtmeielr", "sqwwpkqx", 52, 6),
            ("abcde", "fghij", 50, 5),
        ],
    )
    def test_equal_substring(self, s: str, t: str, max_cost: int, expected: int):
        result = run_equal_substring(Solution, s, t, max_cost)
        assert_equal_substring(result, expected)
