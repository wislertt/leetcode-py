import pytest

from leetcode_py import logged_test

from .helpers import assert_find_duplicates, run_find_duplicates
from .solution import Solution


class TestFindAllDuplicatesInAnArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
            ([1, 1, 2], [1]),
            ([1], []),
            ([2, 2], [2]),
            ([1, 2, 3, 4, 5], []),
            ([1, 1], [1]),
            ([5, 4, 3, 2, 1], []),
            ([2, 1, 2, 1], [1, 2]),
            ([3, 1, 2, 3], [3]),
            ([1, 2, 1, 2], [1, 2]),
            ([1, 2, 2, 1], [1, 2]),
            ([4, 1, 3, 4, 2, 2], [2, 4]),
            ([5, 5, 4, 4, 3, 3, 2, 2, 1, 1], [1, 2, 3, 4, 5]),
            ([2, 2, 1], [2]),
            ([1, 3, 2, 3], [3]),
            ([6, 5, 4, 3, 2, 1, 6], [6]),
            ([2, 3, 2, 4, 3], [2, 3]),
            ([1, 4, 4, 1, 2, 3], [1, 4]),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], []),
            ([1, 1, 2, 2, 3, 3, 4, 4], [1, 2, 3, 4]),
        ],
    )
    def test_find_duplicates(self, nums: list[int], expected: list[int]):
        result = run_find_duplicates(Solution, nums)
        assert_find_duplicates(result, expected)
