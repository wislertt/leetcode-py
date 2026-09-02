import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_steps, run_minimum_steps
from .solution import Solution


class TestSeparateBlackAndWhiteBalls:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("101", 1),
            ("100", 2),
            ("0111", 0),
            ("1", 0),
            ("0", 0),
            ("10", 1),
            ("01", 0),
            ("110", 2),
            ("1100", 4),
            ("111000", 9),
            ("011010", 5),
            ("1010101", 6),
            ("1111", 0),
            ("0000", 0),
            ("0011", 0),
            ("0101010101010101010101010101010101010101", 190),
            ("1101111000110100010101111000000111", 166),
            ("0110100", 8),
            ("00101001", 5),
            ("00010", 1),
            ("00011100011110", 16),
        ],
    )
    def test_minimum_steps(self, s: str, expected: int):
        result = run_minimum_steps(Solution, s)
        assert_minimum_steps(result, expected)
