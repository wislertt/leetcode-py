import pytest

from leetcode_py import logged_test

from .helpers import assert_binary_searchable_numbers, run_binary_searchable_numbers
from .solution import Solution


class TestBinarySearchableNumbersInAnUnsortedArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([7], 1),
            ([-1, 5, 2], 1),
            ([1, 2, 3, 4, 5], 5),
            ([5, 4, 3, 2, 1], 0),
            ([1], 1),
            ([2, 1], 0),
            ([1, 2], 2),
            ([3, 1, 2], 0),
            ([1, 3, 2], 1),
            ([2, 3, 1], 0),
            ([4, 2, 3, 1], 0),
            ([1, 5, 2, 6, 3, 7], 2),
            ([-3, 0, -1, 4, 2, 9], 2),
            ([100000, -100000], 0),
            ([-100000, 100000], 2),
            ([0, -1, 1], 1),
            ([10, 20, 30, 15, 40], 2),
            ([-6, 5, 1, 3, 6, -3, 2], 1),
            ([3, -1, 0, -4, -5, 6], 1),
            ([-3, -2, 4, 0, 2], 2),
            ([0, -5, -2, 1, 5], 2),
            ([-1], 1),
            ([2, 5, -2, -6, 3], 0),
            ([6, 0, 4, -1, -6, 5], 0),
            ([3, 4, -1, 6], 1),
            ([0, -4, 5, -3, 2, 3], 0),
            ([2, 1, 6, -6, 3], 0),
        ],
    )
    def test_binary_searchable_numbers(self, nums: list[int], expected: int):
        result = run_binary_searchable_numbers(Solution, nums)
        assert_binary_searchable_numbers(result, expected)
