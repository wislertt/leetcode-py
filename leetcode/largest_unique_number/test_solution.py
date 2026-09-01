import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_unique_number, run_largest_unique_number
from .solution import Solution


class TestLargestUniqueNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([5, 7, 3, 9, 4, 9, 8, 3, 1], 8),
            ([9, 9, 8, 8], -1),
            ([1], 1),
            ([0], 0),
            ([0, 0], -1),
            ([1, 1, 1], -1),
            ([7, 7, 7, 3], 3),
            ([3, 7, 7, 7], 3),
            ([1000, 1000, 999], 999),
            ([1000, 999, 1000], 999),
            ([1000], 1000),
            ([0, 1, 2, 3, 4, 5], 5),
            ([5, 4, 3, 2, 1, 0], 5),
            ([10, 10, 5, 5, 3, 3, 1, 1], -1),
            ([2, 2, 8, 8, 9, 9, 12, 12, 1000], 1000),
            ([6, 6, 4, 4, 4, 2], 2),
            ([999, 999, 1000, 1000, 998, 1, 1], 998),
            ([13, 13, 13, 2, 2, 2, 5], 5),
            ([14, 8, 6, 4, 15, 15, 5], 14),
            ([0, 12, 3, 0, 15, 5, 15, 5, 9, 5, 13, 6], 13),
        ],
    )
    def test_largest_unique_number(self, nums: list[int], expected: int):
        result = run_largest_unique_number(Solution, nums)
        assert_largest_unique_number(result, expected)
