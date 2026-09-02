import pytest

from leetcode_py import logged_test

from .helpers import assert_most_profitable_path, run_most_profitable_path
from .solution import Solution


class TestMostProfitablePathInATree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "edges, bob, amount, expected",
        [
            ([[0, 1], [1, 2], [1, 3], [3, 4]], 3, [-2, 4, 2, -4, 6], 6),
            ([[0, 1]], 1, [-7280, 2350], -7280),
            ([[0, 1], [1, 2]], 2, [-4, 6, 8], -1),
            ([[0, 1]], 1, [0, 10000], 0),
            ([[0, 1]], 1, [0, -10000], 0),
            ([[0, 1], [0, 2]], 2, [4, -6, 8], 4),
            ([[0, 1], [0, 2]], 1, [4, 6, -8], 4),
            ([[0, 1], [1, 2], [2, 3]], 3, [2, -2, -2, -2], 0),
            ([[0, 1], [1, 2], [1, 3], [2, 4], [2, 5]], 3, [-2, -4, 4, 0, 8, -6], 8),
            ([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [3, 6]], 5, [2, -2, 4, 6, -8, 10, 12], 16),
            ([[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]], 6, [0, 2, -4, 6, -8, 10, -12], 8),
            ([[0, 1], [1, 2], [1, 3], [3, 4]], 4, [-2, 4, 2, -4, 6], 4),
            ([[0, 1], [1, 3], [3, 4], [0, 2]], 4, [-18, 16, -6, -6, -6], -2),
            ([[2, 3], [0, 1], [0, 2]], 2, [0, 14, -2, -8], 14),
            ([[2, 3], [1, 4], [0, 1], [2, 6], [3, 5], [1, 2]], 3, [12, -12, 2, -4, 4, -2, 2], 4),
            ([[0, 2], [0, 5], [1, 3], [0, 4], [0, 1]], 1, [6, 2, 10, 14, 2, -12], 20),
            (
                [[0, 6], [0, 4], [1, 2], [4, 5], [0, 3], [0, 1]],
                4,
                [6, -8, -16, -4, -2, -18, 16],
                22,
            ),
            ([[1, 2], [0, 1]], 1, [2, 8, 12], 14),
            ([[0, 2], [0, 1], [0, 3]], 1, [-10, 8, 12, 2], 2),
            ([[0, 2], [1, 4], [1, 3], [0, 1]], 1, [2, -18, 18, -10, 12], 20),
        ],
    )
    def test_most_profitable_path(
        self, edges: list[list[int]], bob: int, amount: list[int], expected: int
    ):
        result = run_most_profitable_path(Solution, edges, bob, amount)
        assert_most_profitable_path(result, expected)
