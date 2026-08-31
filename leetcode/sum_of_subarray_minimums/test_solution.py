import pytest

from leetcode_py import logged_test

from .helpers import assert_sum_subarray_mins, run_sum_subarray_mins
from .solution import Solution


class TestSumOfSubarrayMinimums:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([3, 1, 2, 4], 17),
            ([50], 50),
            ([1], 1),
            ([2, 1], 4),
            ([1, 2], 4),
            ([3, 3, 3], 18),
            ([11, 81, 94, 43, 78], 647),
            ([1, 2, 3], 10),
            ([3, 2, 1], 10),
            ([2, 2, 1, 2, 2], 21),
            ([10000, 10000], 30000),
            ([1, 30000, 1], 30005),
            ([4, 3, 2, 1, 5], 29),
            ([5, 1, 2, 3, 4], 29),
            ([7, 7, 7, 7, 7, 7, 7], 196),
            ([20000, 1, 20000, 1, 20000], 60012),
            ([2, 5, 3, 1, 4], 29),
            ([9], 9),
        ],
    )
    def test_sum_subarray_mins(self, arr: list[int], expected: int):
        result = run_sum_subarray_mins(Solution, arr)
        assert_sum_subarray_mins(result, expected)
