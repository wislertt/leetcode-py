import pytest

from leetcode_py import logged_test

from .helpers import assert_pivot_index, run_pivot_index
from .solution import Solution


class TestFindPivotIndex:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 7, 3, 6, 5, 6], 3),
            ([1, 2, 3], -1),
            ([2, 1, -1], 0),
            ([1], 0),
            ([0], 0),
            ([-1, -1, -1, -1, -1], 2),
            ([1, 0], 0),
            ([0, 0, 0], 0),
            ([-1, 1], -1),
            ([1, -1, 1], 0),
            ([10, 0, 10], 1),
            ([2, 3, 5, 1, 4, 3, 2], -1),
            ([100, -100, 100], 0),
            ([1, 100, 1], 1),
            ([5, 5, 5, 5, 5, 5], -1),
        ],
    )
    def test_pivot_index(self, nums: list[int], expected: int):
        result = run_pivot_index(Solution, nums)
        assert_pivot_index(result, expected)
