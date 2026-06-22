import pytest

from leetcode_py import logged_test

from .helpers import assert_max_area_of_island, run_max_area_of_island
from .solution import Solution


class TestMaxAreaOfIsland:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            (
                [
                    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
                ],
                6,
            ),
            ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
            ([[1]], 1),
            ([[1, 1], [1, 1]], 4),
            ([[1, 0], [0, 1]], 1),
            ([[1, 1, 0], [0, 1, 0], [0, 0, 0]], 3),
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 8),
            ([[0, 0, 0], [0, 0, 0]], 0),
            ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 1),
            ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 1]], 5),
            ([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 1]], 4),
            ([[1, 1, 1, 1, 1]], 5),
            ([[1], [1], [1]], 3),
        ],
    )
    def test_max_area_of_island(self, grid: list[list[int]], expected: int):
        result = run_max_area_of_island(Solution, grid)
        assert_max_area_of_island(result, expected)
