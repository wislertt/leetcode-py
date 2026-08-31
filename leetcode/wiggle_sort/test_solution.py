import pytest

from leetcode_py import logged_test

from .helpers import assert_wiggle_sort, run_wiggle_sort
from .solution import Solution


class TestWiggleSort:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 5, 2, 1, 6, 4], [3, 5, 2, 1, 6, 4]),
            ([6, 6, 5, 6, 3, 8], [6, 6, 5, 6, 3, 8]),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([2, 1], [2, 1]),
            ([1, 1], [1, 1]),
            ([3, 3, 3, 3], [3, 3, 3, 3]),
            ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
            ([6, 5, 4, 3, 2, 1], [6, 5, 4, 3, 2, 1]),
            ([1, 1, 1, 2, 2, 2], [1, 1, 1, 2, 2, 2]),
            ([5, 5, 4, 4, 3, 3, 2, 2], [5, 5, 4, 4, 3, 3, 2, 2]),
            ([0, 0, 0], [0, 0, 0]),
            ([2, 1, 2, 1, 2, 1], [2, 1, 2, 1, 2, 1]),
            ([10, 1, 9, 2, 8, 3], [10, 1, 9, 2, 8, 3]),
            ([1, 5, 1, 1, 6, 4], [1, 5, 1, 1, 6, 4]),
        ],
    )
    def test_wiggle_sort(self, nums: list[int], expected: list[int]):
        result = run_wiggle_sort(Solution, nums)
        assert_wiggle_sort(result, expected)
