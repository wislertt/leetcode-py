import pytest

from leetcode_py import logged_test

from .helpers import assert_eventual_safe_nodes, run_eventual_safe_nodes
from .solution import Solution


class TestFindEventualSafeStates:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "graph, expected",
        [
            ([[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6]),
            ([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []], [4]),
            ([[]], [0]),
            ([[0]], []),
            ([[1, 0], [0, 1]], []),
            ([[1], [2], [], [0, 1, 2]], [0, 1, 2, 3]),
            ([[1, 3], [2, 3, 4], [0, 3, 4], [4], []], [3, 4]),
            ([[1], [0]], []),
            ([[1, 2], [2], [0]], []),
            ([[], [1], [2, 0]], [0]),
            ([[1, 2], [3], [3], []], [0, 1, 2, 3]),
            ([[2, 3], [2, 3, 4], [4], [], [0, 1]], [3]),
        ],
    )
    def test_eventual_safe_nodes(self, graph: list[list[int]], expected: list[int]):
        result = run_eventual_safe_nodes(Solution, graph)
        assert_eventual_safe_nodes(result, expected)
