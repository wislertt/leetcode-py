import pytest

from leetcode_py import logged_test

from .helpers import assert_number_of_subarrays, run_number_of_subarrays
from .solution import Solution


class TestCountNumberOfNiceSubarraysTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 1, 2, 1, 1], 3, 2),
            ([2, 4, 6], 1, 0),
            ([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2, 16),
            ([1], 1, 1),
            ([2], 1, 0),
            ([1, 1, 1, 1], 2, 3),
            ([1, 1, 1, 1], 4, 1),
            ([1, 1, 1, 1], 1, 4),
            ([2, 1, 2, 1, 2], 2, 4),
            ([1, 2, 1, 2, 1], 3, 1),
            ([2, 2, 2, 2], 1, 0),
            ([5, 5, 5, 5, 5], 5, 1),
            ([1, 2, 3, 4, 5, 6, 7], 4, 1),
            ([2, 4, 6, 8, 1, 3, 5], 3, 5),
            ([1, 3, 5, 7, 9], 2, 4),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1], 3, 8),
        ],
    )
    def test_number_of_subarrays(self, nums: list[int], k: int, expected: int):
        result = run_number_of_subarrays(Solution, nums, k)
        assert_number_of_subarrays(result, expected)
