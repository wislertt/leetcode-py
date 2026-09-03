import pytest

from leetcode_py import logged_test

from .helpers import assert_find_length_of_lcis, run_find_length_of_lcis
from .solution import Solution


class TestLongestContinuousIncreasingSubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 3, 5, 4, 7], 3),
            ([2, 2, 2, 2, 2], 1),
            ([1], 1),
            ([1, 2, 3, 4, 5], 5),
            ([5, 4, 3, 2, 1], 1),
            ([1, 3, 5, 7], 4),
            ([10, 9, 8, 7, 6, 5, 4], 1),
            ([1, 2, 2, 3, 4, 4, 5], 3),
            ([-1, 0, 1, 0, -1, 0, 1, 2], 4),
            ([1000000000, -1000000000, 1000000000], 2),
            ([-1000000000, -999999999, -999999998], 3),
            ([1, 2, 1, 2, 1, 2, 1], 2),
            ([3, 1, 2, 5, 4, 6, 7, 8, 9], 5),
            ([7, 8, 1, 2, 3, 0, 1], 3),
            ([4, 5, 6, 3, 4, 5], 3),
        ],
    )
    def test_find_length_of_lcis(self, nums: list[int], expected: int):
        result = run_find_length_of_lcis(Solution, nums)
        assert_find_length_of_lcis(result, expected)
