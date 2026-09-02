import pytest

from leetcode_py import logged_test

from .helpers import assert_max_frequency, run_max_frequency
from .solution import Solution


class TestMaximumFrequencyAfterSubarrayOperation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 2, 3, 4, 5, 6], 1, 2),
            ([10, 2, 3, 4, 5, 5, 4, 3, 2, 2], 10, 4),
            ([1], 1, 1),
            ([7], 3, 1),
            ([5, 5, 5], 5, 3),
            ([1, 2, 3], 1, 2),
            ([3, 2, 1], 1, 2),
            ([2, 2, 2, 2], 3, 4),
            ([50, 1, 50, 1], 1, 3),
            ([4, 4, 9, 4, 9], 4, 4),
            ([6, 6, 6, 1], 6, 4),
            ([10, 20, 30, 40], 30, 2),
            ([2, 3, 4, 5, 2, 3], 3, 3),
            ([1, 1, 50, 1, 50, 1], 50, 4),
            ([10, 10, 7, 5, 1, 3], 8, 2),
            ([12, 6, 11, 9, 7, 8, 2, 2], 8, 3),
            ([7, 4, 3, 9, 11, 6, 6], 6, 3),
            ([1, 6, 12, 12, 7, 10, 4, 12], 11, 3),
        ],
    )
    def test_max_frequency(self, nums: list[int], k: int, expected: int):
        result = run_max_frequency(Solution, nums, k)
        assert_max_frequency(result, expected)
