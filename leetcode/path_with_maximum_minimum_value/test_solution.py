import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_minimum_path, run_maximum_minimum_path
from .solution import Solution


class TestPathWithMaximumMinimumValue:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[5, 4, 5], [1, 2, 6], [7, 4, 6]], 4),
            ([[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]], 2),
            (
                [
                    [3, 4, 6, 3, 4],
                    [0, 2, 1, 1, 7],
                    [8, 8, 3, 2, 7],
                    [3, 2, 4, 9, 8],
                    [4, 1, 2, 0, 0],
                    [4, 6, 5, 4, 3],
                ],
                3,
            ),
            ([[1]], 1),
            ([[0, 0], [0, 0]], 0),
            ([[1, 2, 3], [6, 5, 4]], 1),
            ([[9, 9, 9], [9, 0, 9], [9, 9, 9]], 9),
            ([[5, 0], [0, 5]], 0),
            ([[4, 3, 1], [3, 2, 4], [1, 4, 5]], 2),
            ([[7, 6, 5, 4], [8, 7, 6, 5], [9, 8, 7, 6]], 6),
            ([[0, 10, 0], [10, 0, 10], [0, 10, 0]], 0),
            ([[2, 0, 2, 0], [1, 9, 9, 1], [2, 0, 2, 0]], 0),
        ],
    )
    def test_maximum_minimum_path(self, grid: list[list[int]], expected: int):
        result = run_maximum_minimum_path(Solution, grid)
        assert_maximum_minimum_path(result, expected)
