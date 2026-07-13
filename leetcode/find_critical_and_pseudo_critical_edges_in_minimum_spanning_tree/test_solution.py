import pytest

from leetcode_py import logged_test

from .helpers import (
    assert_find_critical_and_pseudo_critical_edges,
    run_find_critical_and_pseudo_critical_edges,
)
from .solution import Solution


class TestFindCriticalAndPseudoCriticalEdgesInMinimumSpanningTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, expected",
        [
            (
                5,
                [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]],
                [[0, 1], [2, 3, 4, 5]],
            ),
            (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]], [[], [0, 1, 2, 3]]),
            (2, [[0, 1, 5]], [[0], []]),
            (3, [[0, 1, 1], [1, 2, 1], [0, 2, 1]], [[], [0, 1, 2]]),
            (3, [[0, 1, 1], [1, 2, 2], [0, 2, 2]], [[0], [1, 2]]),
            (4, [[0, 1, 1], [1, 2, 2], [2, 3, 3], [0, 3, 4]], [[0, 1, 2], []]),
            (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 2]], [[0, 1, 2], []]),
            (4, [[0, 1, 1], [1, 2, 2], [2, 3, 1], [0, 3, 2]], [[0, 2], [1, 3]]),
            (5, [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4]], [[0, 1, 2, 3], []]),
            (4, [[0, 1, 1], [1, 2, 1], [0, 2, 1], [2, 3, 2]], [[3], [0, 1, 2]]),
            (3, [[0, 1, 1], [1, 2, 1], [0, 2, 2]], [[0, 1], []]),
            (5, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [3, 4, 1], [0, 4, 1]], [[], [0, 1, 2, 3, 4]]),
        ],
    )
    def test_find_critical_and_pseudo_critical_edges(
        self, n: int, edges: list[list[int]], expected: list[list[int]]
    ):
        result = run_find_critical_and_pseudo_critical_edges(Solution, n, edges)
        assert_find_critical_and_pseudo_critical_edges(result, expected)
