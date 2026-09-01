import pytest

from leetcode_py import logged_test

from .helpers import assert_count_unguarded, run_count_unguarded
from .solution import Solution


class TestCountUnguardedCellsInTheGrid:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "m, n, guards, walls, expected",
        [
            (4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]], 7),
            (3, 3, [[1, 1]], [[0, 1], [1, 0], [2, 1], [1, 2]], 4),
            (1, 2, [[0, 0]], [[0, 1]], 0),
            (2, 2, [[0, 0]], [[1, 1]], 0),
            (2, 3, [[0, 1]], [[1, 2]], 1),
            (1, 5, [[0, 0], [0, 2]], [[0, 4]], 0),
            (3, 3, [[0, 0]], [[1, 0]], 5),
            (1, 3, [[0, 1]], [[0, 2]], 0),
            (2, 2, [[0, 1], [1, 0]], [[0, 0], [1, 1]], 0),
            (3, 4, [[0, 3], [2, 0]], [[1, 1], [2, 3]], 1),
            (4, 4, [[0, 0], [3, 3]], [[1, 1], [2, 2]], 2),
            (2, 5, [[0, 0], [1, 4]], [[1, 0], [0, 4]], 0),
            (3, 3, [[1, 0]], [[0, 2], [2, 2]], 2),
            (5, 5, [[0, 4], [3, 0], [0, 2], [4, 4], [3, 2]], [[0, 3], [3, 4]], 4),
            (4, 4, [[3, 1], [1, 0], [1, 1], [2, 2], [3, 2]], [[0, 3]], 0),
            (2, 1, [[0, 0]], [[1, 0]], 0),
            (2, 1, [[0, 0]], [[1, 0]], 0),
            (3, 1, [[0, 0]], [[2, 0]], 0),
            (5, 3, [[0, 1]], [[4, 1]], 8),
            (1, 4, [[0, 3]], [[0, 1]], 1),
        ],
    )
    def test_count_unguarded(
        self, m: int, n: int, guards: list[list[int]], walls: list[list[int]], expected: int
    ):
        result = run_count_unguarded(Solution, m, n, guards, walls)
        assert_count_unguarded(result, expected)
