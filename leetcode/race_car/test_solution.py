import pytest

from leetcode_py import logged_test

from .helpers import assert_racecar, run_racecar
from .solution import Solution


class TestRaceCar:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "target, expected",
        [
            (1, 1),
            (2, 4),
            (3, 2),
            (4, 5),
            (5, 7),
            (6, 5),
            (7, 3),
            (10, 7),
            (15, 4),
            (16, 7),
            (17, 9),
            (20, 12),
            (31, 5),
            (63, 6),
            (100, 19),
            (127, 7),
            (200, 22),
            (255, 8),
            (342, 26),
            (511, 9),
            (1000, 23),
            (1666, 30),
            (2731, 44),
            (4095, 12),
            (7777, 39),
            (10000, 45),
        ],
    )
    def test_racecar(self, target: int, expected: int):
        result = run_racecar(Solution, target)
        assert_racecar(result, expected)
