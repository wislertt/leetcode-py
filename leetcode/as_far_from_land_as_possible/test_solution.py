import pytest

from leetcode_py import logged_test

from .helpers import assert_max_distance, run_max_distance
from .solution import Solution


class TestAsFarFromLandAsPossibleTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 2),
            ([[1, 0, 0], [0, 0, 0], [0, 0, 0]], 4),
            ([[1]], -1),
            ([[0]], -1),
            ([[1, 1], [1, 1]], -1),
            ([[0, 0], [0, 0]], -1),
            ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], 1),
            ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]], 3),
            ([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 4),
            ([[1, 0], [0, 0]], 2),
            ([[0, 1], [0, 0]], 2),
            ([[1, 1, 0], [0, 0, 0], [0, 0, 0]], 3),
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2),
            (
                [
                    [1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 1],
                ],
                4,
            ),
            ([[1, 0, 1], [0, 0, 0], [1, 0, 0]], 2),
        ],
    )
    def test_max_distance(self, grid: list[list[int]], expected: int):
        result = run_max_distance(Solution, grid)
        assert_max_distance(result, expected)
