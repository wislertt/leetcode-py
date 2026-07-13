import pytest

from leetcode_py import logged_test

from .helpers import assert_can_partition_k_subsets, run_can_partition_k_subsets
from .solution import Solution


class TestPartitionToKEqualSumSubsets:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([4, 3, 2, 3, 5, 2, 1], 4, True),
            ([1, 2, 3, 4], 3, False),
            ([1, 1, 1, 1], 2, True),
            ([1, 1, 1, 1], 4, True),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, True),
            ([2, 2, 2, 2, 2, 2], 3, True),
            ([1, 2, 3, 4], 2, True),
            ([1, 1], 2, True),
            ([1, 2, 3, 4, 5], 2, False),
            ([10, 10, 10, 7, 7, 7, 7, 7, 7, 6, 6, 6], 3, True),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 1, True),
            ([2, 2, 2, 2, 3, 3, 3, 3], 4, True),
            ([5, 5, 5, 5, 5, 5], 3, True),
            ([4, 5, 9, 3, 10, 2, 1, 1, 1, 1], 4, False),
        ],
    )
    def test_can_partition_k_subsets(self, nums: list[int], k: int, expected: bool):
        result = run_can_partition_k_subsets(Solution, nums, k)
        assert_can_partition_k_subsets(result, expected)
