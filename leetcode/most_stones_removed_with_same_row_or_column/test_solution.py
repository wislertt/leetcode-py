import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_stones, run_remove_stones
from .solution import Solution


class TestMostStonesRemovedWithSameRowOrColumn:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "stones, expected",
        [
            ([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]], 5),
            ([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]], 3),
            ([[0, 0]], 0),
            ([[0, 0], [0, 1]], 1),
            ([[0, 0], [1, 1]], 0),
            ([[0, 0], [1, 1], [2, 2], [3, 3]], 0),
            ([[0, 0], [0, 1], [0, 2], [0, 3]], 3),
            ([[0, 0], [0, 1], [1, 0]], 2),
            ([[0, 1], [1, 0], [1, 2], [2, 1]], 2),
            ([[0, 0], [0, 1], [1, 2], [2, 3]], 1),
            ([[10000, 10000], [10000, 0], [0, 10000]], 2),
            ([[2, 2], [4, 0], [1, 3], [2, 0], [1, 2], [4, 1], [0, 2]], 6),
            ([[3, 2], [0, 1], [3, 1], [1, 2], [2, 4], [4, 2], [2, 2]], 6),
            ([[4, 4], [2, 4], [0, 4], [2, 3], [3, 2], [1, 1], [2, 1], [3, 1], [0, 2]], 8),
            ([[4, 1], [1, 2], [3, 2], [3, 4], [0, 4], [0, 0]], 4),
            ([[3, 0], [0, 4], [2, 3], [4, 0], [2, 2], [0, 0], [3, 3], [1, 3], [1, 4]], 8),
            ([[2, 4], [0, 3], [1, 3], [4, 3], [2, 3], [4, 2]], 5),
            ([[0, 4], [3, 3], [1, 4], [2, 3], [4, 2], [3, 1], [0, 1], [4, 3]], 7),
            ([[1, 2], [3, 3], [3, 2], [1, 1], [4, 3], [1, 3]], 5),
            ([[3, 2], [1, 3], [4, 0], [0, 0], [0, 4], [4, 1], [0, 3], [2, 2]], 6),
        ],
    )
    def test_remove_stones(self, stones: list[list[int]], expected: int):
        result = run_remove_stones(Solution, stones)
        assert_remove_stones(result, expected)
