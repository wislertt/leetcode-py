import pytest

from leetcode_py import logged_test

from .helpers import assert_min_flips, run_min_flips
from .solution import Solution


class TestMinimumNumberOfFlipsToMakeTheBinaryStringAlternating:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("111000", 2),
            ("010", 0),
            ("1110", 1),
            ("0", 0),
            ("1", 0),
            ("00", 1),
            ("11", 1),
            ("01", 0),
            ("10", 0),
            ("0000", 2),
            ("1111", 2),
            ("0101", 0),
            ("1010", 0),
            ("1100", 2),
            ("000111", 2),
            ("1001", 2),
            ("10010010100", 3),
            ("10101110", 1),
            ("000", 1),
            ("10010110000110", 7),
            ("1101001100", 4),
            ("1010001011001", 3),
            ("100011", 2),
            ("00110011", 4),
            ("111000111000", 4),
            ("010010", 3),
            ("110100", 2),
            ("0011", 2),
        ],
    )
    def test_min_flips(self, s: str, expected: int):
        result = run_min_flips(Solution, s)
        assert_min_flips(result, expected)
