import pytest

from leetcode_py import logged_test

from .helpers import assert_num_distinct_islands_ii, run_num_distinct_islands_ii
from .solution import Solution


class TestNumberOfDistinctIslandsII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]], 1),
            ([[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]], 1),
            ([[1]], 1),
            ([[0]], 0),
            ([[1, 0], [0, 1]], 1),
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 1),
            ([[1, 1, 0], [0, 1, 0], [0, 0, 1]], 2),
            ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 1),
            ([[1, 1, 0, 0], [1, 0, 1, 0], [0, 0, 0, 1]], 2),
            ([[1], [1], [0], [1]], 2),
            ([[1, 1], [1, 0], [1, 1]], 1),
            ([[1, 0, 0], [1, 1, 1]], 1),
        ],
    )
    def test_num_distinct_islands_ii(self, grid: list[list[int]], expected: int):
        result = run_num_distinct_islands_ii(Solution, grid)
        assert_num_distinct_islands_ii(result, expected)
