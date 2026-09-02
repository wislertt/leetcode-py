import pytest

from leetcode_py import logged_test

from .helpers import assert_colored_cells, run_colored_cells
from .solution import Solution


class TestCountTotalNumberOfColoredCells:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 5),
            (3, 13),
            (4, 25),
            (5, 41),
            (6, 61),
            (7, 85),
            (8, 113),
            (9, 145),
            (10, 181),
            (11, 221),
            (12, 265),
            (50, 4901),
            (1000, 1998001),
            (100000, 19999800001),
        ],
    )
    def test_colored_cells(self, n: int, expected: int):
        result = run_colored_cells(Solution, n)
        assert_colored_cells(result, expected)
