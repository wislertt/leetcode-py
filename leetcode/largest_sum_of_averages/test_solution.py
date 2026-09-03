import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_sum_of_averages, run_largest_sum_of_averages
from .solution import Solution


class TestLargestSumOfAverages:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([9, 1, 2, 3, 9], 3, 20.0),
            ([1, 2, 3, 4, 5, 6, 7], 4, 20.5),
            ([1], 1, 1.0),
            ([9], 1, 9.0),
            ([1, 2], 1, 1.5),
            ([1, 2], 2, 3.0),
            ([1, 2, 3], 3, 6.0),
            ([10, 10, 10, 10], 2, 20.0),
            ([3, 1, 4, 1, 5], 3, 10.0),
            ([100, 1, 100, 1, 100], 2, 150.5),
            ([7, 7, 7, 7, 7], 5, 35.0),
            ([1, 4, 2, 3], 1, 2.5),
            ([9, 1, 2, 3, 9], 1, 4.8),
            ([4, 1, 7, 5, 6, 2, 3], 4, 18.166666666666664),
            ([2, 8, 3, 6, 5, 7], 3, 16.833333333333332),
            ([5, 2, 1], 2, 6.5),
        ],
    )
    def test_largest_sum_of_averages(self, nums: list[int], k: int, expected: float):
        result = run_largest_sum_of_averages(Solution, nums, k)
        assert_largest_sum_of_averages(result, expected)
