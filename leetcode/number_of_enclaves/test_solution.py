import pytest

from leetcode_py import logged_test

from .helpers import assert_num_enclaves, run_num_enclaves
from .solution import Solution


class TestNumberOfEnclaves:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 0, 0, 0], [1, 0, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]], 3),
            ([[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]], 0),
            ([[0]], 0),
            ([[1]], 0),
            ([[0, 0], [0, 0]], 0),
            ([[1, 1], [1, 1]], 0),
            ([[1, 0], [0, 1]], 0),
            ([[1, 1], [0, 0], [1, 1]], 0),
            ([[0, 1], [1, 0]], 0),
            ([[0, 0, 1], [1, 1, 1], [1, 1, 1]], 0),
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 1),
            ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 1),
        ],
    )
    def test_num_enclaves(self, grid: list[list[int]], expected: int):
        result = run_num_enclaves(Solution, grid)
        assert_num_enclaves(result, expected)
