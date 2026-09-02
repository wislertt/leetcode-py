import pytest

from leetcode_py import logged_test

from .helpers import assert_min_difference, run_min_difference
from .solution import Solution


class TestMinimumDifferenceBetweenLargestAndSmallestValueInThreeMoves:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([5, 3, 2, 4], 0),
            ([1, 5, 0, 10, 14], 1),
            ([3, 100, 20], 0),
            ([1], 0),
            ([2], 0),
            ([1, 2], 0),
            ([5, 5], 0),
            ([1, 2, 3], 0),
            ([7, 1, 9], 0),
            ([1, 2, 3, 4], 0),
            ([6, 6, 0, 1, 1, 4], 1),
            ([1, 5, 6, 14, 15], 1),
            ([10, 1, 1, 1, 10], 0),
            ([-1, 3, -1, 8, 5, 4], 2),
            ([-1000000000, 1000000000, 0, 0, 0], 0),
            ([9, 9, 9, 9, 9, 9, 9], 0),
            ([0, 0, 1, 2, 3, 100, 101, 102], 3),
            ([4, 3, 2, 1, 0, -1, -2], 3),
            ([100, -100, 50, -50, 25, -25, 0], 75),
            ([1, 1000000000], 0),
        ],
    )
    def test_min_difference(self, nums: list[int], expected: int):
        result = run_min_difference(Solution, nums)
        assert_min_difference(result, expected)
