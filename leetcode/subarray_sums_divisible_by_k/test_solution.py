import pytest

from leetcode_py import logged_test

from .helpers import assert_subarrays_div_by_k, run_subarrays_div_by_k
from .solution import Solution


class TestSubarraySumsDivisibleByK:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([4, 5, 0, -2, -3, 1], 5, 7),
            ([5], 9, 0),
            ([1, 2, 3], 3, 3),
            ([-1, 2, 9], 2, 2),
            ([0, 0, 0], 2, 6),
            ([1], 2, 0),
            ([2], 2, 1),
            ([1, -1], 2, 1),
            ([4, 5, 0, -2, -3, 1], 3, 6),
            ([2, -2, 2, -2], 2, 10),
            ([7, 4, 5], 3, 1),
            ([1, 2, 3, 4, 5], 7, 2),
        ],
    )
    def test_subarrays_div_by_k(self, nums: list[int], k: int, expected: int):
        result = run_subarrays_div_by_k(Solution, nums, k)
        assert_subarrays_div_by_k(result, expected)
