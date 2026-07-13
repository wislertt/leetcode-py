import pytest

from leetcode_py import logged_test

from .helpers import assert_smallest_range, run_smallest_range
from .solution import Solution


class TestSmallestRangeCoveringElementsFromKLists:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([[4, 10, 15, 24, 26], [0, 9, 12, 20], [5, 18, 22, 30]], [20, 24]),
            ([[1, 2, 3], [1, 2, 3], [1, 2, 3]], [1, 1]),
            ([[1]], [1, 1]),
            ([[1], [2], [3]], [1, 3]),
            ([[1], [1], [1]], [1, 1]),
            ([[1, 5], [2, 6]], [1, 2]),
            ([[10], [20], [30]], [10, 30]),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [3, 7]),
            ([[1], [2], [3], [4]], [1, 4]),
            ([[5]], [5, 5]),
            ([[1, 2], [3, 4]], [2, 3]),
            ([[-10, -5], [0, 5]], [-5, 0]),
            ([[1, 5, 10], [2, 6, 9], [3, 7, 8]], [1, 3]),
            ([[10, 20], [15, 25]], [10, 15]),
            ([[1, 9], [2, 8]], [1, 2]),
        ],
    )
    def test_smallest_range(self, nums: list[list[int]], expected: list[int]):
        result = run_smallest_range(Solution, nums)
        assert_smallest_range(result, expected)
