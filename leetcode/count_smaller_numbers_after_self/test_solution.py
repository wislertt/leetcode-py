import pytest

from leetcode_py import logged_test

from .helpers import assert_count_smaller, run_count_smaller
from .solution import Solution


class TestCountSmallerNumbersAfterSelf:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([5, 2, 6, 1], [2, 1, 1, 0]),
            ([-1], [0]),
            ([-1, -1], [0, 0]),
            ([1], [0]),
            ([2, 1], [1, 0]),
            ([1, 2], [0, 0]),
            ([3, 2, 1], [2, 1, 0]),
            ([1, 2, 3], [0, 0, 0]),
            ([2, 0, 1], [2, 0, 0]),
            ([5, 4, 3, 2, 1], [4, 3, 2, 1, 0]),
            ([1, 1, 1], [0, 0, 0]),
            ([-5, -3, -4], [0, 1, 0]),
            ([0, 0, 1, 0], [0, 0, 1, 0]),
            ([7, 3, 7, 3, 7], [2, 0, 1, 0, 0]),
            ([3, 0, -10, 1, 8, 10, -9, -8, -6], [6, 4, 0, 3, 3, 3, 0, 0, 0]),
            ([-6, -2, -7, 6, -10, -8, 6, -4], [3, 4, 2, 3, 0, 0, 1, 0]),
            ([6, -7, 10, -1, 9, 2, -8], [4, 1, 4, 1, 2, 1, 0]),
            ([1, -9, 5, 4, -10, 10, 0, -3, -9], [5, 1, 5, 4, 0, 3, 2, 1, 0]),
            ([-4, 7, -3, -7, -3, -10], [2, 4, 2, 1, 1, 0]),
            ([-5, -6, 9, -7, 1, -10, 1, 1], [3, 2, 5, 1, 1, 0, 0, 0]),
            ([-1, -10, 3, 5, 7, 2, 4, 8, 4], [1, 0, 1, 3, 3, 0, 0, 1, 0]),
            ([-4, -2, -10, -8, 3, -4], [2, 3, 0, 0, 1, 0]),
        ],
    )
    def test_count_smaller(self, nums: list[int], expected: list[int]):
        result = run_count_smaller(Solution, nums)
        assert_count_smaller(result, expected)
