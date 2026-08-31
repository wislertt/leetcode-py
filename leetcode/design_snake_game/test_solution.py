import pytest

from leetcode_py import logged_test

from .helpers import assert_design_snake_game, run_design_snake_game
from .solution import SnakeGame


class TestDesignSnakeGame:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["SnakeGame", "move", "move", "move", "move", "move", "move"],
                [[3, 2, [[1, 2], [0, 1]]], ["R"], ["D"], ["R"], ["U"], ["L"], ["U"]],
                [None, 0, 0, 1, 1, 2, -1],
            ),
            (["SnakeGame", "move"], [[1, 1, []], ["D"]], [None, -1]),
            (["SnakeGame", "move", "move"], [[3, 1, [[0, 1]]], ["R"], ["L"]], [None, 1, 1]),
            (["SnakeGame", "move", "move"], [[2, 2, [[0, 1], [1, 1]]], ["R"], ["D"]], [None, 1, 2]),
            (
                ["SnakeGame", "move", "move", "move", "move"],
                [[3, 3, []], ["R"], ["D"], ["L"], ["U"]],
                [None, 0, 0, 0, 0],
            ),
            (["SnakeGame", "move", "move"], [[2, 2, [[1, 0]]], ["R"], ["D"]], [None, 0, 0]),
            (
                ["SnakeGame", "move", "move", "move", "move", "move", "move", "move"],
                [
                    [4, 4, [[0, 3], [1, 3], [2, 3], [3, 3]]],
                    ["R"],
                    ["R"],
                    ["R"],
                    ["D"],
                    ["D"],
                    ["D"],
                    ["D"],
                ],
                [None, 0, 0, 1, 2, 3, 4, -1],
            ),
            (
                ["SnakeGame", "move", "move", "move", "move", "move"],
                [[3, 3, [[2, 0], [2, 1], [2, 2], [1, 2]]], ["D"], ["D"], ["R"], ["R"], ["U"]],
                [None, 0, 1, 2, 3, 4],
            ),
            (["SnakeGame", "move", "move"], [[1, 3, [[1, 0], [2, 0]]], ["D"], ["D"]], [None, 1, 2]),
            (["SnakeGame", "move"], [[3, 3, []], ["L"]], [None, -1]),
            (["SnakeGame"], [[3, 3, [[0, 0]]]], [None]),
            (
                ["SnakeGame", "move", "move", "move", "move"],
                [[5, 5, [[2, 2]]], ["D"], ["R"], ["R"], ["D"]],
                [None, 0, 0, 0, 1],
            ),
            (
                ["SnakeGame", "move", "move", "move"],
                [[2, 3, [[2, 1]]], ["D"], ["D"], ["L"]],
                [None, 0, 0, -1],
            ),
            (["SnakeGame", "move", "move"], [[3, 3, [[1, 2]]], ["R"], ["R"]], [None, 0, 0]),
        ],
    )
    def test_design_snake_game(
        self, operations: list[str], inputs: list[list], expected: list[int | None]
    ):
        result, _ = run_design_snake_game(SnakeGame, operations, inputs)
        assert_design_snake_game(result, expected)
