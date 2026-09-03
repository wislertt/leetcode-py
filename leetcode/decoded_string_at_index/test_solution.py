import pytest

from leetcode_py import logged_test

from .helpers import assert_decode_at_index, run_decode_at_index
from .solution import Solution


class TestDecodedStringAtIndex:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("leet2code3", 10, "o"),
            ("ha22", 5, "h"),
            ("a2345678999999999999999", 1, "a"),
            ("abc", 1, "a"),
            ("abc", 3, "c"),
            ("a2", 2, "a"),
            ("a9", 9, "a"),
            ("ab2c3", 4, "b"),
            ("ab2c3", 15, "c"),
            ("a2b3c4", 7, "a"),
            ("a2b3c4", 20, "c"),
            ("leet2code3", 1, "l"),
            ("leet2code3", 8, "t"),
            ("leet2code3", 11, "d"),
            ("leet2code3", 36, "e"),
            ("ha22", 1, "h"),
            ("ha22", 8, "a"),
            ("m5n9", 30, "n"),
            ("g9h9i9", 100, "g"),
            ("x3y2z4", 15, "x"),
            ("leetcode9", 40, "e"),
            ("b8a999999999", 8, "b"),
            ("b8a999999999", 9, "a"),
            ("vzpp636", 20, "p"),
        ],
    )
    def test_decode_at_index(self, s: str, k: int, expected: str):
        result = run_decode_at_index(Solution, s, k)
        assert_decode_at_index(result, expected)
