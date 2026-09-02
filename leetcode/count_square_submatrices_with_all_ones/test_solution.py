import pytest

from leetcode_py import logged_test

from .helpers import assert_count_squares, run_count_squares
from .solution import Solution


class TestCountSquareSubmatricesWithAllOnes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            [[[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]], 15],
            [[[1, 0, 1], [1, 1, 0], [1, 1, 0]], 7],
            [[[1]], 1],
            [[[0]], 0],
            [[[0, 1], [1, 0]], 2],
            [[[1, 1], [1, 1]], 5],
            [[[1, 1, 1], [1, 1, 1], [1, 1, 1]], 14],
            [[[0, 0], [0, 0]], 0],
            [[[1, 0], [0, 1]], 2],
            [[[1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 0]], 14],
            [
                [
                    [1, 0, 0, 1, 0, 0],
                    [1, 1, 1, 1, 1, 0],
                    [1, 0, 1, 0, 1, 1],
                    [1, 1, 1, 1, 0, 1],
                    [1, 0, 0, 1, 1, 1],
                    [1, 1, 1, 1, 0, 0],
                ],
                24,
            ],
            [[[1, 1, 1], [0, 0, 0], [1, 0, 1]], 5],
            [[[0, 0, 1, 0], [0, 1, 0, 0], [0, 1, 1, 0], [1, 1, 0, 1]], 7],
            [[[1, 0, 0, 1, 1, 1], [1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1]], 24],
            [[[1, 1, 1, 1, 1], [1, 0, 1, 0, 1]], 8],
        ],
    )
    def test_count_squares(self, matrix: list[list[int]], expected: int):
        result = run_count_squares(Solution, matrix)
        assert_count_squares(result, expected)
