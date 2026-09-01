import pytest

from leetcode_py import logged_test

from .helpers import assert_min_operations, run_min_operations
from .solution import Solution


class TestMinimumOperationsToReduceXToZero:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, x, expected",
        [
            ([1, 1, 4, 2, 3], 5, 2),
            ([5, 6, 7, 8, 9], 4, -1),
            ([3, 2, 20, 1, 1, 3], 10, 5),
            ([1], 1, 1),
            ([1], 2, -1),
            ([1, 1], 2, 2),
            ([5, 2, 3, 1, 1], 5, 1),
            ([3, 2, 20, 1, 1, 3], 11, -1),
            ([5, 6, 7, 8, 9], 39, -1),
            ([5, 6, 7, 8, 9], 35, 5),
            ([5, 6, 7, 8, 9], 100, -1),
            ([1, 1, 1, 1, 1, 1, 1, 1], 4, 4),
            ([2, 3, 1, 1, 4, 5], 5, 1),
            ([10000, 10000, 10000, 10000, 10000], 50000, 5),
            ([10000, 10000, 10000, 10000, 10000], 30000, 3),
            ([10000, 10000, 10000, 10000, 10000], 99999, -1),
            ([4, 3, 2, 1, 5, 6], 12, 3),
            ([10, 1, 1, 1, 10], 12, 3),
            ([8820, 4094, 7834, 6552, 4880, 3661, 3301, 9733], 26800, -1),
            ([5207, 5594, 477, 6924, 7788, 2822, 227, 4692], 9819, -1),
        ],
    )
    def test_min_operations(self, nums: list[int], x: int, expected: int):
        result = run_min_operations(Solution, nums, x)
        assert_min_operations(result, expected)
