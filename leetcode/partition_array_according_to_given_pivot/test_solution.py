import pytest

from leetcode_py import logged_test

from .helpers import assert_pivot_array, run_pivot_array
from .solution import Solution


class TestTestPartitionArrayAccordingToGivenPivot:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, pivot, expected",
        [
            ([9, 12, 5, 10, 14, 3, 10], 10, [9, 5, 3, 10, 10, 12, 14]),
            ([-3, 4, 3, 2], 2, [-3, 2, 4, 3]),
            ([10], 10, [10]),
            ([1, 1, 1, 1], 1, [1, 1, 1, 1]),
            ([-1, -5, 0, 3, -2], -1, [-5, -2, -1, 0, 3]),
            ([5, 9, 3, 5, 2, 5, 8], 5, [3, 2, 5, 5, 5, 9, 8]),
            ([4, 2, 4, 1, 4, 3], 4, [2, 1, 3, 4, 4, 4]),
            ([1000000, -1000000, 0, 1000000], 0, [-1000000, 0, 1000000, 1000000]),
            ([2, 1, 3, 2, 4, 2], 2, [1, 2, 2, 2, 3, 4]),
            ([7, 7, 7, 1], 7, [1, 7, 7, 7]),
            ([1, 2], 2, [1, 2]),
            ([2, 1], 1, [1, 2]),
            ([-2, 7], 7, [-2, 7]),
            ([0, 4, 8], 4, [0, 4, 8]),
            ([-2], -2, [-2]),
            ([-9, -5, -10, 9], 9, [-9, -5, -10, 9]),
        ],
    )
    def test_pivot_array(self, nums: list[int], pivot: int, expected: list[int]):
        result = run_pivot_array(Solution, nums, pivot)
        assert_pivot_array(result, expected)
