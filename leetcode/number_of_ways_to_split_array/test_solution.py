import pytest

from leetcode_py import logged_test

from .helpers import assert_ways_to_split_array, run_ways_to_split_array
from .solution import Solution


class TestNumberOfWaysToSplitArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([10, 4, -8, 7], 2),
            ([2, 3, 1, 0], 2),
            ([1, 1], 1),
            ([0, 0], 1),
            ([-1, 1], 0),
            ([100000, -100000], 1),
            ([-100000, 100000], 0),
            ([0, 5], 0),
            ([5, 0], 1),
            ([3, -1, 2, 1, 4], 1),
            ([-2, -1, -3, 10], 0),
            ([1, 2, 3, 4, 5], 1),
            ([5, 4, 3, 2, 1], 3),
            ([0, 0, 0, 0, 0], 4),
            ([-1, -1, 5, -1, -1], 2),
            ([7, -7, 7, -7, 7, -7], 5),
            ([9, 1, -5, 7, 3, 6], 2),
            ([2, -2, 2, -5, 9, 3, -7, -8, 0, 10], 5),
            ([-8, 2, -7, 9, 5, 10], 0),
            ([-3, 8, -3, 8, -9, 8, 4], 2),
        ],
    )
    def test_ways_to_split_array(self, nums: list[int], expected: int):
        result = run_ways_to_split_array(Solution, nums)
        assert_ways_to_split_array(result, expected)
