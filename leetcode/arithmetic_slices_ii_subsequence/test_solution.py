import pytest

from leetcode_py import logged_test

from .helpers import assert_number_of_arithmetic_slices, run_number_of_arithmetic_slices
from .solution import Solution


class TestArithmeticSlicesIISubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 4, 6, 8, 10], 7),
            ([7, 7, 7, 7, 7], 16),
            ([1], 0),
            ([1, 2], 0),
            ([1, 2, 3], 1),
            ([1, 2, 4], 0),
            ([0, 0, 0], 1),
            ([1, 1, 2, 3], 2),
            ([1, 3, 5, 7], 3),
            ([2, 2, 3, 4], 2),
            ([1, 2, 1, 2, 4, 1, 5, 10], 1),
            ([5, 4, 3, 2, 1], 7),
            ([1, -1, 1, -1, 1], 1),
            ([0, 2000000000, -294967296], 0),
            ([1, 2, 3, 4, 5, 6, 7], 20),
            ([7, 7, 7, 7], 5),
            ([3, -1, -5, -9], 3),
        ],
    )
    def test_number_of_arithmetic_slices(self, nums: list[int], expected: int):
        result = run_number_of_arithmetic_slices(Solution, nums)
        assert_number_of_arithmetic_slices(result, expected)
