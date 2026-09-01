import pytest

from leetcode_py import logged_test

from .helpers import assert_count_fair_pairs, run_count_fair_pairs
from .solution import Solution


class TestCountTheNumberOfFairPairs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, lower, upper, expected",
        [
            ([0, 1, 7, 4, 4, 5], 3, 6, 6),
            ([1, 7, 9, 2, 5], 11, 11, 1),
            ([0, 0, 0, 0], 0, 0, 6),
            ([1], 0, 0, 0),
            ([1, 2], 3, 3, 1),
            ([1, 2], 4, 10, 0),
            ([-5, 5, -5, 5], 0, 0, 4),
            ([-1000000000, 1000000000], 0, 0, 1),
            ([-500000000, -500000000], -1000000000, -1000000000, 1),
            ([1, 2, 3, 4, 5], 4, 7, 7),
            ([5, 4, 3, 2, 1], 4, 7, 7),
            ([2, 2, 2, 2, 2], 4, 4, 10),
            ([1000000000, 999999999, -1000000000], -1000000000, 0, 2),
            ([7, 1, 7, 1, 7], 8, 14, 9),
            ([-3, -1, 0, 2, 4], -1, 3, 6),
            ([0, 1, 2, 3, 4, 5, 6, 7], 5, 9, 16),
            ([3, -6, -6], 14, 24, 0),
            ([0, -9, -3, -2, -5, -5, 3, 10, 1], -5, 5, 19),
            ([-1, 6, -10, -1, 1, 1], -1, 1, 4),
            ([-3, 1, 0, 1, 5, -9, -10, 8, 3], 14, 17, 0),
        ],
    )
    def test_count_fair_pairs(self, nums: list[int], lower: int, upper: int, expected: int):
        result = run_count_fair_pairs(Solution, nums, lower, upper)
        assert_count_fair_pairs(result, expected)
