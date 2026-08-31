import pytest

from leetcode_py import logged_test

from .helpers import assert_num_distinct_islands, run_num_distinct_islands
from .solution import Solution


class TestNumberOfDistinctIslands:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]], 1),
            ([[1, 1, 0, 1, 1], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [1, 1, 0, 1, 1]], 3),
            ([[1]], 1),
            ([[0]], 0),
            ([[0, 0], [0, 0]], 0),
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 1),
            ([[1, 0], [0, 1]], 1),
            ([[1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0]], 2),
            ([[1, 1, 1, 1], [1, 0, 0, 0]], 1),
            ([[1, 1, 0], [1, 1, 0], [0, 0, 1], [0, 1, 1]], 2),
            ([[1], [1], [0], [1]], 2),
            ([[1, 0, 1, 0, 1]], 1),
        ],
    )
    def test_num_distinct_islands(self, grid: list[list[int]], expected: int):
        result = run_num_distinct_islands(Solution, grid)
        assert_num_distinct_islands(result, expected)
