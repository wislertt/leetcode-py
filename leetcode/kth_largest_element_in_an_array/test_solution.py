import pytest

from leetcode_py import logged_test

from .helpers import assert_find_kth_largest, run_find_kth_largest
from .solution import Solution


class TestKthLargestElementInAnArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([3, 2, 1, 5, 6, 4], 2, 5),
            ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
            ([1], 1, 1),
            ([1, 2], 1, 2),
            ([1, 2], 2, 1),
            ([3, 1, 4, 1, 5, 9, 2, 6], 3, 5),
            ([7, 6, 5, 4, 3, 2, 1], 5, 3),
            ([-1, -2, -3], 1, -1),
            ([-1, -2, -3], 3, -3),
            ([1, 1, 1, 1], 2, 1),
            ([5], 1, 5),
            ([3, 2, 3, 1, 2, 4, 5, 5, 6], 1, 6),
            ([3, 2, 3, 1, 2, 4, 5, 5, 6], 9, 1),
            ([99, 99], 1, 99),
        ],
    )
    def test_find_kth_largest(self, nums: list[int], k: int, expected: int):
        result = run_find_kth_largest(Solution, nums, k)
        assert_find_kth_largest(result, expected)
