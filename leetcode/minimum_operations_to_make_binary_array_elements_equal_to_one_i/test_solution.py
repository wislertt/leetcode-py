import pytest

from leetcode_py import logged_test

from .helpers import assert_min_operations, run_min_operations
from .solution import Solution


class TestMinimumOperationsToMakeBinaryArrayElementsEqualToOneI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([0, 0, 0], 1),
            ([0, 0, 1], -1),
            ([1, 0, 0], -1),
            ([1, 1, 0], -1),
            ([1, 1, 1], 0),
            ([0, 1, 1, 1], -1),
            ([1, 1, 1, 0], -1),
            ([0, 0, 1, 0, 0], 2),
            ([0, 1, 1, 1, 0], -1),
            ([1, 0, 0, 0, 1], 1),
            ([1, 0, 1, 0, 1], -1),
            ([1, 0, 1, 1, 1], -1),
            ([1, 1, 1, 1, 1], 0),
            ([0, 1, 1, 1, 0, 0], 3),
            ([1, 1, 0, 1, 0, 1], -1),
            ([1, 1, 1, 1, 1, 1, 1], 0),
            ([0, 1, 1, 1, 1, 0, 0, 0], -1),
            ([1, 1, 0, 1, 1, 1, 1, 0], -1),
            ([1, 1, 1, 0, 0, 1, 1, 1], -1),
            ([0, 0, 0, 1, 0, 1, 0, 0, 0], -1),
            ([1, 1, 0, 0, 1, 1, 0, 0, 1], -1),
            ([1, 1, 1, 1, 0, 0, 0, 0, 1], -1),
        ],
    )
    def test_min_operations(self, nums: list[int], expected: int):
        result = run_min_operations(Solution, nums)
        assert_min_operations(result, expected)
