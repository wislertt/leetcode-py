import pytest

from leetcode_py import logged_test

from .helpers import assert_closed_islands, run_closed_islands
from .solution import Solution


class TestNumberOfClosedIslandsTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            (
                [
                    [1, 1, 1, 1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0, 1, 1, 0],
                    [1, 0, 1, 0, 1, 1, 1, 0],
                    [1, 0, 0, 0, 0, 1, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 0],
                ],
                2,
            ),
            ([[0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [0, 1, 1, 1, 0]], 1),
            (
                [
                    [1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [1, 0, 1, 1, 1, 0, 1],
                    [1, 0, 1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1, 0, 1],
                    [1, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1],
                ],
                2,
            ),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 0),
            ([[0, 0], [0, 0]], 0),
            ([[1]], 0),
            ([[0]], 0),
            ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 0),
            ([[1, 1, 0], [1, 0, 1], [0, 1, 1]], 1),
            ([[1, 0], [0, 1]], 0),
            ([[1, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]], 1),
            ([[0, 1, 0], [1, 0, 1], [0, 1, 0]], 1),
            ([[1, 1, 1, 1, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]], 2),
            ([[1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 1, 1]], 0),
            ([[1, 1], [1, 0]], 0),
            (
                [
                    [0, 0, 1, 1],
                    [1, 1, 1, 1],
                    [1, 0, 0, 0],
                    [1, 1, 0, 1],
                    [1, 1, 0, 1],
                    [0, 1, 1, 1],
                ],
                0,
            ),
        ],
    )
    def test_closed_islands(self, grid: list[list[int]], expected: int):
        result = run_closed_islands(Solution, grid)
        assert_closed_islands(result, expected)
