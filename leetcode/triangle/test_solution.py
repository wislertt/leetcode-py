import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_total, run_minimum_total
from .solution import Solution


class TestTriangle:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "triangle, expected",
        [
            ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
            ([[-10]], -10),
            ([[1]], 1),
            ([[1], [2, 3]], 3),
            ([[1], [2, 3], [4, 5, 6]], 7),
            ([[-1], [-2, -3]], -4),
            ([[-10000]], -10000),
            ([[10000], [10000, 10000]], 20000),
            ([[5], [6, 3], [7, 2, 9]], 10),
            ([[1], [2, 3], [3, 6, 7], [8, 9, 6, 10]], 14),
            ([[-5], [-10, -1], [5, 3, -2]], -12),
            ([[3], [4, 1], [1, 8, 9], [2, 5, 6, 7]], 10),
            ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3], [9, 2, 8, 5, 6]], 13),
            ([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]], 14),
            ([[0], [0, 0], [0, 0, 0]], 0),
            ([[7], [8, 9], [10, 11, 12], [13, 14, 15, 16]], 38),
        ],
    )
    def test_minimum_total(self, triangle: list[list[int]], expected: int):
        result = run_minimum_total(Solution, triangle)
        assert_minimum_total(result, expected)
