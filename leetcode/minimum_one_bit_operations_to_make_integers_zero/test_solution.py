import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_one_bit_operations, run_minimum_one_bit_operations
from .solution import Solution


class TestMinimumOneBitOperationsToMakeIntegersZero:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            (3, 2),
            (6, 4),
            (0, 0),
            (1, 1),
            (2, 3),
            (4, 7),
            (5, 6),
            (7, 5),
            (8, 15),
            (15, 10),
            (16, 31),
            (31, 21),
            (32, 63),
            (63, 42),
            (255, 170),
            (256, 511),
            (1023, 682),
            (1000000000, 756249599),
            (999999999, 756248917),
            (536870911, 357913941),
            (536870912, 1073741823),
            (123456789, 93489638),
            (999999998, 756248916),
        ],
    )
    def test_minimum_one_bit_operations(self, n: int, expected: int):
        result = run_minimum_one_bit_operations(Solution, n)
        assert_minimum_one_bit_operations(result, expected)
