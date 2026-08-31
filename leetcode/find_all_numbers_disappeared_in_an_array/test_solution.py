import pytest

from leetcode_py import logged_test

from .helpers import assert_find_disappeared_numbers, run_find_disappeared_numbers
from .solution import Solution


class TestFindAllNumbersDisappearedInAnArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
            ([1, 1], [2]),
            ([1], []),
            ([1, 1, 1, 1, 1], [2, 3, 4, 5]),
            ([1, 2, 3], []),
            ([3, 3, 3], [1, 2]),
            ([2, 2], [1]),
            ([1, 1, 1], [2, 3]),
            ([5, 4, 3, 2, 1], []),
            ([1, 1, 2, 2], [3, 4]),
            ([2, 1, 2, 1], [3, 4]),
            ([1, 2, 2, 4], [3]),
            ([4, 4, 4, 4], [1, 2, 3]),
        ],
    )
    def test_find_disappeared_numbers(self, nums: list[int], expected: list[int]):
        result = run_find_disappeared_numbers(Solution, nums)
        assert_find_disappeared_numbers(result, expected)
