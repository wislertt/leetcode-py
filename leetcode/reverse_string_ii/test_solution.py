import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_str, run_reverse_str
from .solution import Solution


class TestReverseStringII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("abcdefg", 2, "bacdfeg"),
            ("abcd", 2, "bacd"),
            ("a", 1, "a"),
            ("a", 5, "a"),
            ("ab", 1, "ab"),
            ("ab", 2, "ba"),
            ("abc", 2, "bac"),
            ("abcdef", 2, "bacdfe"),
            ("abcdefgh", 3, "cbadefhg"),
            ("abcdefghij", 4, "dcbaefghji"),
            ("abcdefg", 1, "abcdefg"),
            ("abcdefg", 3, "cbadefg"),
            ("abcdefg", 7, "gfedcba"),
            ("abcdefg", 100, "gfedcba"),
            ("hyzq", 2, "yhzq"),
            ("krxhetv", 5, "ehxrktv"),
            ("aomefr", 6, "rfemoa"),
            ("oycbsx", 3, "cyobsx"),
        ],
    )
    def test_reverse_str(self, s: str, k: int, expected: str):
        result = run_reverse_str(Solution, s, k)
        assert_reverse_str(result, expected)
