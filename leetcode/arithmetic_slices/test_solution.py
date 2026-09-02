import pytest

from leetcode_py import logged_test

from .helpers import assert_number_of_arithmetic_slices, run_number_of_arithmetic_slices
from .solution import Solution


class TestArithmeticSlices:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 4], 3),
            ([1], 0),
            ([1, 2, 3], 1),
            ([1, 2], 0),
            ([1, 3], 0),
            ([-1000, 0, 1000, 2000, 3000], 6),
            ([7, 7, 7, 7], 3),
            ([3, -1, -5, -9], 3),
            ([1, 3, 5, 7, 9], 6),
            ([1, 2, 3, 8, 9, 10], 2),
            ([1, 2, 3, 4, 5, 6], 10),
            ([1, 3, 5, 4, 3, 2, 1], 7),
            ([10, 8, 6, 4, 2, 0, -2], 15),
            ([1, 2, 4, 8, 16], 0),
            ([5, 5, 5, 1, 2, 3, 4], 4),
            ([1, 2, 3, 4, 5, 7, 9, 11], 9),
            ([0, 0, 0, 0, 0], 6),
            ([4, 1, -1, -3, 2, 4, 4, 0, -1], 1),
            ([2, -1, 0, 1, 0, -3, 2, 1], 1),
            ([0, 2, 0, 1, 0, -1], 1),
            ([4, 4, 4, -1, 2, -1], 1),
            ([0, -3, 0, 0, 2, 4, 4, 1, 1], 1),
        ],
    )
    def test_number_of_arithmetic_slices(self, nums: list[int], expected: int):
        result = run_number_of_arithmetic_slices(Solution, nums)
        assert_number_of_arithmetic_slices(result, expected)
