import pytest

from leetcode_py import logged_test

from .helpers import assert_champagne_tower, run_champagne_tower
from .solution import Solution


class TestChampagneTower:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "poured, query_row, query_glass, expected",
        [
            (1, 1, 1, 0.0),
            (2, 1, 1, 0.5),
            (100000009, 33, 17, 1.0),
            (0, 0, 0, 0.0),
            (1, 0, 0, 1.0),
            (3, 1, 1, 1.0),
            (4, 2, 1, 0.5),
            (4, 2, 0, 0.25),
            (1000000000, 25, 12, 1.0),
            (5, 3, 2, 0.0),
            (2, 0, 0, 1.0),
            (6, 2, 2, 0.75),
            (100, 50, 25, 0.0),
            (7, 3, 0, 0.0),
        ],
    )
    def test_champagne_tower(self, poured: int, query_row: int, query_glass: int, expected: float):
        result = run_champagne_tower(Solution, poured, query_row, query_glass)
        assert_champagne_tower(result, expected)
