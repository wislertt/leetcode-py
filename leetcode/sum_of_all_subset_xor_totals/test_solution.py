import pytest

from leetcode_py import logged_test

from .helpers import assert_subset_xor_sum, run_subset_xor_sum
from .solution import Solution


class TestTestSumOfAllSubsetXORTotals:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 3], 6),
            ([5, 1, 6], 28),
            ([3, 4, 5, 6, 7, 8], 480),
            ([1], 1),
            ([5], 5),
            ([1, 2], 6),
            ([2, 2], 4),
            ([1, 1], 2),
            ([10], 10),
            ([1, 2, 3], 12),
            ([1, 2, 3, 4], 56),
            ([8, 8, 8], 32),
            ([20], 20),
            ([1, 2, 4, 8], 120),
            ([7, 7, 7, 7], 56),
        ],
    )
    def test_subset_xor_sum(self, nums: list[int], expected: int):
        result = run_subset_xor_sum(Solution, nums)
        assert_subset_xor_sum(result, expected)
