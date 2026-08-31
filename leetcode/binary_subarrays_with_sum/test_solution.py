import pytest

from leetcode_py import logged_test

from .helpers import assert_num_subarrays_with_sum, run_num_subarrays_with_sum
from .solution import Solution


class TestBinarySubarraysWithSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, goal, expected",
        [
            ([1, 0, 1, 0, 1], 2, 4),
            ([0, 0, 0, 0, 0], 0, 15),
            ([1], 1, 1),
            ([1], 0, 0),
            ([0], 0, 1),
            ([0, 1], 1, 2),
            ([1, 0], 1, 2),
            ([1, 1], 2, 1),
            ([1, 1], 1, 2),
            ([0, 0], 0, 3),
            ([1, 0, 1], 1, 4),
            ([1, 0, 1, 1], 2, 3),
            ([0, 1, 0, 1, 0], 1, 8),
            ([1, 1, 1, 1], 3, 2),
            ([0, 0, 1, 0, 0, 1], 2, 3),
        ],
    )
    def test_num_subarrays_with_sum(self, nums: list[int], goal: int, expected: int):
        result = run_num_subarrays_with_sum(Solution, nums, goal)
        assert_num_subarrays_with_sum(result, expected)
