import pytest

from leetcode_py import logged_test

from .helpers import assert_find_paths, run_find_paths
from .solution import Solution


class TestOutOfBoundaryPaths:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "m, n, max_move, start_row, start_column, expected",
        [
            (2, 2, 2, 0, 0, 6),
            (1, 3, 3, 0, 1, 12),
            (1, 1, 1, 0, 0, 4),
            (1, 1, 0, 0, 0, 0),
            (2, 2, 0, 1, 1, 0),
            (3, 3, 4, 1, 1, 52),
            (2, 3, 5, 0, 2, 78),
            (3, 2, 3, 2, 0, 13),
            (1, 4, 6, 0, 3, 48),
            (4, 1, 5, 3, 0, 29),
            (5, 5, 10, 2, 2, 79840),
            (3, 3, 8, 0, 0, 1756),
            (2, 2, 50, 0, 0, 797922653),
            (5, 4, 20, 2, 3, 891314074),
        ],
    )
    def test_find_paths(
        self, m: int, n: int, max_move: int, start_row: int, start_column: int, expected: int
    ):
        result = run_find_paths(Solution, m, n, max_move, start_row, start_column)
        assert_find_paths(result, expected)
