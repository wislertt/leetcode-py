import pytest

from leetcode_py import logged_test

from .helpers import assert_prison_after_n_days, run_prison_after_n_days
from .solution import Solution


class TestPrisonCellsAfterNDays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "cells, n, expected",
        [
            ([0, 1, 0, 1, 1, 0, 0, 1], 7, [0, 0, 1, 1, 0, 0, 0, 0]),
            ([1, 0, 0, 1, 0, 0, 1, 0], 1000000000, [0, 0, 1, 1, 1, 1, 1, 0]),
            ([0, 0, 0, 0, 0, 0, 0, 0], 1, [0, 1, 1, 1, 1, 1, 1, 0]),
            ([1, 1, 1, 1, 1, 1, 1, 1], 1, [0, 1, 1, 1, 1, 1, 1, 0]),
            ([0, 1, 1, 0, 1, 1, 0, 0], 1, [0, 0, 0, 1, 0, 0, 0, 0]),
            ([1, 0, 0, 0, 0, 0, 0, 1], 1, [0, 0, 1, 1, 1, 1, 0, 0]),
            ([0, 1, 0, 1, 0, 1, 0, 1], 1, [0, 1, 1, 1, 1, 1, 1, 0]),
            ([0, 1, 1, 1, 1, 1, 1, 0], 2, [0, 0, 0, 1, 1, 0, 0, 0]),
            ([1, 1, 0, 1, 1, 0, 1, 1], 3, [0, 0, 1, 0, 0, 1, 0, 0]),
            ([0, 0, 1, 1, 1, 1, 0, 0], 14, [0, 0, 1, 1, 1, 1, 0, 0]),
            ([1, 0, 1, 0, 1, 0, 1, 0], 6, [0, 1, 1, 0, 0, 1, 1, 0]),
            ([0, 1, 0, 1, 1, 0, 0, 1], 1000000000, [0, 0, 1, 0, 1, 1, 0, 0]),
            ([1, 1, 1, 0, 0, 1, 1, 1], 999999999, [0, 1, 1, 1, 1, 1, 1, 0]),
            ([0, 0, 0, 1, 1, 0, 0, 0], 5, [0, 1, 1, 1, 1, 1, 1, 0]),
            ([1, 0, 0, 1, 1, 0, 0, 1], 4, [0, 0, 0, 1, 1, 0, 0, 0]),
        ],
    )
    def test_prison_after_n_days(self, cells: list[int], n: int, expected: list[int]):
        result = run_prison_after_n_days(Solution, cells, n)
        assert_prison_after_n_days(result, expected)
