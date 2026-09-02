import pytest

from leetcode_py import logged_test

from .helpers import assert_can_measure_water, run_can_measure_water
from .solution import Solution


class TestWaterAndJugProblem:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "x, y, target, expected",
        [
            (3, 5, 4, True),
            (2, 6, 5, False),
            (1, 2, 3, True),
            (1, 1, 1, True),
            (1, 1, 2, True),
            (1, 2, 4, False),
            (3, 5, 8, True),
            (3, 5, 9, False),
            (4, 6, 8, True),
            (4, 6, 3, False),
            (11, 13, 12, True),
            (34, 58, 7, False),
            (7, 9, 5, True),
            (6, 9, 4, False),
            (220, 330, 550, True),
            (220, 330, 110, True),
            (220, 330, 115, False),
            (999, 998, 998, True),
            (1000, 999, 1, True),
            (1000, 1000, 999, False),
            (11, 5, 5, True),
            (5, 10, 7, False),
            (9, 7, 13, True),
            (11, 9, 6, True),
            (1, 4, 7, False),
            (2, 1, 1, True),
        ],
    )
    def test_can_measure_water(self, x: int, y: int, target: int, expected: bool):
        result = run_can_measure_water(Solution, x, y, target)
        assert_can_measure_water(result, expected)
