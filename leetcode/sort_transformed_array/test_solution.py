import pytest

from leetcode_py import logged_test

from .helpers import assert_sort_transformed_array, run_sort_transformed_array
from .solution import Solution


class TestSortTransformedArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, a, b, c, expected",
        [
            ([-4, -2, 2, 4], 1, 3, 5, [3, 9, 15, 33]),
            ([-4, -2, 2, 4], -1, 3, 5, [-23, -5, 1, 7]),
            ([-4, -2, 2, 4], 0, 3, 5, [-7, -1, 11, 17]),
            ([-4, -2, 2, 4], 0, -3, 5, [-7, -1, 11, 17]),
            ([0], 0, 0, 0, [0]),
            ([0], 1, 1, 1, [1]),
            ([-100, 100], 1, 0, 0, [10000, 10000]),
            ([-100, 100], -1, 0, 0, [-10000, -10000]),
            ([-3, -2, -1], 1, 0, -1, [0, 3, 8]),
            ([1, 2, 3, 4, 5], -2, 1, 3, [-42, -25, -12, -3, 2]),
            ([-5, 0, 5], 2, -4, 6, [6, 36, 76]),
            ([1, 1, 1], 1, 1, 1, [3, 3, 3]),
            ([-10, -5, 0, 5, 10], 1, -2, 1, [1, 16, 36, 81, 121]),
            ([-1, 0, 1], 3, -6, 2, [-1, 2, 11]),
            ([-2, 2], 1, 4, 4, [0, 16]),
            ([1, 3, 5, 7, 9, 11], 0, 0, 2, [2, 2, 2, 2, 2, 2]),
        ],
    )
    def test_sort_transformed_array(
        self, nums: list[int], a: int, b: int, c: int, expected: list[int]
    ):
        result = run_sort_transformed_array(Solution, nums, a, b, c)
        assert_sort_transformed_array(result, expected)
