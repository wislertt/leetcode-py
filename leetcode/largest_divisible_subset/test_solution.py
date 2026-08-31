import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_divisible_subset, run_largest_divisible_subset
from .solution import Solution


class TestLargestDivisibleSubset:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3], [1, 2]),
            ([1, 2, 4, 8], [1, 2, 4, 8]),
            ([1], [1]),
            ([5], [5]),
            ([2, 3], [2]),
            ([3, 4, 6, 12], [3, 6, 12]),
            ([1, 2, 4, 8, 16, 32], [1, 2, 4, 8, 16, 32]),
            ([2, 4, 8, 16], [2, 4, 8, 16]),
            ([9, 18, 54, 108, 27], [9, 18, 54, 108]),
            ([1, 3, 9, 27, 81], [1, 3, 9, 27, 81]),
            ([4, 8, 12, 24, 36], [4, 8, 24]),
            ([2, 3, 5, 7, 11, 13], [2]),
            ([1, 2, 3, 4, 6, 8, 12, 24, 36, 72], [1, 2, 4, 8, 24, 72]),
            ([10, 5, 2, 1], [1, 2, 10]),
            ([100, 200, 400, 800, 1600], [100, 200, 400, 800, 1600]),
            ([7, 14, 28, 56, 3, 6, 12, 24], [3, 6, 12, 24]),
            ([2, 3, 4, 9, 27], [3, 9, 27]),
            ([6, 12, 18, 24, 36, 72], [6, 12, 24, 72]),
            ([1, 2, 5, 10, 20, 40], [1, 2, 10, 20, 40]),
            ([8, 16, 32, 3, 6, 12], [3, 6, 12]),
        ],
    )
    def test_largest_divisible_subset(self, nums: list[int], expected: list[int]):
        result = run_largest_divisible_subset(Solution, nums)
        assert_largest_divisible_subset(result, expected)
