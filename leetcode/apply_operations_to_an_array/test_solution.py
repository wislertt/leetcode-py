import pytest

from leetcode_py import logged_test

from .helpers import assert_apply_operations, run_apply_operations
from .solution import Solution


class TestApplyOperationsToAnArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 2, 1, 1, 0], [1, 4, 2, 0, 0, 0]),
            ([0, 1], [1, 0]),
            ([1, 1], [2, 0]),
            ([0, 0], [0, 0]),
            ([1, 0], [1, 0]),
            ([2, 2, 2], [4, 2, 0]),
            ([3, 3, 3, 3], [6, 6, 0, 0]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([0, 0, 0, 0], [0, 0, 0, 0]),
            ([847, 847, 0, 0, 378, 378], [1694, 756, 0, 0, 0, 0]),
            ([1000, 1000, 1000, 1000], [2000, 2000, 0, 0]),
            ([5, 0, 5, 0], [5, 5, 0, 0]),
            ([1, 1, 0, 0, 0, 2, 2, 3], [2, 4, 3, 0, 0, 0, 0, 0]),
            ([7, 3, 3, 4, 4, 0, 1, 1, 6], [7, 6, 8, 2, 6, 0, 0, 0, 0]),
            ([3, 1, 4], [3, 1, 4]),
            ([4, 2], [4, 2]),
            ([1, 4], [1, 4]),
            ([2, 3, 3, 4, 4], [2, 6, 8, 0, 0]),
        ],
    )
    def test_apply_operations(self, nums: list[int], expected: list[int]):
        result = run_apply_operations(Solution, nums)
        assert_apply_operations(result, expected)
