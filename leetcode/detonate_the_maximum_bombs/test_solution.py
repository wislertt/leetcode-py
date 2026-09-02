import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_detonation, run_maximum_detonation
from .solution import Solution


class TestDetonateTheMaximumBombs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "bombs, expected",
        [
            ([[2, 1, 3], [6, 1, 4]], 2),
            ([[1, 1, 5], [10, 10, 5]], 1),
            ([[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]], 5),
            ([[1, 1, 1]], 1),
            ([[1, 1, 1], [1, 1, 1]], 2),
            ([[1, 1, 5], [10, 10, 5], [1, 2, 1]], 2),
            ([[1, 1, 100], [2, 2, 1], [3, 3, 1], [4, 4, 1]], 4),
            ([[1, 1, 1], [2, 2, 1], [3, 3, 1], [4, 4, 1]], 1),
            ([[100000, 100000, 100000], [1, 1, 1]], 1),
            ([[1, 1, 2], [1, 1, 2], [5, 5, 2], [9, 9, 1]], 2),
            ([[2, 1, 3], [6, 1, 4], [15, 20, 50], [5, 5, 1]], 4),
            ([[1, 3, 2], [3, 1, 2], [5, 5, 1], [6, 6, 1], [9, 9, 1]], 1),
            ([[12, 3, 1], [5, 10, 3], [11, 10, 3], [10, 3, 9]], 4),
            ([[9, 11, 4], [2, 11, 8]], 2),
            ([[3, 2, 7], [10, 4, 10], [6, 10, 5]], 3),
            ([[11, 10, 9], [8, 8, 9], [10, 5, 5]], 3),
            ([[3, 3, 7], [5, 5, 3], [5, 11, 9], [10, 10, 6], [5, 8, 10], [10, 3, 8]], 6),
            ([[1, 6, 5], [3, 9, 7], [2, 9, 9], [6, 10, 1], [2, 9, 8]], 5),
            ([[12, 3, 8], [1, 11, 7], [9, 6, 7]], 2),
            ([[12, 4, 5], [1, 3, 10], [7, 12, 7], [3, 10, 10], [7, 4, 3], [6, 6, 3]], 5),
        ],
    )
    def test_maximum_detonation(self, bombs: list[list[int]], expected: int):
        result = run_maximum_detonation(Solution, bombs)
        assert_maximum_detonation(result, expected)
