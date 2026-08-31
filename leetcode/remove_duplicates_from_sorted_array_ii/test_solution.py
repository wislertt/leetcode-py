import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_duplicates, run_remove_duplicates
from .solution import Solution


class TestRemoveDuplicatesFromSortedArrayII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 1, 1, 2, 2, 3], (5, [1, 1, 2, 2, 3])),
            ([0, 0, 1, 1, 1, 1, 2, 3, 3], (7, [0, 0, 1, 1, 2, 3, 3])),
            ([1], (1, [1])),
            ([1, 1], (2, [1, 1])),
            ([1, 1, 1], (2, [1, 1])),
            ([1, 2, 3], (3, [1, 2, 3])),
            ([1, 1, 1, 1], (2, [1, 1])),
            ([2, 2, 2, 2, 2], (2, [2, 2])),
            ([1, 2, 2, 2, 3, 3, 3, 3, 4], (6, [1, 2, 2, 3, 3, 4])),
            ([-1, -1, -1, 0, 0, 0, 0, 1], (5, [-1, -1, 0, 0, 1])),
            ([1, 1, 2, 2, 3, 3], (6, [1, 1, 2, 2, 3, 3])),
            ([5, 5, 5, 5, 5, 5, 5], (2, [5, 5])),
            ([1, 2, 3, 4, 5], (5, [1, 2, 3, 4, 5])),
            ([3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 5, 5], (6, [3, 3, 4, 4, 5, 5])),
            ([0, 0, 0, 0, 0], (2, [0, 0])),
            ([-3, -3, -3], (2, [-3, -3])),
            ([1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3], (6, [1, 1, 2, 2, 3, 3])),
            ([7], (1, [7])),
        ],
    )
    def test_remove_duplicates(self, nums: list[int], expected: tuple[int, list[int]]):
        result = run_remove_duplicates(Solution, nums)
        assert_remove_duplicates(result, expected)
