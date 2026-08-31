import pytest

from leetcode_py import logged_test

from .helpers import assert_moving_average, run_moving_average
from .solution import MovingAverage


class TestMovingAverageFromDataStream:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (
                ["MovingAverage", "next", "next", "next", "next"],
                [[3], [1], [10], [3], [5]],
                [None, 1.0, 5.5, 14 / 3, 6.0],
            ),
            (
                ["MovingAverage", "next", "next", "next", "next"],
                [[2], [1], [2], [3], [4]],
                [None, 1.0, 1.5, 2.5, 3.5],
            ),
            (
                ["MovingAverage", "next", "next", "next"],
                [[1], [5], [6], [7]],
                [None, 5.0, 6.0, 7.0],
            ),
            (
                ["MovingAverage", "next", "next", "next", "next"],
                [[3], [3], [6], [9], [12]],
                [None, 3.0, 4.5, 6.0, 9.0],
            ),
            (
                ["MovingAverage", "next", "next", "next"],
                [[2], [-2], [-4], [0]],
                [None, -2.0, -3.0, -2.0],
            ),
            (
                ["MovingAverage", "next", "next", "next", "next", "next"],
                [[4], [1], [2], [3], [4], [5]],
                [None, 1.0, 1.5, 2.0, 2.5, 3.5],
            ),
            (["MovingAverage", "next", "next"], [[5], [10], [20]], [None, 10.0, 15.0]),
            (
                ["MovingAverage", "next", "next", "next"],
                [[3], [0], [0], [0]],
                [None, 0.0, 0.0, 0.0],
            ),
            (
                ["MovingAverage", "next", "next", "next"],
                [[2], [100], [-100], [100]],
                [None, 100.0, 0.0, 0.0],
            ),
            (
                ["MovingAverage", "next", "next", "next", "next", "next"],
                [[3], [5], [10], [15], [20], [25]],
                [None, 5.0, 7.5, 10.0, 15.0, 20.0],
            ),
            (["MovingAverage", "next"], [[1], [-1]], [None, -1.0]),
            (
                ["MovingAverage", "next", "next", "next", "next", "next"],
                [[10], [1], [2], [3], [4], [5]],
                [None, 1.0, 1.5, 2.0, 2.5, 3.0],
            ),
            (
                ["MovingAverage", "next", "next", "next", "next"],
                [[2], [7], [7], [7], [7]],
                [None, 7.0, 7.0, 7.0, 7.0],
            ),
            (
                ["MovingAverage", "next", "next", "next", "next"],
                [[3], [3], [3], [6], [9]],
                [None, 3.0, 3.0, 4.0, 6.0],
            ),
            (
                ["MovingAverage", "next", "next", "next", "next", "next"],
                [[4], [8], [4], [2], [1], [0]],
                [None, 8.0, 6.0, 14 / 3, 3.75, 1.75],
            ),
        ],
    )
    def test_moving_average(
        self, operations: list[str], inputs: list[list[int]], expected: list[float | None]
    ):
        result, _ = run_moving_average(MovingAverage, operations, inputs)
        assert_moving_average(result, expected)
