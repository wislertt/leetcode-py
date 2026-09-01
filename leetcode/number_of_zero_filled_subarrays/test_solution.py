import pytest

from leetcode_py import logged_test

from .helpers import assert_zero_filled_subarray, run_zero_filled_subarray
from .solution import Solution


class TestNumberOfZeroFilledSubarrays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 3, 0, 0, 2, 0, 0, 4], 6),
            ([0, 0, 0, 2, 0, 0], 9),
            ([2, 10, 2019], 0),
            ([0], 1),
            ([1], 0),
            ([0, 0], 3),
            ([0, 0, 0], 6),
            ([0, 0, 0, 0], 10),
            ([0, 1, 0], 2),
            ([1, 0, 1, 0, 1], 2),
            ([-1, 0, -1000000000], 1),
            ([0, 0, 5, 0, 0, 0], 9),
            ([5, 0, 0, 0, 0, 1, 0, 0], 13),
            ([1000000000, 0, -1000000000, 0], 2),
            ([0, 0, 0, 0, 0, 0, 0], 28),
        ],
    )
    def test_zero_filled_subarray(self, nums: list[int], expected: int):
        result = run_zero_filled_subarray(Solution, nums)
        assert_zero_filled_subarray(result, expected)
