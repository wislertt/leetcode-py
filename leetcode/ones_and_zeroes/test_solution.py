import pytest

from leetcode_py import logged_test

from .helpers import assert_find_max_form, run_find_max_form
from .solution import Solution


class TestOnesAndZeroes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "strs, m, n, expected",
        [
            (["10", "0001", "111001", "1", "0"], 5, 3, 4),
            (["10", "0", "1"], 1, 1, 2),
            (["0"], 1, 1, 1),
            (["1"], 1, 1, 1),
            (["11"], 1, 1, 0),
            (["00", "11"], 1, 1, 0),
            (["00", "11"], 2, 2, 2),
            (["10", "0001", "111001", "1", "0"], 1, 1, 2),
            (["10", "0001", "111001", "1", "0"], 3, 4, 3),
            (["111", "1000", "1000", "1000"], 9, 3, 3),
            (["0", "0", "0", "1"], 3, 1, 4),
            (["0", "0", "0", "1"], 2, 1, 3),
            (["001", "010", "100", "111"], 4, 4, 2),
            (["1101", "1010", "1100", "0100", "1001"], 5, 5, 2),
            (["1", "0", "1", "0"], 2, 2, 4),
        ],
    )
    def test_find_max_form(self, strs: list[str], m: int, n: int, expected: int):
        result = run_find_max_form(Solution, strs, m, n)
        assert_find_max_form(result, expected)
