import pytest

from leetcode_py import logged_test

from .helpers import assert_smallest_range_i, run_smallest_range_i
from .solution import Solution


class TestSmallestRangeI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1], 0, 0),
            ([0, 10], 2, 6),
            ([1, 3, 6], 3, 0),
            ([0, 10], 5, 0),
            ([1], 10000, 0),
            ([0], 0, 0),
            ([2, 7, 2], 1, 3),
            ([1, 5, 9], 2, 4),
            ([3, 1, 10], 4, 1),
            ([10, 0, 5, 5], 0, 10),
            ([0, 10000], 10000, 0),
            ([0, 10000], 9999, 0),
            ([5000, 5000, 5000], 7, 0),
            ([9, 1, 4, 4, 7], 3, 2),
            ([0, 6, 2, 12, 0, 4], 6, 0),
            ([5, 11, 10, 7, 4, 10], 1, 5),
        ],
    )
    def test_smallest_range_i(self, nums: list[int], k: int, expected: int):
        result = run_smallest_range_i(Solution, nums, k)
        assert_smallest_range_i(result, expected)
