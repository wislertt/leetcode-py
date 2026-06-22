from typing import Any

import pytest

from leetcode_py import logged_test

from .helpers import assert_detect_squares, run_detect_squares
from .solution import DetectSquares


class TestDetectSquares:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"],
                [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]],
                [None, None, None, None, 1, 0, None, 2],
            ),
            (["DetectSquares", "add", "count"], [[], [[0, 0]], [[0, 0]]], [None, None, 0]),
            (
                ["DetectSquares", "add", "add", "add", "count"],
                [[], [[0, 0]], [[0, 2]], [[2, 0]], [[2, 2]]],
                [None, None, None, None, 1],
            ),
            (
                ["DetectSquares", "add", "add", "add", "add", "count"],
                [[], [[0, 0]], [[0, 0]], [[0, 2]], [[2, 0]], [[2, 2]]],
                [None, None, None, None, None, 2],
            ),
            (
                ["DetectSquares", "add", "add", "add", "count"],
                [[], [[1, 1]], [[1, 3]], [[3, 1]], [[3, 3]]],
                [None, None, None, None, 1],
            ),
            (
                ["DetectSquares", "add", "add", "add", "count"],
                [[], [[0, 0]], [[1, 0]], [[2, 0]], [[0, 1]]],
                [None, None, None, None, 0],
            ),
            (
                ["DetectSquares", "add", "add", "add", "count"],
                [[], [[10, 10]], [[10, 20]], [[20, 10]], [[20, 20]]],
                [None, None, None, None, 1],
            ),
            (
                ["DetectSquares", "add", "add", "add", "add", "count"],
                [[], [[0, 0]], [[2, 2]], [[0, 2]], [[2, 0]], [[0, 0]]],
                [None, None, None, None, None, 1],
            ),
            (
                ["DetectSquares", "add", "add", "add", "add", "add", "add", "count", "count"],
                [
                    [],
                    [[1, 1]],
                    [[1, 3]],
                    [[3, 1]],
                    [[5, 5]],
                    [[5, 7]],
                    [[7, 5]],
                    [[3, 3]],
                    [[7, 7]],
                ],
                [None, None, None, None, None, None, None, 1, 1],
            ),
            (
                [
                    "DetectSquares",
                    "add",
                    "add",
                    "add",
                    "add",
                    "add",
                    "add",
                    "add",
                    "add",
                    "add",
                    "count",
                ],
                [
                    [],
                    [[0, 0]],
                    [[0, 0]],
                    [[0, 0]],
                    [[0, 2]],
                    [[0, 2]],
                    [[2, 0]],
                    [[2, 0]],
                    [[2, 0]],
                    [[2, 0]],
                    [[2, 2]],
                ],
                [None, None, None, None, None, None, None, None, None, None, 24],
            ),
            (["DetectSquares", "count"], [[], [[5, 5]]], [None, 0]),
            (["DetectSquares", "add", "count"], [[], [[3, 3]], [[3, 3]]], [None, None, 0]),
            (
                ["DetectSquares", "add", "add", "add", "count"],
                [[], [[0, 0]], [[0, 3]], [[5, 0]], [[5, 3]]],
                [None, None, None, None, 0],
            ),
            (
                ["DetectSquares", "add", "add", "add", "count"],
                [[], [[2, 2]], [[2, 4]], [[4, 2]], [[4, 4]]],
                [None, None, None, None, 1],
            ),
        ],
    )
    def test_detect_squares(self, operations: list[str], inputs: list[Any], expected: list[Any]):
        result = run_detect_squares(DetectSquares, operations, inputs)
        assert_detect_squares(result, expected)
