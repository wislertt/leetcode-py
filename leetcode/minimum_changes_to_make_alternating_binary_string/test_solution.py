import pytest

from leetcode_py import logged_test

from .helpers import assert_min_operations, run_min_operations
from .solution import Solution


class TestTestMinimumChangesToMakeAlternatingBinaryString:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("0100", 1),
            ("10", 0),
            ("1111", 2),
            ("0", 0),
            ("1", 0),
            ("01", 0),
            ("00", 1),
            ("11", 1),
            ("0101", 0),
            ("1010", 0),
            ("0000", 2),
            ("1001", 2),
            ("110010", 2),
            ("00110011", 4),
            ("111", 1),
            ("11010101000", 2),
            ("01011011", 3),
            ("111111", 3),
            ("10001", 1),
            ("0101110101", 1),
        ],
    )
    def test_min_operations(self, s: str, expected: int):
        result = run_min_operations(Solution, s)
        assert_min_operations(result, expected)
