import pytest

from leetcode_py import logged_test

from .helpers import assert_find_number_of_lis, run_find_number_of_lis
from .solution import Solution


class TestNumberOfLongestIncreasingSubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 3, 5, 4, 7], 2),
            ([2, 2, 2, 2, 2], 5),
            ([1], 1),
            ([1, 2, 3], 1),
            ([3, 2, 1], 3),
            ([1, 2, 4, 3, 5, 4, 7, 2], 3),
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
            ([1, 1, 1, 2, 2, 2, 3, 3, 3], 27),
            ([5, 4, 3, 2, 1], 5),
            ([1, 2, 3, 4, 5], 1),
            ([-1, -2, -3], 3),
            ([0, 0, 0], 3),
            ([1, 3, 2], 2),
            ([2, 1, 3, 2, 1], 3),
            ([7, 7, 7, 7, 7, 7, 7], 7),
        ],
    )
    def test_find_number_of_lis(self, nums: list[int], expected: int):
        result = run_find_number_of_lis(Solution, nums)
        assert_find_number_of_lis(result, expected)
