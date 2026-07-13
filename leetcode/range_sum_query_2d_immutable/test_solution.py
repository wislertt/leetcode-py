import pytest

from leetcode_py import logged_test

from .helpers import assert_num_matrix, run_num_matrix
from .solution import NumMatrix


class TestRangeSumQuery2DImmutable:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"],
                [
                    [
                        [
                            [3, 0, 1, 4, 2],
                            [5, 6, 3, 2, 1],
                            [1, 2, 0, 1, 5],
                            [4, 1, 0, 1, 7],
                            [1, 0, 3, 0, 5],
                        ]
                    ],
                    [2, 1, 4, 3],
                    [1, 1, 2, 2],
                    [1, 2, 2, 4],
                ],
                [None, 8, 11, 12],
            ),
            (
                ["NumMatrix", "sumRegion", "sumRegion"],
                [[[[1, 2], [3, 4]]], [0, 0, 1, 1], [0, 0, 0, 0]],
                [None, 10, 1],
            ),
            (["NumMatrix", "sumRegion"], [[[[5]]], [0, 0, 0, 0]], [None, 5]),
            (
                ["NumMatrix", "sumRegion", "sumRegion"],
                [[[[-1, -2], [-3, -4]]], [0, 0, 1, 1], [0, 0, 0, 1]],
                [None, -10, -3],
            ),
            (
                ["NumMatrix", "sumRegion", "sumRegion"],
                [[[[1, 2, 3, 4]]], [0, 0, 0, 3], [0, 1, 0, 2]],
                [None, 10, 5],
            ),
            (
                ["NumMatrix", "sumRegion", "sumRegion"],
                [[[[1], [2], [3], [4]]], [0, 0, 3, 0], [1, 0, 2, 0]],
                [None, 10, 5],
            ),
            (
                ["NumMatrix", "sumRegion", "sumRegion"],
                [
                    [
                        [
                            [3, 0, 1, 4, 2],
                            [5, 6, 3, 2, 1],
                            [1, 2, 0, 1, 5],
                            [4, 1, 0, 1, 7],
                            [1, 0, 3, 0, 5],
                        ]
                    ],
                    [0, 0, 4, 4],
                    [0, 0, 0, 0],
                ],
                [None, 58, 3],
            ),
            (
                ["NumMatrix", "sumRegion"],
                [
                    [
                        [
                            [3, 0, 1, 4, 2],
                            [5, 6, 3, 2, 1],
                            [1, 2, 0, 1, 5],
                            [4, 1, 0, 1, 7],
                            [1, 0, 3, 0, 5],
                        ]
                    ],
                    [0, 0, 2, 2],
                ],
                [None, 21],
            ),
            (["NumMatrix", "sumRegion"], [[[[0, 0], [0, 0]]], [0, 0, 1, 1]], [None, 0]),
            (
                ["NumMatrix", "sumRegion", "sumRegion"],
                [[[[1, 1, 1], [1, 1, 1], [1, 1, 1]]], [0, 0, 2, 2], [1, 1, 2, 2]],
                [None, 9, 4],
            ),
            (
                ["NumMatrix", "sumRegion"],
                [
                    [
                        [
                            [3, 0, 1, 4, 2],
                            [5, 6, 3, 2, 1],
                            [1, 2, 0, 1, 5],
                            [4, 1, 0, 1, 7],
                            [1, 0, 3, 0, 5],
                        ]
                    ],
                    [2, 1, 2, 3],
                ],
                [None, 3],
            ),
            (
                ["NumMatrix", "sumRegion"],
                [
                    [
                        [
                            [3, 0, 1, 4, 2],
                            [5, 6, 3, 2, 1],
                            [1, 2, 0, 1, 5],
                            [4, 1, 0, 1, 7],
                            [1, 0, 3, 0, 5],
                        ]
                    ],
                    [0, 2, 4, 2],
                ],
                [None, 7],
            ),
            (
                ["NumMatrix", "sumRegion", "sumRegion"],
                [[[[100, 200], [300, 400]]], [0, 0, 1, 1], [0, 1, 1, 1]],
                [None, 1000, 600],
            ),
            (
                ["NumMatrix", "sumRegion", "sumRegion"],
                [[[[1, 2, 3], [4, 5, 6]]], [0, 0, 1, 2], [0, 2, 1, 2]],
                [None, 21, 9],
            ),
            (
                ["NumMatrix", "sumRegion", "sumRegion"],
                [[[[1, -2, 3], [-4, 5, -6], [7, -8, 9]]], [0, 0, 2, 2], [0, 0, 0, 2]],
                [None, 5, 2],
            ),
        ],
    )
    def test_num_matrix_operations(
        self, operations: list[str], inputs: list[list], expected: list[int | None]
    ):
        result, _ = run_num_matrix(NumMatrix, operations, inputs)
        assert_num_matrix(result, expected)
