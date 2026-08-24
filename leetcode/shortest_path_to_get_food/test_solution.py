import pytest

from leetcode_py import logged_test

from .helpers import assert_get_food, run_get_food
from .solution import Solution


class TestShortestPathToGetFood:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            (
                [
                    ["X", "X", "X", "X", "X", "X"],
                    ["X", "*", "O", "O", "O", "X"],
                    ["X", "O", "O", "#", "O", "X"],
                    ["X", "X", "X", "X", "X", "X"],
                ],
                3,
            ),
            (
                [
                    ["X", "X", "X", "X", "X"],
                    ["X", "*", "X", "O", "X"],
                    ["X", "O", "X", "#", "X"],
                    ["X", "X", "X", "X", "X"],
                ],
                -1,
            ),
            (
                [
                    ["X", "X", "X", "X", "X", "X", "X", "X"],
                    ["X", "*", "O", "X", "O", "#", "O", "X"],
                    ["X", "O", "O", "X", "O", "O", "X", "X"],
                    ["X", "O", "O", "O", "O", "#", "O", "X"],
                    ["X", "X", "X", "X", "X", "X", "X", "X"],
                ],
                6,
            ),
            ([["O", "*"], ["#", "O"]], 2),
            ([["X", "*"], ["#", "X"]], -1),
            ([["*", "#"]], 1),
            ([["#", "*"]], 1),
            ([["*", "O", "#"]], 2),
            ([["*", "X", "#"]], -1),
            ([["*"]], -1),
            ([["*", "O", "O", "O", "O", "O", "O", "#"]], 7),
            ([["*"], ["O"], ["O"], ["#"]], 3),
            ([["O", "O", "*", "O", "O"], ["O", "X", "X", "X", "O"], ["O", "O", "#", "O", "O"]], 6),
            ([["O", "*", "O"], ["O", "X", "O"], ["#", "O", "#"]], 3),
            ([["*", "O", "O"], ["X", "X", "O"], ["O", "O", "#"]], 4),
            ([["#", "X", "*"], ["O", "X", "O"], ["O", "O", "#"]], 2),
            ([["X", "*", "X"], ["X", "O", "X"], ["X", "#", "X"]], 2),
            (
                [
                    ["*", "O", "O", "O"],
                    ["O", "X", "X", "O"],
                    ["O", "X", "#", "O"],
                    ["O", "O", "O", "O"],
                ],
                6,
            ),
            ([["*", "O", "O"], ["X", "X", "O"], ["O", "O", "O"], ["O", "X", "#"]], 5),
        ],
    )
    def test_get_food(self, grid: list[list[str]], expected: int):
        result = run_get_food(Solution, grid)
        assert_get_food(result, expected)
