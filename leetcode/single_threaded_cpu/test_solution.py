import pytest

from leetcode_py import logged_test

from .helpers import assert_get_order, run_get_order
from .solution import Solution


class TestTestSingleThreadedCPU:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "tasks, expected",
        [
            ([[1, 2], [2, 4], [3, 2], [4, 1]], [0, 2, 3, 1]),
            ([[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]], [4, 3, 2, 0, 1]),
            ([[1, 1]], [0]),
            ([[5, 1]], [0]),
            ([[1, 1], [2, 1]], [0, 1]),
            ([[1, 5], [2, 2]], [0, 1]),
            ([[1, 3], [2, 1], [3, 1]], [0, 1, 2]),
            ([[1, 2], [1, 2], [1, 2]], [0, 1, 2]),
            ([[1, 100], [2, 1], [3, 1], [4, 1]], [0, 1, 2, 3]),
            ([[5, 2], [5, 1], [5, 3]], [1, 0, 2]),
            ([[1, 5], [5, 1]], [0, 1]),
            ([[1, 10], [2, 5], [3, 1]], [0, 2, 1]),
            ([[1, 1], [1, 1], [1, 1], [1, 1]], [0, 1, 2, 3]),
            ([[10, 1], [1, 10]], [1, 0]),
            ([[100, 1], [1, 100]], [1, 0]),
        ],
    )
    def test_get_order(self, tasks: list[list[int]], expected: list[int]):
        result = run_get_order(Solution, tasks)
        assert_get_order(result, expected)
