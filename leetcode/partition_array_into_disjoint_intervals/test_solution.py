import pytest

from leetcode_py import logged_test

from .helpers import assert_partition_disjoint, run_partition_disjoint
from .solution import Solution


class TestPartitionArrayIntoDisjointIntervals:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([5, 0, 3, 8, 6], 3),
            ([1, 1, 1, 0, 6, 12], 4),
            ([1, 2], 1),
            ([0, 0], 1),
            ([5, 5, 5, 5], 1),
            ([1, 2, 3, 4, 5], 1),
            ([0, 1000000], 1),
            ([2, 6, 2, 3], 1),
            ([0, 4, 0, 5, 1, 5], 1),
            ([1, 3, 1, 3, 2, 6], 1),
            ([1, 2, 4, 2, 6, 3], 1),
            ([1, 3, 5, 1, 1, 2, 2, 1], 1),
            ([0, 2, 6, 0], 1),
            ([3, 0, 0, 6, 6], 3),
            ([3, 4], 1),
            ([2, 0, 6, 6, 4], 2),
            ([2, 5], 1),
            ([3, 4, 6, 2, 2, 0, 3, 0, 6], 8),
            ([5, 4, 3, 3, 1, 1, 5, 5, 0, 3, 6], 10),
            ([0, 4, 1, 6, 3, 4, 6, 5, 6, 3], 1),
        ],
    )
    def test_partition_disjoint(self, nums: list[int], expected: int):
        result = run_partition_disjoint(Solution, nums)
        assert_partition_disjoint(result, expected)
