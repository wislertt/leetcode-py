import pytest

from leetcode_py import logged_test

from .helpers import assert_spiral_matrix_iii, run_spiral_matrix_iii
from .solution import Solution


class TestSpiralMatrixIii:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "rows, cols, r_start, c_start, expected",
        [
            (1, 4, 0, 0, [[0, 0], [0, 1], [0, 2], [0, 3]]),
            (
                5,
                6,
                1,
                4,
                [
                    [1, 4],
                    [1, 5],
                    [2, 5],
                    [2, 4],
                    [2, 3],
                    [1, 3],
                    [0, 3],
                    [0, 4],
                    [0, 5],
                    [3, 5],
                    [3, 4],
                    [3, 3],
                    [3, 2],
                    [2, 2],
                    [1, 2],
                    [0, 2],
                    [4, 5],
                    [4, 4],
                    [4, 3],
                    [4, 2],
                    [4, 1],
                    [3, 1],
                    [2, 1],
                    [1, 1],
                    [0, 1],
                    [4, 0],
                    [3, 0],
                    [2, 0],
                    [1, 0],
                    [0, 0],
                ],
            ),
            (3, 3, 1, 1, [[1, 1], [1, 2], [2, 2], [2, 1], [2, 0], [1, 0], [0, 0], [0, 1], [0, 2]]),
            (2, 2, 0, 0, [[0, 0], [0, 1], [1, 1], [1, 0]]),
            (1, 1, 0, 0, [[0, 0]]),
            (2, 1, 1, 0, [[1, 0], [0, 0]]),
            (1, 2, 0, 0, [[0, 0], [0, 1]]),
            (3, 2, 2, 1, [[2, 1], [2, 0], [1, 0], [1, 1], [0, 0], [0, 1]]),
            (
                4,
                4,
                0,
                0,
                [
                    [0, 0],
                    [0, 1],
                    [1, 1],
                    [1, 0],
                    [0, 2],
                    [1, 2],
                    [2, 2],
                    [2, 1],
                    [2, 0],
                    [0, 3],
                    [1, 3],
                    [2, 3],
                    [3, 3],
                    [3, 2],
                    [3, 1],
                    [3, 0],
                ],
            ),
            (2, 3, 1, 2, [[1, 2], [1, 1], [0, 1], [0, 2], [1, 0], [0, 0]]),
            (
                4,
                4,
                1,
                2,
                [
                    [1, 2],
                    [1, 3],
                    [2, 3],
                    [2, 2],
                    [2, 1],
                    [1, 1],
                    [0, 1],
                    [0, 2],
                    [0, 3],
                    [3, 3],
                    [3, 2],
                    [3, 1],
                    [3, 0],
                    [2, 0],
                    [1, 0],
                    [0, 0],
                ],
            ),
            (
                3,
                5,
                0,
                0,
                [
                    [0, 0],
                    [0, 1],
                    [1, 1],
                    [1, 0],
                    [0, 2],
                    [1, 2],
                    [2, 2],
                    [2, 1],
                    [2, 0],
                    [0, 3],
                    [1, 3],
                    [2, 3],
                    [0, 4],
                    [1, 4],
                    [2, 4],
                ],
            ),
        ],
    )
    def test_spiral_matrix_iii(
        self, rows: int, cols: int, r_start: int, c_start: int, expected: list[list[int]]
    ):
        result = run_spiral_matrix_iii(Solution, rows, cols, r_start, c_start)
        assert_spiral_matrix_iii(result, expected)
