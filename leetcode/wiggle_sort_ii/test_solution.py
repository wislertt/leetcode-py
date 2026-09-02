import pytest

from leetcode_py import logged_test

from .helpers import assert_wiggle_sort, run_wiggle_sort
from .solution import Solution


class TestWiggleSortII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 5, 1, 1, 6, 4], [1, 5, 1, 1, 6, 4]),
            ([1, 3, 2, 2, 3, 1], [1, 3, 2, 2, 3, 1]),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([2, 1], [2, 1]),
            ([1, 1, 2, 2], [1, 1, 2, 2]),
            ([4, 5, 5, 6], [4, 5, 5, 6]),
            ([1, 1, 1, 2, 2], [1, 1, 1, 2, 2]),
            ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
            ([6, 5, 4, 3, 2, 1], [6, 5, 4, 3, 2, 1]),
            ([1, 1, 2, 2, 3, 3], [1, 1, 2, 2, 3, 3]),
            ([9, 1, 8, 2, 7, 3], [9, 1, 8, 2, 7, 3]),
            ([5, 5, 4, 4, 3, 3], [5, 5, 4, 4, 3, 3]),
            ([0, 1, 0, 2, 1, 2], [0, 1, 0, 2, 1, 2]),
            ([22, 27, 30, 22, 15], [22, 27, 30, 22, 15]),
            ([17, 13, 26, 10], [17, 13, 26, 10]),
            ([0, 8, 16, 5], [0, 8, 16, 5]),
            ([11, 28, 11, 4, 20, 22], [11, 28, 11, 4, 20, 22]),
            ([24, 27, 9, 18, 7, 25, 6, 27, 3], [24, 27, 9, 18, 7, 25, 6, 27, 3]),
            ([23, 4, 14, 6, 1, 22, 8, 27, 5, 21], [23, 4, 14, 6, 1, 22, 8, 27, 5, 21]),
        ],
    )
    def test_wiggle_sort(self, nums: list[int], expected: list[int]):
        result = run_wiggle_sort(Solution, nums)
        assert_wiggle_sort(result, expected)
