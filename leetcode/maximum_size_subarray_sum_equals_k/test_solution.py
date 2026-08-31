import pytest

from leetcode_py import logged_test

from .helpers import assert_max_sub_array_len, run_max_sub_array_len
from .solution import Solution


class TestMaximumSizeSubarraySumEqualsK:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, -1, 5, -2, 3], 3, 4),
            ([-2, -1, 2, 1], 1, 2),
            ([1, 0, 0, 0], 1, 4),
            ([1], 1, 1),
            ([1], 2, 0),
            ([0, 0, 0], 0, 3),
            ([-1, -1, -1], -3, 3),
            ([1, 2, 3, 4, 5], 15, 5),
            ([1, 2, 3, 4, 5], 9, 3),
            ([3, 4, 7, 2, -3, 1, 4, 2], 7, 4),
            ([1, -1, 1, -1], 0, 4),
            ([5], 5, 1),
            ([2, 2, 2], 4, 2),
            ([-5, 5], 0, 2),
            ([10, -10, 10, -10], 0, 4),
        ],
    )
    def test_max_sub_array_len(self, nums: list[int], k: int, expected: int):
        result = run_max_sub_array_len(Solution, nums, k)
        assert_max_sub_array_len(result, expected)
