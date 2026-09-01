import pytest

from leetcode_py import logged_test

from .helpers import assert_missing_number, run_missing_number
from .solution import Solution


class TestTestMissingNumberInArithmeticProgression:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "solution_class, arr, expected",
        [
            (Solution, [5, 7, 11, 13], 9),
            (Solution, [15, 13, 12], 14),
            (Solution, [1, 3, 5, 9], 7),
            (Solution, [9, 7, 5, 1], 3),
            (Solution, [0, 2, 6, 8, 10], 4),
            (Solution, [10, 8, 4, 2], 6),
            (Solution, [3, 3, 3], 3),
            (Solution, [0, 0, 0], 0),
            (Solution, [100000, 99999, 99997], 99998),
            (Solution, [0, 4, 6], 2),
            (Solution, [7, 14, 28], 21),
            (Solution, [1, 2, 4], 3),
            (Solution, [6, 4, 0], 2),
            (Solution, [2, 4, 8, 10, 12], 6),
            (Solution, [500, 499, 497], 498),
            (Solution, [1, 1, 1, 1], 1),
        ],
    )
    def test_missing_number(self, solution_class, arr: list[int], expected: int):
        result = run_missing_number(solution_class, arr)
        assert_missing_number(result, expected)
