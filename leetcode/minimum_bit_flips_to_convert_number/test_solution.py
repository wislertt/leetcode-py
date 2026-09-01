import pytest

from leetcode_py import logged_test

from .helpers import assert_min_bit_flips, run_min_bit_flips
from .solution import Solution


class TestMinimumBitFlipsToConvertNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "start, goal, expected",
        [
            (10, 7, 3),
            (3, 4, 3),
            (0, 0, 0),
            (1, 0, 1),
            (0, 1, 1),
            (1, 1, 0),
            (2, 1, 2),
            (2, 4, 2),
            (7, 10, 3),
            (5, 5, 0),
            (0, 109, 5),
            (1000000000, 999999999, 10),
            (109, 109, 0),
            (15, 0, 4),
            (0, 15, 4),
            (123456789, 987654321, 15),
            (634299979, 507333477, 21),
            (219763584, 981865221, 15),
            (564858347, 927327245, 19),
            (806020841, 357252220, 14),
            (175593312, 297145375, 17),
            (358957714, 991723447, 17),
            (83136965, 811909648, 14),
            (328571609, 119393132, 12),
        ],
    )
    def test_min_bit_flips(self, start: int, goal: int, expected: int):
        result = run_min_bit_flips(Solution, start, goal)
        assert_min_bit_flips(result, expected)
