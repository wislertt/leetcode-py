import pytest

from leetcode_py import logged_test

from .helpers import assert_min_operations, run_min_operations
from .solution import Solution


class TestMinimumNumberOfOperationsToMakeArrayContinuous:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 2, 5, 3], 0),
            ([1, 2, 3, 5, 6], 1),
            ([1, 10, 100, 1000], 3),
            ([1], 0),
            ([1, 1], 1),
            ([2, 2], 1),
            ([1, 3, 1], 1),
            ([8, 5, 6, 7, 5, 6], 2),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0),
            ([10, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0),
            ([1, 1, 1, 1], 3),
            ([5, 4, 3, 2, 1, 1], 1),
            ([9, 9, 9, 1, 2, 3], 3),
            ([1, 5, 10, 15, 20], 3),
            ([1000000000, 1, 2, 3], 1),
            ([7, 8, 9, 10, 11, 3, 4, 5], 1),
            ([11, 13, 11, 10, 3], 2),
            ([1, 12, 12, 6, 3, 14, 5], 3),
        ],
    )
    def test_min_operations(self, nums: list[int], expected: int):
        result = run_min_operations(Solution, nums)
        assert_min_operations(result, expected)
