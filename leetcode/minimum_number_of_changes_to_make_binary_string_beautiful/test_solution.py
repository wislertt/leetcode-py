import pytest

from leetcode_py import logged_test

from .helpers import assert_min_changes, run_min_changes
from .solution import Solution


class TestMinimumNumberOfChangesToMakeBinaryStringBeautiful:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("1001", 2),
            ("10", 1),
            ("0000", 0),
            ("11", 0),
            ("01", 1),
            ("0011", 0),
            ("1100", 0),
            ("1010", 2),
            ("0101", 2),
            ("100110", 3),
            ("01101100", 2),
            ("11100011", 1),
            ("010010110011", 2),
            ("0111", 1),
            ("0110000000101101", 4),
            ("111000000010", 2),
            ("1011011011111100", 3),
            ("001001011100", 3),
            ("1000001000100111", 4),
            ("010000100111", 3),
            ("0010010010", 3),
            ("0111100101", 4),
        ],
    )
    def test_min_changes(self, s: str, expected: int):
        result = run_min_changes(Solution, s)
        assert_min_changes(result, expected)
