import pytest

from leetcode_py import logged_test

from .helpers import assert_min_operations, run_min_operations
from .solution import Solution


class TestMinimumNumberOfOperationsToMakeArrayEmpty:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 3, 3, 2, 2, 4, 2, 3, 4], 4),
            ([2, 1, 2, 2, 3, 3], -1),
            ([1, 1], 1),
            ([1, 1, 1], 1),
            ([1, 1, 1, 1], 2),
            ([1, 1, 1, 1, 1], 2),
            ([1, 1, 1, 1, 1, 1], 2),
            ([1, 2], -1),
            ([1, 2, 2], -1),
            ([2, 2, 2], 1),
            ([3, 3, 3, 3, 3, 3, 3, 3, 3, 3], 4),
            ([1, 1, 2, 2, 3, 3, 4, 4], 4),
            ([5, 5, 5, 5, 5, 5, 5], 3),
            ([7, 7, 7, 7, 7], 2),
            ([1, 1, 2, 2, 3, 3, 3, 4, 4, 4], 4),
            ([9, 9, 9, 9, 9, 9, 9, 9], 3),
            ([1, 2, 3, 4, 4], -1),
            ([20, 16, 7, 16, 20, 16, 7, 20, 20], 4),
            ([15, 1, 8, 1, 1, 15, 8, 8], 3),
            ([3, 6, 3, 3, 6, 3, 3], 3),
            ([16, 7, 10, 2, 10, 16, 7, 16, 2], 4),
            ([6, 22, 19, 6, 15, 6, 6, 19, 6, 15, 6, 15, 22, 6], 6),
            ([1, 1, 1, 42, 2, 2, 3, 3], -1),
        ],
    )
    def test_min_operations(self, nums: list[int], expected: int):
        result = run_min_operations(Solution, nums)
        assert_min_operations(result, expected)
