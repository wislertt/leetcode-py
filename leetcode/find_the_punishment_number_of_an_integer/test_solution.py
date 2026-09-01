import pytest

from leetcode_py import logged_test

from .helpers import assert_punishment_number, run_punishment_number
from .solution import Solution


class TestFindThePunishmentNumberOfAnInteger:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (1, 1),
            (2, 1),
            (3, 1),
            (4, 1),
            (5, 1),
            (9, 82),
            (10, 182),
            (11, 182),
            (15, 182),
            (20, 182),
            (25, 182),
            (37, 1478),
            (45, 3503),
            (50, 3503),
            (75, 6528),
            (99, 31334),
            (100, 41334),
            (121, 41334),
            (200, 41334),
            (500, 772866),
            (750, 2154349),
            (999, 9804657),
            (1000, 10804657),
        ],
    )
    def test_punishment_number(self, n: int, expected: int):
        result = run_punishment_number(Solution, n)
        assert_punishment_number(result, expected)
