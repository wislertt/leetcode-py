import pytest

from leetcode_py import logged_test

from .helpers import assert_solve, run_solve
from .solution import Solution


class TestSurroundedRegions:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "board, expected",
        [
            (
                [
                    ["X", "X", "X", "X"],
                    ["X", "O", "O", "X"],
                    ["X", "X", "O", "X"],
                    ["X", "O", "X", "X"],
                ],
                [
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["X", "O", "X", "X"],
                ],
            ),
            ([["X"]], [["X"]]),
            ([["O"]], [["O"]]),
            ([["O", "O"], ["O", "O"]], [["O", "O"], ["O", "O"]]),
            (
                [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]],
                [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]],
            ),
            ([["X", "O", "X"]], [["X", "O", "X"]]),
            ([["O", "X", "O", "X", "O"]], [["O", "X", "O", "X", "O"]]),
            (
                [
                    ["X", "X", "X", "X", "X"],
                    ["X", "O", "O", "O", "X"],
                    ["X", "O", "X", "O", "X"],
                    ["X", "O", "O", "O", "X"],
                    ["X", "X", "X", "X", "X"],
                ],
                [
                    ["X", "X", "X", "X", "X"],
                    ["X", "X", "X", "X", "X"],
                    ["X", "X", "X", "X", "X"],
                    ["X", "X", "X", "X", "X"],
                    ["X", "X", "X", "X", "X"],
                ],
            ),
            ([["X", "O"], ["O", "X"]], [["X", "O"], ["O", "X"]]),
            ([["O", "X", "X", "X", "X", "X", "O"]], [["O", "X", "X", "X", "X", "X", "O"]]),
            ([["O", "X"], ["X", "O"]], [["O", "X"], ["X", "O"]]),
            (
                [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]],
                [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"]],
            ),
            (
                [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]],
                [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]],
            ),
            (
                [
                    ["O", "X", "X", "O"],
                    ["X", "O", "O", "X"],
                    ["X", "O", "O", "X"],
                    ["O", "X", "X", "O"],
                ],
                [
                    ["O", "X", "X", "O"],
                    ["X", "X", "X", "X"],
                    ["X", "X", "X", "X"],
                    ["O", "X", "X", "O"],
                ],
            ),
        ],
    )
    def test_solve(self, board: list[list[str]], expected: list[list[str]]):
        result = run_solve(Solution, board)
        assert_solve(result, expected)
