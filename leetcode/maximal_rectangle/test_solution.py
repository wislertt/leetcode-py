import pytest

from leetcode_py import logged_test

from .helpers import assert_maximal_rectangle, run_maximal_rectangle
from .solution import Solution


class TestMaximalRectangle:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            ([["1", "0", "1", "1"], ["1", "0", "1", "1"], ["1", "1", "1", "1"]], 6),
            ([["0"]], 0),
            ([["1"]], 1),
            ([["1", "1"], ["1", "1"]], 4),
            ([["0", "0"], ["0", "0"]], 0),
            ([["1", "0"], ["0", "1"]], 1),
            ([["1", "1"], ["1", "0"]], 2),
            ([["1"], ["1"], ["1"]], 3),
            ([["1", "1", "1"]], 3),
            ([["0", "1"], ["1", "1"], ["1", "1"]], 4),
            (
                [
                    ["1", "0", "1", "0"],
                    ["1", "0", "1", "1"],
                    ["1", "1", "1", "1"],
                    ["0", "1", "1", "1"],
                ],
                6,
            ),
            ([["0", "0", "0"], ["0", "1", "1"], ["0", "1", "1"]], 4),
            ([["1", "0", "1", "1", "1"], ["0", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"]], 9),
            ([["1"], ["0"]], 1),
            ([["1", "0", "1", "0"], ["1", "1", "0", "0"]], 2),
            ([["1"], ["1"], ["1"], ["1"], ["0"]], 4),
            ([["1", "0"], ["1", "0"]], 2),
            ([["0", "0", "0", "1"]], 1),
        ],
    )
    def test_maximal_rectangle(self, matrix: list[list[str]], expected: int):
        result = run_maximal_rectangle(Solution, matrix)
        assert_maximal_rectangle(result, expected)
