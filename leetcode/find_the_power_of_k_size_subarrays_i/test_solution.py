import pytest

from leetcode_py import logged_test

from .helpers import assert_results_array, run_results_array
from .solution import Solution


class TestFindThePowerOfKSizeSubarraysI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 2, 3, 4, 3, 2, 5], 3, [3, 4, -1, -1, -1]),
            ([2, 2, 2, 2, 2], 4, [-1, -1]),
            ([3, 2, 3, 2, 3, 2], 2, [-1, 3, -1, 3, -1]),
            ([1], 1, [1]),
            ([5], 1, [5]),
            ([1, 2], 1, [1, 2]),
            ([2, 1], 1, [2, 1]),
            ([1, 2, 3, 4], 4, [4]),
            ([1, 2, 3, 5], 4, [-1]),
            ([7, 8, 9, 10, 11], 5, [11]),
            ([1, 3, 5, 7], 2, [-1, -1, -1]),
            ([4, 5, 6, 7, 8], 2, [5, 6, 7, 8]),
            ([10, 11, 12, 13, 14, 15], 3, [12, 13, 14, 15]),
            ([100000, 99999, 100000], 2, [-1, 100000]),
            ([1, 2, 2, 3], 3, [-1, -1]),
            ([3, 4, 5, 1, 2, 3, 4, 5, 6], 4, [-1, -1, -1, 4, 5, 6]),
            ([9, 2, 4, 2, 12, 9, 5], 4, [-1, -1, -1, -1]),
            ([4, 3, 9], 2, [-1, -1]),
            ([6, 17, 14, 11, 20], 3, [-1, -1, -1]),
            ([19, 3, 17], 1, [19, 3, 17]),
            ([17, 5, 20, 1, 9, 20, 13, 4], 5, [-1, -1, -1, -1]),
            ([5, 3, 18, 5], 3, [-1, -1]),
        ],
    )
    def test_results_array(self, nums: list[int], k: int, expected: list[int]):
        result = run_results_array(Solution, nums, k)
        assert_results_array(result, expected)
