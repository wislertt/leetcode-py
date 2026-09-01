import pytest

from leetcode_py import logged_test

from .helpers import assert_get_sum_absolute_differences, run_get_sum_absolute_differences
from .solution import Solution


class TestSumOfAbsoluteDifferencesInASortedArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 3, 5], [4, 3, 5]),
            ([1, 4, 6, 8, 10], [24, 15, 13, 15, 21]),
            ([1, 2], [1, 1]),
            ([1, 1], [0, 0]),
            ([5, 5, 5, 5], [0, 0, 0, 0]),
            ([1, 10000], [9999, 9999]),
            ([9999, 10000], [1, 1]),
            ([1, 1, 1, 2, 2, 3], [4, 4, 4, 4, 4, 8]),
            ([1, 3, 3, 3, 7], [12, 6, 6, 6, 18]),
            ([2, 2, 4, 4, 4, 9], [13, 13, 9, 9, 9, 29]),
            ([10, 20, 30, 40, 50, 60, 70, 80], [280, 220, 180, 160, 160, 180, 220, 280]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [45, 37, 31, 27, 25, 25, 27, 31, 37, 45]),
            ([7, 7, 7, 7, 7, 7, 10000], [9993, 9993, 9993, 9993, 9993, 9993, 59958]),
            ([3, 4, 6, 6, 8, 11, 15, 20, 21, 21], [85, 77, 65, 65, 61, 61, 69, 89, 95, 95]),
            (
                [20, 44, 77, 79, 84, 89, 90, 93, 93, 98],
                [567, 375, 177, 169, 159, 159, 161, 173, 173, 213],
            ),
            ([9, 9, 17, 20, 35, 50, 71, 92], [231, 231, 199, 193, 193, 223, 307, 433]),
            ([48, 52, 78, 83], [69, 61, 61, 71]),
            ([15, 25, 34, 45, 53, 73, 83, 97], [305, 245, 209, 187, 187, 227, 267, 351]),
        ],
    )
    def test_get_sum_absolute_differences(self, nums: list[int], expected: list[int]):
        result = run_get_sum_absolute_differences(Solution, nums)
        assert_get_sum_absolute_differences(result, expected)
