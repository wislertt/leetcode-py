import pytest

from leetcode_py import logged_test

from .helpers import assert_divide_array, run_divide_array
from .solution import Solution


class TestDivideArrayIntoArraysWithMaxDifference:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 3, 4, 8, 7, 9, 3, 5, 1], 2, [[1, 1, 3], [3, 4, 5], [7, 8, 9]]),
            ([2, 4, 2, 2, 5, 2], 2, []),
            ([5, 1, 3], 2, []),
            ([10, 1, 11], 10, [[1, 10, 11]]),
            ([10, 1, 12], 10, []),
            ([7, 7, 7], 1, [[7, 7, 7]]),
            ([1, 2, 3, 4, 5, 6], 1, []),
            ([1, 1, 1, 1, 1, 1], 1, [[1, 1, 1], [1, 1, 1]]),
            ([8, 1, 2, 3, 4, 5], 2, []),
            ([1, 2, 3, 4, 5, 9], 3, []),
            ([3, 9, 1, 2, 4, 10], 8, [[1, 2, 3], [4, 9, 10]]),
            ([100000, 1, 99999], 100000, [[1, 99999, 100000]]),
            ([15, 1, 2, 2, 16, 14, 7, 10, 6], 5, [[1, 2, 2], [6, 7, 10], [14, 15, 16]]),
            ([9, 2, 18], 6, []),
            ([1, 8, 20, 18, 4, 19], 9, [[1, 4, 8], [18, 19, 20]]),
            ([8, 2, 19, 9, 6, 8, 17, 10, 11], 4, []),
            ([7, 18, 17, 1, 9, 17], 6, []),
            ([18, 6, 4, 14, 15, 8, 9, 8, 16], 9, [[4, 6, 8], [8, 9, 14], [15, 16, 18]]),
            ([12, 12, 3, 13, 19, 8], 1, []),
            ([9, 16, 9], 4, []),
        ],
    )
    def test_divide_array(self, nums: list[int], k: int, expected: list[list[int]]):
        result = run_divide_array(Solution, nums, k)
        assert_divide_array(result, expected, k)
