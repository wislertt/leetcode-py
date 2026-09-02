import pytest

from leetcode_py import logged_test

from .helpers import assert_minimize_xor, run_minimize_xor
from .solution import Solution


class TestMinimizeXor:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num1, num2, expected",
        [
            (1, 2, 1),
            (1, 1, 1),
            (2, 1, 2),
            (3, 1, 2),
            (4, 1, 4),
            (1000000000, 536870912, 536870912),
            (1000000000, 1, 536870912),
            (1, 12, 3),
            (3, 5, 3),
            (5, 3, 5),
            (65, 65, 65),
            (93, 40, 80),
            (7, 7, 7),
            (11, 23, 15),
            (1, 1000000000, 8191),
            (1000000000, 1000000000, 1000000000),
            (377557700, 830082661, 377557759),
            (123456789, 987654321, 123456791),
            (79707355, 871857972, 79953919),
            (536870911, 536870911, 536870911),
        ],
    )
    def test_minimize_xor(self, num1: int, num2: int, expected: int):
        result = run_minimize_xor(Solution, num1, num2)
        assert_minimize_xor(result, expected)
