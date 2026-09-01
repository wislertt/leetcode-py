import pytest

from leetcode_py import logged_test

from .helpers import assert_count_sub_islands, run_count_sub_islands
from .solution import Solution


class TestCountSubIslandsTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid1, grid2, expected",
        [
            ([[1]], [[1]], 1),
            ([[0]], [[1]], 0),
            ([[1]], [[0]], 0),
            ([[1, 1], [1, 1]], [[1, 1], [1, 1]], 1),
            ([[1, 0], [0, 1]], [[1, 1], [1, 0]], 0),
            ([[0, 0], [0, 0]], [[1, 1], [1, 1]], 0),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]], 4),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]], 1),
            ([[1, 1, 1, 1]], [[1, 0, 0, 1]], 2),
            ([[1, 0, 1, 1, 1]], [[1, 1, 0, 1, 1]], 1),
            ([[1, 0, 1, 0, 1]], [[1, 1, 0, 1, 1]], 0),
            ([[1], [1], [1]], [[1], [0], [1]], 2),
            ([[1], [0], [1]], [[1], [1], [1]], 0),
            ([[1, 0, 0], [1, 1, 1]], [[1, 1, 1], [1, 1, 1]], 0),
            ([[1, 1, 0], [0, 1, 0], [0, 0, 1]], [[1, 1, 0], [0, 1, 0], [0, 0, 0]], 1),
            ([[1, 1, 0], [0, 1, 1], [0, 0, 0]], [[1, 1, 0], [0, 1, 0], [0, 0, 1]], 1),
            (
                [[1, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 0, 0, 0]],
                [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [0, 1, 0, 1, 0]],
                0,
            ),
            ([[1, 0], [1, 1], [0, 1]], [[1, 1], [1, 1], [1, 1]], 0),
        ],
    )
    def test_count_sub_islands(self, grid1: list[list[int]], grid2: list[list[int]], expected: int):
        result = run_count_sub_islands(Solution, grid1, grid2)
        assert_count_sub_islands(result, expected)
