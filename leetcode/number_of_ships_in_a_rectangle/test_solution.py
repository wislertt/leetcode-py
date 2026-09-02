import pytest

from leetcode_py import logged_test

from .helpers import assert_count_ships, run_count_ships
from .solution import Solution


class TestNumberOfShipsInARectangle:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "ships, top_right, bottom_left, expected",
        [
            ([[1, 1], [2, 2], [3, 3], [5, 5]], [4, 4], [0, 0], 3),
            ([[1, 1], [2, 2], [3, 3]], [1000, 1000], [0, 0], 3),
            ([[0, 0]], [1, 1], [0, 0], 1),
            ([], [10, 10], [0, 0], 0),
            ([[5, 5]], [4, 4], [0, 0], 0),
            ([[0, 0]], [0, 1], [0, 0], 1),
            ([[7, 7]], [7, 7], [3, 3], 1),
            ([[0, 0], [0, 4], [4, 0], [4, 4]], [4, 4], [0, 0], 4),
            ([[2, 2]], [1000, 1000], [0, 0], 1),
            (
                [[1, 1], [1, 2], [2, 1], [2, 2], [3, 3], [3, 4], [4, 4], [5, 5], [6, 6], [7, 7]],
                [7, 7],
                [0, 0],
                10,
            ),
            ([[0, 0], [3, 0], [3, 1]], [5, 0], [0, 0], 2),
            ([[1, 1], [0, 5]], [0, 9], [0, 0], 1),
            ([[999, 999], [500, 500]], [1000, 1000], [999, 999], 1),
            ([[10, 10], [20, 20], [30, 30]], [25, 25], [15, 15], 1),
            ([[389, 497]], [889, 790], [125, 402], 1),
            ([[456, 612]], [571, 975], [335, 416], 1),
            ([[745, 404], [766, 500], [632, 864]], [769, 798], [685, 67], 2),
            ([[913, 293]], [938, 706], [823, 2], 1),
        ],
    )
    def test_count_ships(
        self, ships: list[list[int]], top_right: list[int], bottom_left: list[int], expected: int
    ):
        result = run_count_ships(Solution, ships, top_right, bottom_left)
        assert_count_ships(result, expected)
