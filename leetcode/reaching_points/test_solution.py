import pytest

from leetcode_py import logged_test

from .helpers import assert_reaching_points, run_reaching_points
from .solution import Solution


class TestReachingPoints:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "sx, sy, tx, ty, expected",
        [
            (1, 1, 3, 5, True),
            (1, 1, 2, 2, False),
            (1, 1, 1, 1, True),
            (1, 1, 2, 3, True),
            (1, 1, 3, 3, False),
            (2, 1, 2, 7, True),
            (2, 1, 2, 6, False),
            (1, 2, 7, 2, True),
            (3, 3, 12, 9, True),
            (3, 3, 12, 10, False),
            (1, 1, 4, 7, True),
            (5, 2, 5, 12, True),
            (5, 2, 5, 13, False),
            (9, 5, 9, 14, True),
            (1, 1, 1000000000, 1, True),
            (2, 3, 1000000000, 3, False),
            (1, 1, 1000000000, 1000000000, False),
            (999999937, 1, 1000000000, 1000000000, False),
            (4, 6, 23, 23, False),
            (3, 8, 7, 14, False),
            (7, 2, 20, 3, False),
            (2, 1, 6, 4, False),
        ],
    )
    def test_reaching_points(self, sx: int, sy: int, tx: int, ty: int, expected: bool):
        result = run_reaching_points(Solution, sx, sy, tx, ty)
        assert_reaching_points(result, expected)
