import pytest

from leetcode_py import logged_test

from .helpers import assert_num_magic_squares_inside, run_num_magic_squares_inside
from .solution import Solution


class TestMagicSquaresInGrid:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]], 1),
            ([[8]], 0),
            ([[4, 7, 8], [9, 5, 1], [2, 3, 6]], 0),
            ([[4, 9, 2], [3, 5, 7], [8, 1, 6]], 1),
            (
                [
                    [3, 2, 9, 2, 7],
                    [6, 1, 8, 8, 6],
                    [5, 0, 1, 4, 5],
                    [6, 7, 2, 9, 4],
                    [3, 2, 7, 6, 1],
                ],
                0,
            ),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0),
            ([[10, 3, 5], [1, 6, 11], [7, 9, 2]], 0),
            ([[4, 3, 8, 4, 3, 8], [9, 5, 1, 9, 5, 1], [2, 7, 6, 2, 7, 6]], 2),
            ([[5, 5, 5], [5, 5, 5], [5, 5, 5]], 0),
            (
                [
                    [8, 1, 6, 8, 1, 6],
                    [3, 5, 7, 3, 5, 7],
                    [4, 9, 2, 4, 9, 2],
                    [8, 1, 6, 8, 1, 6],
                    [3, 5, 7, 3, 5, 7],
                    [4, 9, 2, 4, 9, 2],
                ],
                4,
            ),
            (
                [
                    [1, 15, 14, 4, 13],
                    [12, 6, 7, 9, 8],
                    [11, 10, 2, 5, 3],
                    [1, 15, 14, 4, 13],
                    [12, 6, 7, 9, 8],
                ],
                0,
            ),
            ([[9, 0, 8, 1, 6], [2, 7, 3, 5, 7], [4, 5, 4, 9, 2], [6, 1, 8, 1, 6]], 1),
            ([[1]], 0),
        ],
    )
    def test_num_magic_squares_inside(self, grid: list[list[int]], expected: int):
        result = run_num_magic_squares_inside(Solution, grid)
        assert_num_magic_squares_inside(result, expected)
