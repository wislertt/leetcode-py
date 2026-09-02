import pytest

from leetcode_py import logged_test

from .helpers import assert_find_min_step, run_find_min_step
from .solution import Solution


class TestZumaGame:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "board, hand, expected",
        [
            ("WRRBBW", "RB", -1),
            ("WWRRBBWW", "WRBRW", 2),
            ("G", "GGGGG", 2),
            ("G", "GG", 2),
            ("WW", "WW", 1),
            ("WR", "WRW", -1),
            ("WWRRBBWW", "RWB", 2),
            ("WWRRBBWW", "WWRRB", 2),
            ("RRWWRRBBRR", "WB", -1),
            ("RRYGGYYRRYYGGYRR", "GGBBB", -1),
            ("BWRRBBW", "RWB", -1),
            ("WWBBWBBWW", "WWBBB", 2),
            ("RRGGRR", "RRGGG", 1),
            ("YRRYYRRY", "YYRRR", 2),
            ("RYYRRYYR", "YRRYY", 2),
            ("GGBGGBGG", "GBGGB", 2),
            ("RBYYWYRWBBRRWYYG", "RWYBG", -1),
            ("GGRRWWGGWWGGRRG", "RGRRG", 2),
            ("WWYYRWWYYWRR", "WYYRW", 3),
            ("WRRBBW", "RBW", 3),
            ("BBWWBB", "BWB", 1),
            ("RRGGYYRR", "GGYYR", 2),
        ],
    )
    def test_find_min_step(self, board: str, hand: str, expected: int):
        result = run_find_min_step(Solution, board, hand)
        assert_find_min_step(result, expected)
