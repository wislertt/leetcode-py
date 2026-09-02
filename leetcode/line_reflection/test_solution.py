import pytest

from leetcode_py import logged_test

from .helpers import assert_is_reflected, run_is_reflected
from .solution import Solution


class TestLineReflection:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "points, expected",
        [
            ([[1, 1], [-1, 1]], True),
            ([[1, 1], [-1, -1]], False),
            ([[0, 0]], True),
            ([[1, 1], [1, 1]], True),
            ([[1, 1], [-1, 1], [2, 0], [-2, 0]], True),
            ([[1, 1], [-1, 1], [2, 0], [-1, 0]], False),
            (
                [
                    [-16, 5],
                    [-13, -9],
                    [-7, -14],
                    [-18, -4],
                    [-19, -17],
                    [16, 5],
                    [13, -9],
                    [7, -14],
                    [18, -4],
                    [19, -17],
                ],
                True,
            ),
            ([[1, 2], [0, 2]], True),
            ([[5, 0], [5, 1]], True),
            ([[0, 0], [0, 1], [0, 2]], True),
            ([[0, 10], [-3, 10]], True),
            ([[-1, 0], [-3, 0]], True),
            ([[1, 0], [-1, 0], [3, 0], [-3, 0], [0, 0]], True),
            ([[2, 3], [1, 3], [-1, 3]], False),
        ],
    )
    def test_is_reflected(self, points: list[list[int]], expected: bool):
        result = run_is_reflected(Solution, points)
        assert_is_reflected(result, expected)
