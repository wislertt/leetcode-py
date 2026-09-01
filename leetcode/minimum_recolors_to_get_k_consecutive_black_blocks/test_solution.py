import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_recolors, run_minimum_recolors
from .solution import Solution


class TestMinimumRecolorsToGetKConsecutiveBlackBlocks:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "blocks, k, expected",
        [
            ("WBBWWBBWBW", 7, 3),
            ("WBWBBBW", 2, 0),
            ("B", 1, 0),
            ("W", 1, 1),
            ("WB", 2, 1),
            ("BB", 2, 0),
            ("WWWW", 4, 4),
            ("BBBB", 4, 0),
            ("WBBW", 3, 1),
            ("BWBWBWBW", 2, 1),
            ("WBWBWBWB", 3, 1),
            ("WWBBWWBB", 5, 2),
            ("BBBWWBB", 4, 1),
            ("WB", 1, 0),
            ("BWBBBWBBWBWBWBBW", 7, 2),
            ("BWBW", 2, 1),
            ("WBW", 1, 0),
            ("W", 1, 1),
        ],
    )
    def test_minimum_recolors(self, blocks: str, k: int, expected: int):
        result = run_minimum_recolors(Solution, blocks, k)
        assert_minimum_recolors(result, expected)
