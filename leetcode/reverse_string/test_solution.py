import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_string, run_reverse_string
from .solution import Solution


class TestReverseString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
            (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
            (["a"], ["a"]),
            (["a", "b"], ["b", "a"]),
            (["a", "b", "c"], ["c", "b", "a"]),
            (["1", "2", "3", "4", "5"], ["5", "4", "3", "2", "1"]),
            (["x"], ["x"]),
            (["A", "B", "C", "D"], ["D", "C", "B", "A"]),
            ([" "], [" "]),
            (["!", "@", "#", "$"], ["$", "#", "@", "!"]),
            (["p", "a", "l", "i", "n"], ["n", "i", "l", "a", "p"]),
            (["z", "y", "x", "w", "v", "u"], ["u", "v", "w", "x", "y", "z"]),
            (["a", "a", "a", "a"], ["a", "a", "a", "a"]),
            (["T", "e", "s", "t"], ["t", "s", "e", "T"]),
            (["1", "2"], ["2", "1"]),
        ],
    )
    def test_reverse_string(self, s: list[str], expected: list[str]):
        result = run_reverse_string(Solution, s)
        assert_reverse_string(result, expected)
