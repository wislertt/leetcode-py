import pytest

from leetcode_py import logged_test

from .helpers import assert_range_sum_bst, run_range_sum_bst
from .solution import Solution


class TestRangeSumOfBST:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, low, high, expected",
        [
            ([10, 5, 15, 3, 7, None, 18], 7, 15, 32),
            ([10, 5, 15, 3, 7, 13, 18, 1, None, 6], 6, 10, 23),
            ([1], 1, 1, 1),
            ([1], 2, 5, 0),
            ([10, 5, 15], 5, 15, 30),
            ([10, 5, 15], 11, 14, 0),
            ([5, 3, 8, 1, 4, 7, 9], 4, 8, 24),
            ([20, 10, 30, 5, 15, 25, 35], 10, 30, 100),
            ([50, 30, 70, 20, 40, 60, 80], 45, 75, 180),
            ([100], 1, 100000, 100),
            ([2, 1, 3], 1, 3, 6),
            ([10, 5, 15, 3, 7, 13, 18], 6, 14, 30),
        ],
    )
    def test_range_sum_bst(self, root_list: list[int | None], low: int, high: int, expected: int):
        result = run_range_sum_bst(Solution, root_list, low, high)
        assert_range_sum_bst(result, expected)
