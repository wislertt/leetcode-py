import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_bridge, run_shortest_bridge
from .solution import Solution


class TestShortestBridge:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 1], [1, 0]], 1),
            ([[0, 1, 0], [0, 0, 0], [0, 0, 1]], 2),
            (
                [
                    [1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 1, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                ],
                1,
            ),
            ([[1, 0], [0, 1]], 1),
            ([[1, 0, 0], [0, 0, 0], [0, 0, 1]], 3),
            ([[0, 1, 1], [0, 0, 0], [1, 1, 0]], 1),
            ([[1, 1, 0], [0, 0, 0], [0, 1, 1]], 1),
            ([[0, 0, 0], [0, 1, 0], [0, 0, 1]], 1),
            ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 1, 0]], 3),
            (
                [
                    [1, 1, 0, 0, 0],
                    [1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1],
                    [0, 0, 0, 1, 1],
                    [0, 0, 0, 0, 0],
                ],
                4,
            ),
            ([[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]], 3),
            ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 5),
            ([[1, 1, 0, 0], [1, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1]], 3),
        ],
    )
    def test_shortest_bridge(self, grid: list[list[int]], expected: int):
        result = run_shortest_bridge(Solution, grid)
        assert_shortest_bridge(result, expected)
