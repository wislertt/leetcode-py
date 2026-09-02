import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_monotonic_subarray, run_longest_monotonic_subarray
from .solution import Solution


class TestLongestMonotonicSubarray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 4, 3, 3, 2], 2),
            ([3, 3, 3, 3], 1),
            ([3, 2, 1], 3),
            ([1], 1),
            ([1, 2], 2),
            ([2, 1], 2),
            ([1, 1], 1),
            ([1, 2, 3, 4, 5], 5),
            ([5, 4, 3, 2, 1], 5),
            ([1, 3, 2, 4, 1], 2),
            ([1, 2, 2, 3], 2),
            ([2, 2, 1, 1], 2),
            ([1, 2, 1, 2, 1], 2),
            ([10, 20, 30, 30], 3),
            ([3, 2, 4, 5, 1, 1, 6, 6], 3),
            ([6, 5, 3, 3], 3),
        ],
    )
    def test_longest_monotonic_subarray(self, nums: list[int], expected: int):
        result = run_longest_monotonic_subarray(Solution, nums)
        assert_longest_monotonic_subarray(result, expected)
