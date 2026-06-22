import pytest

from leetcode_py import logged_test

from .helpers import assert_find_redundant_connection, run_find_redundant_connection
from .solution import Solution


class TestRedundantConnection:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "edges, expected",
        [
            ([[1, 2], [1, 3], [2, 3]], [2, 3]),
            ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
            ([[1, 2], [2, 3], [1, 3]], [1, 3]),
            ([[1, 2], [2, 3], [3, 4], [2, 4], [1, 5]], [2, 4]),
            ([[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], [1, 5]),
            ([[1, 2], [1, 3], [1, 4], [3, 4], [2, 5]], [3, 4]),
            ([[1, 2], [2, 3], [3, 4], [1, 5], [2, 5]], [2, 5]),
            ([[1, 2], [1, 3], [2, 4], [3, 4]], [3, 4]),
            ([[1, 2], [1, 3], [2, 4], [2, 5], [3, 5]], [3, 5]),
            ([[1, 2], [2, 3], [3, 4], [4, 5], [2, 6], [1, 6]], [1, 6]),
            ([[1, 2], [2, 3], [1, 3], [4, 5], [5, 6], [1, 4]], [1, 3]),
            ([[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], [2, 3]),
        ],
    )
    def test_find_redundant_connection(self, edges: list[list[int]], expected: list[int]):
        result = run_find_redundant_connection(Solution, edges)
        assert_find_redundant_connection(result, expected)
