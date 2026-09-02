import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_subarray_length, run_minimum_subarray_length
from .solution import Solution


class TestShortestSubarrayWithORAtLeastKII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 2, 3], 2, 1),
            ([2, 1, 8], 10, 3),
            ([1, 2], 0, 1),
            ([1], 2, -1),
            ([2], 2, 1),
            ([1], 0, 1),
            ([0, 0, 0], 1, -1),
            ([1, 4, 2, 8], 15, 4),
            ([5, 2, 3], 6, 2),
            ([8, 1, 1, 8], 9, 2),
            ([4, 4, 3], 7, 2),
            ([1000000000, 1000000000], 1000000000, 1),
            ([1, 2, 4, 8, 16], 31, 5),
            ([3, 3, 3, 3], 2, 1),
            ([16, 1, 2, 4], 23, 4),
            ([0, 1, 0], 1, 1),
        ],
    )
    def test_minimum_subarray_length(self, nums: list[int], k: int, expected: int):
        result = run_minimum_subarray_length(Solution, nums, k)
        assert_minimum_subarray_length(result, expected)
