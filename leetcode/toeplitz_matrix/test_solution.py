import pytest

from leetcode_py import logged_test

from .helpers import assert_is_toeplitz_matrix, run_is_toeplitz_matrix
from .solution import Solution


class TestToeplitzMatrix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True),
            ([[1, 2], [2, 2]], False),
            ([[1]], True),
            ([[0]], True),
            ([[99]], True),
            ([[1, 2]], True),
            ([[1], [2]], True),
            ([[1, 2], [1, 2]], False),
            ([[1, 2], [2, 1]], True),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], False),
            ([[1, 2, 3], [4, 1, 2], [7, 4, 1]], True),
            ([[1, 2, 3], [4, 1, 2], [7, 4, 2]], False),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], True),
            ([[18, 66], [84, 18]], True),
            ([[90, 18], [88, 90], [42, 95]], False),
            ([[36, 59, 76, 4], [26, 54, 8, 56], [54, 4, 33, 80]], False),
            ([[37, 36, 11, 70], [65, 37, 43, 11], [18, 65, 37, 36]], False),
            ([[31, 16], [25, 31], [60, 32], [42, 60]], False),
            ([[1, 41], [9, 62], [46, 70]], False),
            ([[79, 2], [15, 58], [33, 42], [94, 83]], False),
        ],
    )
    def test_is_toeplitz_matrix(self, matrix: list[list[int]], expected: bool):
        result = run_is_toeplitz_matrix(Solution, matrix)
        assert_is_toeplitz_matrix(result, expected)
