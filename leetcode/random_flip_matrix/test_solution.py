import pytest

from leetcode_py import logged_test

from .helpers import assert_flip_operations, run_flip_operations
from .solution import Solution


class TestRandomFlipMatrix:
    @logged_test
    @pytest.mark.parametrize(
        "m, n, operations, expected",
        [
            (1, 1, ["Solution", "flip"], [[0, 0]]),
            (1, 1, ["Solution", "flip", "reset", "flip"], [[0, 0], None, [0, 0]]),
            (
                1,
                1,
                ["Solution", "flip", "reset", "flip", "reset", "flip"],
                [None, None, None, None, None],
            ),
            (1, 2, ["Solution", "flip"], [None]),
            (1, 2, ["Solution", "flip", "flip"], [None, None]),
            (1, 3, ["Solution", "flip", "flip", "flip"], [None, None, None]),
            (2, 1, ["Solution", "flip", "flip"], [None, None]),
            (3, 1, ["Solution", "flip", "flip", "flip"], [None, None, None]),
            (2, 2, ["Solution", "flip"], [None]),
            (2, 2, ["Solution", "flip", "flip", "flip", "flip"], [None, None, None, None]),
            (2, 2, ["Solution", "flip", "flip", "reset", "flip"], [None, None, None, None]),
            (2, 2, ["Solution", "reset"], [None]),
            (3, 3, ["Solution", "flip", "flip", "flip"], [None, None, None]),
            (2, 3, ["Solution", "flip", "reset", "flip", "flip"], [None, None, None, None]),
            (4, 1, ["Solution", "flip", "flip", "flip", "flip"], [None, None, None, None]),
            (
                5,
                5,
                ["Solution", "flip", "flip", "flip", "reset", "flip"],
                [None, None, None, None, None],
            ),
            (10000, 10000, ["Solution", "flip", "flip"], [None, None]),
            (1, 10000, ["Solution", "flip", "flip"], [None, None]),
        ],
    )
    def test_flip_operations(
        self, m: int, n: int, operations: list[str], expected: list[list[int] | None]
    ):
        result, _ = run_flip_operations(Solution, m, n, operations)
        assert_flip_operations(result, expected, m, n)
