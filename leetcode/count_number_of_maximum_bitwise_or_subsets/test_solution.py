import pytest

from leetcode_py import logged_test

from .helpers import assert_count_max_or_subsets, run_count_max_or_subsets
from .solution import Solution


class TestCountNumberOfMaximumBitwiseOrSubsets:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 1], 2),
            ([2, 2, 2], 7),
            ([3, 2, 1, 5], 6),
            ([8, 2], 1),
            ([16, 1, 2, 12, 2], 3),
            ([12, 5, 5, 16, 7, 16, 16, 7], 84),
            ([12, 1, 7, 8], 6),
            ([16], 1),
            ([8], 1),
            ([8, 7, 1, 12, 8], 14),
            ([2], 1),
            ([2, 2, 2, 12, 16, 16, 5, 3], 69),
            ([5, 5, 1], 6),
            ([12, 1, 16, 16], 3),
            ([8, 8, 1], 3),
            ([7], 1),
            ([1, 1, 16, 8, 8, 1], 21),
            ([3, 8, 12, 5, 5, 3, 16, 1], 66),
            ([3, 3], 3),
            ([1, 12, 2, 5], 3),
        ],
    )
    def test_count_max_or_subsets(self, nums: list[int], expected: int):
        result = run_count_max_or_subsets(Solution, nums)
        assert_count_max_or_subsets(result, expected)
