import pytest

from leetcode_py import logged_test

from .helpers import assert_subarrays_with_k_distinct, run_subarrays_with_k_distinct
from .solution import Solution


class TestSubarraysWithKDifferentIntegers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 2, 1, 2, 3], 2, 7),
            ([1, 2, 1, 3, 4], 3, 3),
            ([1, 1, 1], 1, 6),
            ([1, 2, 3], 1, 3),
            ([1, 2, 3], 3, 1),
            ([1], 1, 1),
            ([1, 2], 2, 1),
            ([1, 2], 1, 2),
            ([2, 1, 2, 1, 2], 1, 5),
            ([1, 2, 1, 1, 2], 2, 9),
            ([4, 4, 4, 4], 1, 10),
            ([1, 3, 2, 1, 3], 2, 4),
        ],
    )
    def test_subarrays_with_k_distinct(self, nums: list[int], k: int, expected: int):
        result = run_subarrays_with_k_distinct(Solution, nums, k)
        assert_subarrays_with_k_distinct(result, expected)
