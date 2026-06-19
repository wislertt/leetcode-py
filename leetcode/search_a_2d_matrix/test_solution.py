import pytest

from leetcode_py import logged_test

from .helpers import assert_search_matrix, run_search_matrix
from .solution import Solution


class TestSearchA2DMatrix:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, target, expected",
        [
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 60, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 1, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 0, False),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 100, False),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 11, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 16, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 17, False),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 20, True),
            ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 23, True),
            ([[1]], 1, True),
            ([[1]], 2, False),
            ([[1, 2, 3, 4, 5]], 3, True),
            ([[1], [2], [3], [4]], 3, True),
            ([[1], [2], [3], [4]], 5, False),
        ],
    )
    def test_search_matrix(self, matrix: list[list[int]], target: int, expected: bool):
        result = run_search_matrix(Solution, matrix, target)
        assert_search_matrix(result, expected)
