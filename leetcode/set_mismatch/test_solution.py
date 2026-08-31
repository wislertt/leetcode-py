import pytest

from leetcode_py import logged_test

from .helpers import assert_find_error_nums, run_find_error_nums
from .solution import Solution


class TestSetMismatch:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 2, 4], [2, 3]),
            ([1, 1], [1, 2]),
            ([1, 2, 3, 4, 3], [3, 5]),
            ([1, 1, 3, 4, 5], [1, 2]),
            ([5, 2, 3, 4, 5], [5, 1]),
            ([1, 4, 3, 4, 5, 6], [4, 2]),
            ([2, 2], [2, 1]),
            ([1, 2, 2], [2, 3]),
            ([1, 2, 3, 1], [1, 4]),
            ([1, 2, 7, 4, 5, 6, 7, 8, 9, 10], [7, 3]),
            ([1, 2, 3, 4, 5, 2, 7], [2, 6]),
            ([1, 2, 3, 4, 8, 6, 7, 8], [8, 5]),
        ],
    )
    def test_find_error_nums(self, nums: list[int], expected: list[int]):
        result = run_find_error_nums(Solution, nums)
        assert_find_error_nums(result, expected)
