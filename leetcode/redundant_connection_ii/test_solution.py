import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_find_redundant_directed_connection,
    run_find_redundant_directed_connection,
)
from .solution import Solution


class TestRedundantConnectionII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "edges, expected",
        [
            ([[1, 2], [1, 3], [2, 3]], [2, 3]),
            ([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]], [4, 1]),
            ([[2, 1], [3, 1], [1, 4], [4, 3]], [3, 1]),
            ([[1, 4], [4, 2], [4, 3], [3, 2]], [3, 2]),
            ([[1, 2], [2, 3], [3, 4], [4, 1]], [4, 1]),
            ([[1, 2], [1, 3], [2, 4], [3, 4]], [3, 4]),
            ([[1, 3], [3, 4], [4, 2], [2, 3]], [2, 3]),
            ([[4, 2], [1, 2], [2, 3], [3, 4]], [4, 2]),
            ([[2, 1], [1, 3], [3, 1]], [3, 1]),
            ([[3, 2], [3, 1], [1, 2]], [1, 2]),
            ([[1, 3], [3, 2], [2, 1]], [2, 1]),
            ([[1, 3], [3, 4], [2, 3], [3, 2]], [2, 3]),
            ([[1, 4], [4, 3], [1, 3], [3, 2]], [1, 3]),
            ([[2, 3], [2, 1], [3, 4], [3, 2]], [3, 2]),
            ([[4, 2], [4, 3], [5, 1], [2, 4], [5, 4]], [2, 4]),
            ([[4, 5], [4, 3], [4, 2], [5, 1], [2, 3]], [2, 3]),
            ([[4, 2], [4, 1], [5, 3], [2, 5], [2, 4]], [2, 4]),
            ([[6, 4], [1, 2], [6, 3], [2, 1], [1, 5], [6, 2]], [1, 2]),
            ([[1, 4], [6, 2], [3, 6], [1, 3], [1, 6], [4, 5]], [1, 6]),
            ([[3, 4], [4, 5], [3, 7], [2, 1], [7, 6], [1, 3], [5, 2]], [5, 2]),
        ],
    )
    def test_find_redundant_directed_connection(self, edges: list[list[int]], expected: list[int]):
        result = run_find_redundant_directed_connection(Solution, edges)
        assert_find_redundant_directed_connection(result, expected)
