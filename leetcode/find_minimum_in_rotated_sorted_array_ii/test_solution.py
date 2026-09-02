import pytest

from leetcode_py import logged_test

from .helpers import assert_find_min, run_find_min
from .solution import Solution


class TestFindMinimumInRotatedSortedArrayII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 3, 5], 1),
            ([2, 2, 2, 0, 1], 0),
            ([0, 1, 4, 4, 5, 6, 7], 0),
            ([4, 5, 6, 7, 0, 1, 4], 0),
            ([1], 1),
            ([3, 1, 1], 1),
            ([2, 2, 2], 2),
            ([1, 1, 1, 1], 1),
            ([1, 1, 2, 2, 3, 3], 1),
            ([3, 3, 1, 3], 1),
            ([10, 1, 10, 10, 10], 1),
            ([5, 5, 5, 1, 2, 3, 4, 5], 1),
            ([2, 2, 2, 0, 0, 1, 2], 0),
            ([4, 4, 4, 4, 4, 4, 0, 0, 4], 0),
            ([-3, -3, -7, -3], -7),
            ([-5000, 5000, 5000], -5000),
            ([5000, -5000, -5000, 5000], -5000),
            ([1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], 0),
            ([3, -2, 1, 2, 2], -2),
            ([5, -5, -1, 1, 1, 2, 3, 4, 5], -5),
        ],
    )
    def test_find_min(self, nums: list[int], expected: int):
        result = run_find_min(Solution, nums)
        assert_find_min(result, expected)
