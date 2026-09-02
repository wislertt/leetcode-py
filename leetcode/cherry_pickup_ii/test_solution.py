import pytest

from leetcode_py import logged_test

from .helpers import assert_cherry_pickup, run_cherry_pickup
from .solution import Solution


class TestCherryPickupII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]], 24),
            (
                [
                    [1, 0, 0, 0, 0, 0, 1],
                    [2, 0, 0, 0, 0, 3, 0],
                    [2, 0, 9, 0, 0, 0, 0],
                    [0, 3, 0, 5, 4, 0, 0],
                    [1, 0, 2, 3, 0, 0, 6],
                ],
                28,
            ),
            ([[1, 1], [1, 1]], 4),
            ([[0, 0], [0, 0]], 0),
            ([[5, 5], [5, 5]], 20),
            ([[4, 1, 2], [3, 9, 8]], 23),
            ([[1, 2, 3, 4], [5, 6, 7, 8]], 19),
            ([[100, 100], [100, 100]], 400),
            ([[1, 0, 1], [0, 0, 0], [1, 0, 1]], 4),
            ([[7, 0, 0, 7], [0, 6, 6, 0], [5, 0, 0, 5]], 36),
            ([[2, 8, 0], [7, 5, 3], [7, 3, 8], [0, 8, 8]], 45),
            ([[2, 8, 4, 0, 0], [1, 6, 0, 9, 8], [2, 7, 3, 8, 3], [6, 0, 2, 7, 6]], 45),
            ([[9, 9, 2, 1], [0, 0, 6, 9], [0, 0, 6, 9], [0, 0, 6, 7], [5, 0, 3, 4]], 54),
            ([[3, 1], [6, 5]], 15),
            (
                [
                    [9, 1, 9, 7, 1],
                    [0, 5, 5, 4, 1],
                    [7, 8, 2, 2, 8],
                    [5, 1, 9, 4, 5],
                    [2, 1, 8, 2, 7],
                ],
                64,
            ),
            ([[9, 6], [9, 0], [7, 0], [0, 3]], 34),
            ([[5, 2], [6, 2], [2, 6], [0, 3], [7, 5], [3, 5]], 46),
            ([[1, 9], [8, 1], [9, 9], [4, 1], [4, 3]], 49),
        ],
    )
    def test_cherry_pickup(self, grid: list[list[int]], expected: int):
        result = run_cherry_pickup(Solution, grid)
        assert_cherry_pickup(result, expected)
