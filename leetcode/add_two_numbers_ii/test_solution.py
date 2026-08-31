import pytest

from leetcode_py import logged_test

from .helpers import assert_add_two_numbers, run_add_two_numbers
from .solution import Solution


class TestAddTwoNumbersII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "l1_vals, l2_vals, expected_vals",
        [
            ([7, 2, 4, 3], [5, 6, 4], [7, 8, 0, 7]),
            ([2, 4, 3], [5, 6, 4], [8, 0, 7]),
            ([0], [0], [0]),
            ([9, 9, 9, 9], [1], [1, 0, 0, 0, 0]),
            ([1], [9], [1, 0]),
            ([5], [5], [1, 0]),
            ([1, 0, 0], [9, 9], [1, 9, 9]),
            ([3, 7, 8], [5, 4, 3], [9, 2, 1]),
            ([9], [9, 9, 9], [1, 0, 0, 8]),
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [6, 6, 6, 6, 6]),
            ([9, 9], [9, 9], [1, 9, 8]),
            ([1, 8, 9], [2, 1], [2, 1, 0]),
            ([0], [9, 9, 9], [9, 9, 9]),
        ],
    )
    def test_add_two_numbers(
        self, l1_vals: list[int], l2_vals: list[int], expected_vals: list[int]
    ):
        result = run_add_two_numbers(Solution, l1_vals, l2_vals)
        assert_add_two_numbers(result, expected_vals)
