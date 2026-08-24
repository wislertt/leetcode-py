import pytest

from leetcode_py import logged_test

from .helpers import assert_convert, run_convert
from .solution import Solution


class TestZigzagConversion:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, num_rows, expected",
        [
            ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
            ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
            ("PAYPALISHIRING", 5, "PHASIYIRPLIGAN"),
            ("A", 1, "A"),
            ("AB", 1, "AB"),
            ("ABCDEF", 1, "ABCDEF"),
            ("ABC", 2, "ACB"),
            ("ABCD", 2, "ACBD"),
            ("ABCDE", 2, "ACEBD"),
            ("ABAB", 2, "AABB"),
            ("ABCD", 3, "ABDC"),
            ("ABCDE", 3, "AEBDC"),
            ("ABCD", 4, "ABCD"),
            ("ABCDEF", 4, "ABFCED"),
            ("AB", 2, "AB"),
            ("ABC", 5, "ABC"),
            ("Z", 1000, "Z"),
            ("XY", 3, "XY"),
            ("abcdefghijklmnop", 5, "aibhjpcgkodflnem"),
            ("a,b.c", 2, "abc,."),
        ],
    )
    def test_convert(self, s: str, num_rows: int, expected: str):
        result = run_convert(Solution, s, num_rows)
        assert_convert(result, expected)
