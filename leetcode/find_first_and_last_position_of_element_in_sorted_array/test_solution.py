import pytest

from leetcode_py import logged_test

from .helpers import assert_search_range, run_search_range
from .solution import Solution


class TestFindFirstAndLastPositionOfElementInSortedArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([5, 7, 7, 8, 8, 10], 8, [3, 4]),
            ([5, 7, 7, 8, 8, 10], 6, [-1, -1]),
            ([], 0, [-1, -1]),
            ([2, 2], 2, [0, 1]),
            ([1], 1, [0, 0]),
            ([1], 0, [-1, -1]),
            ([1, 2, 3, 4, 5], 3, [2, 2]),
            ([1, 2, 3, 3, 3, 4, 5], 3, [2, 4]),
            ([1, 1, 1, 1, 1], 1, [0, 4]),
            ([1, 2, 3, 4, 5], 6, [-1, -1]),
            ([1, 2, 2, 3, 4, 4, 4, 5], 4, [4, 6]),
            ([5, 7, 7, 8, 8, 10], 5, [0, 0]),
            ([5, 7, 7, 8, 8, 10], 10, [5, 5]),
            ([1, 3], 1, [0, 0]),
            ([1, 3], 3, [1, 1]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, [4, 4]),
            ([2, 2, 2, 2, 2, 2, 2], 2, [0, 6]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 10, [-1, -1]),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1, [0, 0]),
            ([-10, -5, 0, 3, 7], 0, [2, 2]),
        ],
    )
    def test_search_range(self, nums: list[int], target: int, expected: list[int]):
        result = run_search_range(Solution, nums, target)
        assert_search_range(result, expected)
