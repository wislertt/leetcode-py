import pytest

from leetcode_py import logged_test

from .helpers import assert_num_water_bottles, run_num_water_bottles
from .solution import Solution


class TestWaterBottles:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num_bottles, num_exchange, expected",
        [
            (9, 3, 13),
            (15, 4, 19),
            (1, 2, 1),
            (1, 100, 1),
            (2, 2, 3),
            (2, 3, 2),
            (3, 2, 5),
            (4, 2, 7),
            (5, 5, 6),
            (10, 10, 11),
            (11, 5, 13),
            (13, 4, 17),
            (29, 9, 32),
            (100, 2, 199),
            (100, 100, 101),
            (100, 99, 101),
            (61, 3, 91),
            (32, 5, 39),
            (26, 65, 26),
            (95, 34, 97),
            (31, 14, 33),
            (91, 9, 102),
        ],
    )
    def test_num_water_bottles(self, num_bottles: int, num_exchange: int, expected: int):
        result = run_num_water_bottles(Solution, num_bottles, num_exchange)
        assert_num_water_bottles(result, expected)
