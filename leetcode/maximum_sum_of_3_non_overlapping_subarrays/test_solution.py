import pytest

from leetcode_py import logged_test

from .helpers import assert_max_sum_of_three_subarrays, run_max_sum_of_three_subarrays
from .solution import Solution


class TestMaximumSumOf3NonOverlappingSubarrays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 2, 1, 2, 6, 7, 5, 1], 2, [0, 3, 5]),
            ([1, 2, 1, 2, 1, 2, 1, 2, 1], 2, [0, 2, 4]),
            ([1, 2, 3], 1, [0, 1, 2]),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], 3, [0, 3, 6]),
            ([1, 1, 1, 1, 1, 1], 2, [0, 2, 4]),
            ([7, 13, 20, 1, 8, 1, 3, 5, 1], 1, [1, 2, 4]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [0, 3, 6]),
            ([4, 5, 10, 3, 2, 20, 1, 8, 9], 2, [1, 4, 7]),
            ([1, 1, 1, 1, 1, 1, 1, 1, 1], 3, [0, 3, 6]),
            ([3, 9, 1, 1, 5, 8, 1, 1, 7, 9], 2, [0, 4, 8]),
            ([1, 1, 1, 1], 1, [0, 1, 2]),
            ([2, 1, 1, 2, 1, 1], 2, [0, 2, 4]),
            ([5, 5, 5, 1, 5, 5, 5, 1, 5], 1, [0, 1, 2]),
            ([2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 4, [0, 4, 8]),
            ([1, 3, 1, 3, 1, 3, 1, 3, 1], 1, [1, 3, 5]),
            ([4, 4, 4, 2, 2, 2, 4, 4, 4], 3, [0, 3, 6]),
        ],
    )
    def test_max_sum_of_three_subarrays(self, nums: list[int], k: int, expected: list[int]):
        result = run_max_sum_of_three_subarrays(Solution, nums, k)
        assert_max_sum_of_three_subarrays(result, expected)
