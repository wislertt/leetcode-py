import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_subarray, run_shortest_subarray
from .solution import Solution


class TestShortestSubarrayWithSumAtLeastK:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1], 1, 1),
            ([1, 2], 4, -1),
            ([2, -1, 2], 3, 3),
            ([1], 2, -1),
            ([2], 2, 1),
            ([1, 2, 3], 6, 3),
            ([1, 2, 3], 5, 2),
            ([84, -37, 32, 40, 95], 167, 3),
            ([-1, -1, -1], 1, -1),
            ([5, -3, 7], 9, 3),
            ([1, -1, 1, 1], 2, 2),
            ([48, 99, 37, 4, -31], 140, 2),
            ([3, -2, 5], 4, 1),
            ([2, -1, 1, 1], 3, 4),
            ([10, -5, 10], 15, 3),
            ([1, 1, 1, 1], 4, 4),
        ],
    )
    def test_shortest_subarray(self, nums: list[int], k: int, expected: int):
        result = run_shortest_subarray(Solution, nums, k)
        assert_shortest_subarray(result, expected)
