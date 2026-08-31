import pytest

from leetcode_py import logged_test

from .helpers import assert_flatten_2d_vector, run_flatten_2d_vector
from .solution import Vector2D


class TestFlatten2DVector:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (["Vector2D", "next", "has_next"], [[[1]], [], []], [None, 1, False]),
            (["Vector2D", "next", "next", "has_next"], [[[1, 2]], [], [], []], [None, 1, 2, False]),
            (
                ["Vector2D", "next", "has_next", "next"],
                [[[1], [2]], [], [], []],
                [None, 1, True, 2],
            ),
            (["Vector2D", "has_next", "next"], [[[], [1]], [], []], [None, True, 1]),
            (["Vector2D", "next", "has_next"], [[[1], []], [], []], [None, 1, False]),
            (["Vector2D", "has_next"], [[[], []], []], [None, False]),
            (["Vector2D", "has_next"], [[[]], []], [None, False]),
            (["Vector2D", "next", "next", "next"], [[[1, 2], [3]], [], [], []], [None, 1, 2, 3]),
            (
                ["Vector2D", "next", "next", "next"],
                [[[-5], [0], [5]], [], [], []],
                [None, -5, 0, 5],
            ),
            (
                ["Vector2D", "next", "next", "has_next"],
                [[[2, 4], [6, 8]], [], [], []],
                [None, 2, 4, True],
            ),
            (["Vector2D", "has_next", "next"], [[[1], [2], [3]], [], []], [None, True, 1]),
            (["Vector2D", "next", "next", "next"], [[[7, 8, 9]], [], [], []], [None, 7, 8, 9]),
            (["Vector2D", "next"], [[[0]], []], [None, 0]),
            (["Vector2D", "has_next"], [[], []], [None, False]),
        ],
    )
    def test_flatten_2d_vector(
        self, operations: list[str], inputs: list[list], expected: list[int | bool | None]
    ):
        result, _ = run_flatten_2d_vector(Vector2D, operations, inputs)
        assert_flatten_2d_vector(result, expected)
