import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_duplicates, run_remove_duplicates
from .solution import Solution


class TestTestRemoveDuplicatesFromSortedArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 1, 2], (2, [1, 2])),
            ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], (5, [0, 1, 2, 3, 4])),
            ([1], (1, [1])),
            ([1, 2, 3], (3, [1, 2, 3])),
            ([1, 1, 1, 1], (1, [1])),
            ([-1, 0, 0, 1, 1, 2], (4, [-1, 0, 1, 2])),
            ([1, 2], (2, [1, 2])),
            ([5, 5, 5], (1, [5])),
            ([0, 0, 0, 0, 0, 0], (1, [0])),
            ([-100, -100, 0, 100, 100], (3, [-100, 0, 100])),
            ([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], (4, [1, 2, 3, 4])),
            ([10], (1, [10])),
        ],
    )
    def test_remove_duplicates(self, nums: list[int], expected: tuple[int, list[int]]):
        result = run_remove_duplicates(Solution, nums)
        assert_remove_duplicates(result, expected)
