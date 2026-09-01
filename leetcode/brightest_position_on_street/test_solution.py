import pytest

from leetcode_py import logged_test

from .helpers import assert_brightest_position, run_brightest_position
from .solution import Solution


class TestBrightestPositionOnStreet:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "lights, expected",
        [
            ([[-3, 2], [1, 2], [3, 3]], -1),
            ([[1, 0], [0, 1]], 1),
            ([[1, 2]], -1),
            ([[0, 0]], 0),
            ([[5, 0]], 5),
            ([[0, 100000000]], -100000000),
            ([[-100000000, 0]], -100000000),
            ([[100000000, 100000000]], 0),
            ([[1, 1], [1, 1]], 0),
            ([[3, 2], [4, 2]], 2),
            ([[-1, 0], [-1, 0], [-1, 0]], -1),
            ([[0, 3], [2, 1], [4, 2], [6, 1]], 2),
            ([[0, 1], [-7, 3], [7, 4], [-6, 2]], -8),
            ([[1, 3], [-6, 1], [-3, 6]], -7),
            ([[-5, 5]], -10),
            ([[-7, 4], [6, 0], [-2, 4]], -6),
            ([[0, 4], [2, 5], [3, 6], [4, 5]], -1),
            ([[-1, 1]], -2),
        ],
    )
    def test_brightest_position(self, lights: list[list[int]], expected: int):
        result = run_brightest_position(Solution, lights)
        assert_brightest_position(result, expected)
