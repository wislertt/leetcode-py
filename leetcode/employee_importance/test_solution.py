import pytest

from leetcode_py import logged_test

from .helpers import assert_get_importance, run_get_importance
from .solution import Solution


class TestEmployeeImportance:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "employees, id, expected",
        [
            ([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1, 11),
            ([[1, 2, [5]], [5, -3, []]], 5, -3),
            ([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 2, 3),
            ([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 3, 3),
            ([[1, 2, [5]], [5, -3, []]], 1, -1),
            ([[1, 10, []]], 1, 10),
            ([[1, -1, [2]], [2, -2, []]], 1, -3),
            ([[1, -1, [2]], [2, -2, []]], 2, -2),
            ([[1, 0, [2]], [2, 1, [3]], [3, 2, []]], 1, 3),
            ([[1, 0, [2]], [2, 1, [3]], [3, 2, []]], 2, 3),
            ([[1, 0, [2]], [2, 1, [3]], [3, 2, []]], 3, 2),
            ([[1, 0, [2, 3, 4, 5]], [2, 1, []], [3, 1, []], [4, 1, []], [5, 1, []]], 1, 4),
            ([[1, 0, [2, 3, 4, 5]], [2, 1, []], [3, 1, []], [4, 1, []], [5, 1, []]], 5, 1),
            ([[1, 4, [2]], [2, -6, [3]], [3, 7, []], [9, 100, [10]], [10, -100, []]], 1, 5),
            ([[1, 4, [2]], [2, -6, [3]], [3, 7, []], [9, 100, [10]], [10, -100, []]], 9, 0),
            ([[1, 4, [2]], [2, -6, [3]], [3, 7, []], [9, 100, [10]], [10, -100, []]], 3, 7),
        ],
    )
    def test_get_importance(self, employees: list[list[int | list[int]]], id: int, expected: int):
        result = run_get_importance(Solution, employees, id)
        assert_get_importance(result, expected)
