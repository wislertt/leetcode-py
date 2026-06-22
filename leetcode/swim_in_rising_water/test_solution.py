import pytest

from leetcode_py import logged_test

from .helpers import assert_swim_in_water, run_swim_in_water
from .solution import Solution


class TestSwimInRisingWater:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[0, 2], [1, 3]], 3),
            (
                [
                    [0, 1, 2, 3, 4],
                    [24, 23, 22, 21, 5],
                    [12, 13, 14, 15, 16],
                    [11, 17, 18, 19, 20],
                    [10, 9, 8, 7, 6],
                ],
                16,
            ),
            ([[0]], 0),
            ([[5]], 5),
            ([[0, 1], [2, 3]], 3),
            ([[3, 2], [1, 0]], 3),
            ([[0, 5], [5, 1]], 5),
            ([[8, 1], [2, 3]], 8),
            ([[0, 9], [9, 1]], 9),
            ([[1, 4], [2, 3]], 3),
            ([[2, 4], [3, 1]], 3),
            ([[0, 4], [1, 5]], 5),
            ([[0, 3], [2, 1]], 2),
        ],
    )
    def test_swim_in_water(self, grid: list[list[int]], expected: int):
        result = run_swim_in_water(Solution, grid)
        assert_swim_in_water(result, expected)
