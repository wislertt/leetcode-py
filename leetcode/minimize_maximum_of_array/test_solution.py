import pytest

from leetcode_py import logged_test

from .helpers import assert_minimize_array_value, run_minimize_array_value
from .solution import Solution


class TestMinimizeMaximumOfArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 7, 1, 6], 5),
            ([10, 1], 10),
            ([4, 4, 4], 4),
            ([0, 0, 0], 0),
            ([1, 0], 1),
            ([0, 5], 3),
            ([5, 1, 1, 1], 5),
            ([6, 0, 8, 2, 1, 5], 6),
            ([13, 0], 13),
            ([20, 3, 4, 2, 11], 20),
            ([9, 9, 1, 1, 1, 1, 1], 9),
            ([1000000000, 0, 0], 1000000000),
            ([1, 1000000000], 500000001),
            ([2, 1, 2, 1, 2], 2),
            ([10, 10], 10),
            ([0, 3, 11, 9, 5, 5], 6),
            ([6, 3], 6),
            ([9, 12, 10, 12, 8], 11),
        ],
    )
    def test_minimize_array_value(self, nums: list[int], expected: int):
        result = run_minimize_array_value(Solution, nums)
        assert_minimize_array_value(result, expected)
