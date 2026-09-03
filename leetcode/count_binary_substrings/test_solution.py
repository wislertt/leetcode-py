import pytest

from leetcode_py import logged_test

from .helpers import assert_count_binary_substrings, run_count_binary_substrings
from .solution import Solution


class TestCountBinarySubstrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("00110011", 6),
            ("10101", 4),
            ("0", 0),
            ("1", 0),
            ("01", 1),
            ("10", 1),
            ("0011", 2),
            ("1100", 2),
            ("000111", 3),
            ("0000", 0),
            ("1111", 0),
            ("001100", 4),
            ("0100110", 5),
            ("101010", 5),
            ("0010010011", 6),
            ("11001100110011", 12),
            ("011", 1),
            ("1101", 2),
            ("100010", 3),
            ("0011111011", 4),
        ],
    )
    def test_count_binary_substrings(self, s: str, expected: int):
        result = run_count_binary_substrings(Solution, s)
        assert_count_binary_substrings(result, expected)
