import pytest

from leetcode_py import logged_test

from .helpers import assert_num_rolls_to_target, run_num_rolls_to_target
from .solution import Solution


class TestNumberOfDiceRollsWithTargetSumTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, target, expected",
        [
            (1, 6, 3, 1),
            (2, 6, 7, 6),
            (30, 30, 500, 222616187),
            (1, 1, 1, 1),
            (1, 6, 7, 0),
            (2, 2, 3, 2),
            (2, 2, 5, 0),
            (3, 4, 5, 6),
            (2, 12, 13, 12),
            (3, 6, 18, 1),
            (3, 6, 2, 0),
            (4, 6, 24, 1),
            (5, 5, 13, 320),
            (7, 10, 35, 465795),
            (29, 30, 30, 29),
            (30, 30, 900, 1),
        ],
    )
    def test_num_rolls_to_target(self, n: int, k: int, target: int, expected: int):
        result = run_num_rolls_to_target(Solution, n, k, target)
        assert_num_rolls_to_target(result, expected)
