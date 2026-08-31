import pytest

from leetcode_py import logged_test

from .helpers import assert_snakes_and_ladders, run_snakes_and_ladders
from .solution import Solution


class TestSnakesAndLadders:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "board, expected",
        [
            (
                [
                    [-1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1, -1],
                    [-1, 35, -1, -1, 13, -1],
                    [-1, -1, -1, -1, -1, -1],
                    [-1, 15, -1, -1, -1, -1],
                ],
                4,
            ),
            ([[-1, -1], [-1, 3]], 1),
            ([[-1, -1, -1], [-1, 9, 8], [-1, 4, -1]], 1),
            ([[-1, 1, -1], [1, 1, 1], [-1, 1, 1]], 2),
            ([[-1, 4, -1], [6, 2, 6], [-1, 3, -1]], 2),
            (
                [
                    [-1, -1, 22, -1, -1],
                    [-1, -1, -1, -1, -1],
                    [-1, -1, -1, 15, -1],
                    [-1, -1, -1, -1, -1],
                    [-1, -1, -1, -1, -1],
                ],
                4,
            ),
            (
                [
                    [-1, 10, -1, 15, -1],
                    [-1, -1, 18, 2, 20],
                    [-1, -1, -1, -1, 10],
                    [-1, 7, -1, 6, 17],
                    [-1, -1, -1, -1, -1],
                ],
                3,
            ),
            ([[-1, -1], [-1, -1]], 1),
            ([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]], 2),
            ([[-1, -1, -1], [-1, -1, -1], [-1, -1, 9]], 1),
            ([[-1, 7, -1], [-1, -1, -1], [-1, -1, -1]], 2),
            ([[-1, -1, 5, -1], [-1, -1, -1, -1], [-1, -1, -1, 12], [-1, -1, -1, -1]], 2),
        ],
    )
    def test_snakes_and_ladders(self, board: list[list[int]], expected: int):
        result = run_snakes_and_ladders(Solution, board)
        assert_snakes_and_ladders(result, expected)
