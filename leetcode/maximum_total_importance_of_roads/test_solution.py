import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_importance, run_maximum_importance
from .solution import Solution


class TestMaximumTotalImportanceOfRoads:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "roads, n, expected",
        [
            ([[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]], 5, 43),
            ([[0, 3], [2, 4], [1, 3]], 5, 20),
            ([[0, 1]], 2, 3),
            ([[0, 1], [1, 2], [0, 2]], 3, 12),
            ([[0, 1]], 4, 7),
            ([[0, 1], [1, 2]], 3, 9),
            ([[0, 1], [2, 3], [0, 3], [1, 2]], 4, 20),
            ([[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]], 6, 39),
            ([[0, 1], [0, 2], [0, 3], [0, 4]], 5, 30),
            ([[0, 1], [1, 2]], 4, 13),
            ([[0, 1], [1, 2], [0, 2], [3, 4], [5, 6]], 7, 46),
            ([[0, 3], [4, 6], [1, 5]], 7, 27),
            ([[1, 2], [4, 5], [2, 4], [1, 5], [0, 4]], 6, 44),
            ([[0, 3], [2, 3], [0, 2], [1, 2], [0, 1], [1, 3]], 4, 30),
            ([[2, 4], [0, 3], [1, 5]], 6, 21),
            ([[1, 5], [1, 4]], 6, 21),
            ([[0, 3], [4, 5], [0, 5], [2, 4]], 6, 35),
            ([[3, 6], [0, 1], [2, 6], [2, 4]], 7, 40),
            ([[1, 3], [1, 2], [0, 1], [2, 3], [0, 2], [0, 3]], 4, 30),
        ],
    )
    def test_maximum_importance(self, roads: list[list[int]], n: int, expected: int):
        result = run_maximum_importance(Solution, n, roads)
        assert_maximum_importance(result, expected)
