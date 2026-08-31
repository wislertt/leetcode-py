import pytest

from leetcode_py import logged_test

from .helpers import assert_min_falling_path_sum, run_min_falling_path_sum
from .solution import Solution


class TestMinimumFallingPathSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13),
            ([[-19, 57], [-40, -5]], -59),
            ([[1]], 1),
            ([[-5]], -5),
            ([[-100]], -100),
            ([[3, 1, 2], [2, 1, 3], [1, 1, 1]], 3),
            ([[9, 9, 9], [9, 1, 9], [9, 9, 9]], 19),
            ([[1, 2], [3, 4]], 4),
            ([[100, -100], [-100, 100]], -200),
            ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 12),
            ([[-80, -13, 22], [83, 94, -5], [73, -48, -61]], -79),
            ([[17, 82, 5, 33], [1, -44, 29, -79], [8, 49, -11, 3], [-79, 34, 62, -20]], -110),
            ([[48, 36, 86, 85], [43, 45, 15, 84], [0, 32, 21, 75], [4, 93, 58, 1]], 73),
        ],
    )
    def test_min_falling_path_sum(self, matrix: list[list[int]], expected: int):
        result = run_min_falling_path_sum(Solution, matrix)
        assert_min_falling_path_sum(result, expected)
