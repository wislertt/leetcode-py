import pytest

from leetcode_py import logged_test

from .helpers import assert_design_tic_tac_toe, run_design_tic_tac_toe
from .solution import TicTacToe


class TestDesignTicTacToe:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"],
                [[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]],
                [None, 0, 0, 0, 0, 0, 0, 1],
            ),
            (
                ["TicTacToe", "move", "move", "move", "move", "move"],
                [[4], [0, 0, 1], [1, 1, 2], [0, 1, 1], [1, 2, 2], [0, 2, 1]],
                [None, 0, 0, 0, 0, 0],
            ),
            (
                ["TicTacToe", "move", "move", "move"],
                [[2], [0, 0, 1], [1, 0, 2], [0, 1, 1]],
                [None, 0, 0, 1],
            ),
            (
                ["TicTacToe", "move", "move", "move"],
                [[2], [0, 0, 1], [0, 1, 2], [1, 1, 1]],
                [None, 0, 0, 1],
            ),
            (
                ["TicTacToe", "move", "move", "move", "move", "move"],
                [[3], [0, 0, 1], [0, 1, 2], [1, 1, 1], [0, 2, 2], [2, 2, 1]],
                [None, 0, 0, 0, 0, 1],
            ),
            (
                ["TicTacToe", "move", "move", "move", "move", "move", "move"],
                [[3], [0, 0, 1], [0, 2, 2], [0, 1, 1], [1, 1, 2], [1, 0, 1], [2, 0, 2]],
                [None, 0, 0, 0, 0, 0, 2],
            ),
            (
                [
                    "TicTacToe",
                    "move",
                    "move",
                    "move",
                    "move",
                    "move",
                    "move",
                    "move",
                    "move",
                    "move",
                ],
                [
                    [3],
                    [0, 0, 1],
                    [0, 2, 2],
                    [0, 1, 1],
                    [1, 0, 2],
                    [1, 2, 1],
                    [1, 1, 2],
                    [2, 0, 1],
                    [2, 1, 2],
                    [2, 2, 1],
                ],
                [None, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ),
            (
                ["TicTacToe", "move", "move", "move", "move", "move"],
                [[3], [0, 0, 2], [1, 0, 1], [1, 1, 2], [2, 2, 1], [2, 1, 2]],
                [None, 0, 0, 0, 0, 0],
            ),
            (
                ["TicTacToe", "move", "move", "move", "move", "move", "move", "move"],
                [[4], [0, 0, 1], [0, 1, 2], [1, 1, 1], [0, 2, 2], [2, 2, 1], [0, 3, 2], [3, 3, 1]],
                [None, 0, 0, 0, 0, 0, 0, 1],
            ),
            (
                ["TicTacToe", "move", "move", "move", "move", "move"],
                [[3], [0, 1, 1], [0, 0, 2], [1, 1, 1], [1, 0, 2], [2, 1, 1]],
                [None, 0, 0, 0, 0, 1],
            ),
            (
                ["TicTacToe", "move", "move", "move", "move", "move", "move"],
                [[3], [0, 0, 1], [2, 0, 2], [0, 1, 1], [2, 1, 2], [1, 2, 1], [2, 2, 2]],
                [None, 0, 0, 0, 0, 0, 2],
            ),
            (
                ["TicTacToe", "move", "move", "move", "move", "move", "move"],
                [[3], [0, 1, 1], [0, 0, 2], [1, 2, 1], [1, 1, 2], [2, 0, 1], [2, 2, 2]],
                [None, 0, 0, 0, 0, 0, 2],
            ),
            (
                ["TicTacToe", "move", "move", "move", "move", "move", "move"],
                [[3], [0, 0, 1], [0, 2, 2], [1, 1, 1], [1, 2, 2], [2, 1, 1], [2, 2, 2]],
                [None, 0, 0, 0, 0, 0, 2],
            ),
            (
                ["TicTacToe", "move", "move", "move", "move", "move"],
                [[3], [2, 1, 1], [0, 0, 2], [2, 0, 1], [1, 1, 2], [2, 2, 1]],
                [None, 0, 0, 0, 0, 1],
            ),
            (
                ["TicTacToe", "move", "move", "move", "move", "move", "move"],
                [[3], [0, 0, 1], [2, 2, 2], [1, 0, 1], [1, 1, 2], [0, 1, 1], [0, 2, 2]],
                [None, 0, 0, 0, 0, 0, 0],
            ),
        ],
    )
    def test_design_tic_tac_toe(
        self, operations: list[str], inputs: list[list[int]], expected: list[int | None]
    ):
        result, _ = run_design_tic_tac_toe(TicTacToe, operations, inputs)
        assert_design_tic_tac_toe(result, expected)
