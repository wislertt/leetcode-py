import pytest

from leetcode_py import logged_test

from .helpers import assert_employee_free_time, run_employee_free_time
from .solution import Solution


class TestEmployeeFreeTime:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "schedule, expected",
        [
            ([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]], [[3, 4]]),
            ([[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]], [[5, 6], [7, 9]]),
            ([[[1, 2]], [[2, 3]]], []),
            ([[[1, 3]], [[5, 7]]], [[3, 5]]),
            ([[[1, 10]]], []),
            ([[[1, 3]]], []),
            ([[[1, 2], [3, 4]], [[1, 4]]], []),
            ([[[1, 2], [5, 6]], [[1, 2], [5, 6]]], [[2, 5]]),
            ([[[1, 3], [4, 6]], [[2, 5]]], []),
            ([[[1, 4]], [[2, 5]], [[3, 6]]], []),
            ([[[1, 2], [8, 9]], [[3, 4]], [[5, 6]]], [[2, 3], [4, 5], [6, 8]]),
            ([[[1, 5]], [[10, 15]], [[20, 25]]], [[5, 10], [15, 20]]),
            ([[[1, 2], [10, 11]]], [[2, 10]]),
        ],
    )
    def test_employee_free_time(self, schedule: list[list[list[int]]], expected: list[list[int]]):
        result = run_employee_free_time(Solution, schedule)
        assert_employee_free_time(result, expected)
