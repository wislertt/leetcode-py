import pytest

from leetcode_py import logged_test

from .helpers import assert_constrained_subset_sum, run_constrained_subset_sum
from .solution import Solution


class TestConstrainedSubsequenceSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([10, 2, -10, 5, 20], 2, 37),
            ([-1, -2, -3], 1, -1),
            ([10, -2, -10, -5, 20], 2, 23),
            ([1], 1, 1),
            ([-5], 1, -5),
            ([-1, -2, -3, -4], 2, -1),
            ([5, 5, 5, 5], 1, 20),
            ([1, -1, 1, -1, 1], 2, 3),
            ([100, -1, -1, -1, 100], 2, 199),
            ([100, -1, -1, -1, 100], 4, 200),
            ([-10000, 10000, -10000, 10000], 3, 20000),
            ([3, -2, 5, -1, 4], 2, 12),
            ([1, -5, 2, -5, 3, -5, 4], 2, 10),
            ([8, -4, 6, -4, 10, -20, 5], 3, 29),
            ([-2, -3, 4, -1, -2, 1, 5, -3], 2, 9),
            ([-10, 2, -5, -2, -10, 9], 6, 11),
            ([-5, -7, 4, -6, 0, 4, 0], 1, 4),
            ([-6, -5, 6, 10, -8, 1, -4, 5, 0, -7, 7], 1, 16),
            ([9, -4, -5, 8, 3, -3], 5, 20),
            ([-8, 0, -9, 7, 6, -8, -2, -1, -6, -6, 4, 9], 12, 26),
            ([1, 1, 9], 3, 11),
            ([-3, -5, 1, -3, 7, -5, -2, -5, -8, 4, -3, -9], 11, 12),
            ([1, -10, 2, 2, 1], 4, 6),
            ([-7, -4, 2, 5], 2, 7),
            ([-10, 3, -2, -6, -1, -4], 4, 3),
            ([0, 1, 2], 1, 3),
            ([7, -8], 2, 7),
            ([2], 1, 2),
            ([-9, 1, 9], 1, 10),
            ([-6, 10, -7, -4, 4, 6, -5, -8], 4, 20),
        ],
    )
    def test_constrained_subset_sum(self, nums: list[int], k: int, expected: int):
        result = run_constrained_subset_sum(Solution, nums, k)
        assert_constrained_subset_sum(result, expected)
