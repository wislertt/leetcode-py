import pytest

from leetcode_py import logged_test

from .helpers import assert_get_concatenation, run_get_concatenation
from .solution import Solution


class TestTestConcatenationOfArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
            ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
            ([1], [1, 1]),
            ([5], [5, 5]),
            ([1, 2], [1, 2, 1, 2]),
            ([0, 0, 0], [0, 0, 0, 0, 0, 0]),
            ([10, 20], [10, 20, 10, 20]),
            ([100], [100, 100]),
            ([1, 2, 3], [1, 2, 3, 1, 2, 3]),
            ([9, 8, 7, 6], [9, 8, 7, 6, 9, 8, 7, 6]),
            ([1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]),
            ([50], [50, 50]),
            ([1, 5, 9], [1, 5, 9, 1, 5, 9]),
        ],
    )
    def test_get_concatenation(self, nums: list[int], expected: list[int]):
        result = run_get_concatenation(Solution, nums)
        assert_get_concatenation(result, expected)
