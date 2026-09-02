import pytest

from leetcode_py import logged_test

from .helpers import assert_num_of_subarrays, run_num_of_subarrays
from .solution import Solution


class TestNumberOfSubArraysOfSizeKAndAverageGreaterThanOrEqualToThreshold:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, k, threshold, expected",
        [
            [[2, 2, 2, 2, 5, 5, 5, 8], 3, 4, 3],
            [[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5, 6],
            [[1, 1, 1, 1], 1, 1, 4],
            [[1, 1, 1, 1], 4, 1, 1],
            [[1, 1, 1, 1], 4, 2, 0],
            [[4], 1, 4, 1],
            [[4], 1, 5, 0],
            [[2, 2, 2], 3, 2, 1],
            [[0, 10, 0, 10, 0], 2, 5, 4],
            [[10000, 10000, 10000, 10000, 10000], 5, 10000, 1],
            [[9681, 5765, 5388, 8099, 9662, 9261, 5524, 8812, 2781], 6, 6164, 4],
            [[3433, 5652, 4397, 5846, 183, 5997, 7942, 1734, 4017], 3, 5681, 0],
            [[8553, 3271, 3327, 2401, 9591], 2, 3802, 2],
            [[330, 2410, 5935, 1295], 2, 4529, 0],
            [[903, 1018, 5987, 817, 2119, 3590, 3028, 1592], 1, 819, 7],
            [[7473, 1134, 9588, 6964, 410, 2796, 5493, 3610, 4746], 8, 6932, 0],
        ],
    )
    def test_num_of_subarrays(self, arr: list[int], k: int, threshold: int, expected: int):
        result = run_num_of_subarrays(Solution, arr, k, threshold)
        assert_num_of_subarrays(result, expected)
