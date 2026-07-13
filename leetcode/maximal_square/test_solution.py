import pytest

from leetcode_py import logged_test

from .helpers import assert_maximal_square, run_maximal_square
from .solution import Solution


class TestMaximalSquare:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            (
                [
                    ["1", "0", "1", "0", "0"],
                    ["1", "0", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "0", "0", "1", "0"],
                ],
                4,
            ),
            ([["0", "1"], ["1", "0"]], 1),
            ([["0"]], 0),
            ([["1"]], 1),
            ([["1", "1"], ["1", "1"]], 4),
            ([["1", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]], 9),
            ([["1", "0", "1"], ["1", "1", "1"], ["1", "1", "1"]], 4),
            ([["0", "0"], ["0", "0"]], 0),
            ([["1", "1"], ["1", "0"]], 1),
            ([["1", "1"], ["0", "1"]], 1),
            (
                [
                    ["1", "1", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                    ["1", "1", "1", "1", "1"],
                ],
                25,
            ),
            ([["1", "1", "1", "1"], ["1", "1", "1", "1"], ["1", "1", "1", "1"]], 9),
            ([["0", "1", "1"], ["1", "1", "1"], ["1", "1", "1"]], 4),
            ([["1", "1", "1", "0", "0"], ["1", "1", "1", "1", "1"], ["1", "1", "1", "1", "1"]], 9),
            ([["0", "1"]], 1),
        ],
    )
    def test_maximal_square(self, matrix: list[list[str]], expected: int):
        result = run_maximal_square(Solution, matrix)
        assert_maximal_square(result, expected)
