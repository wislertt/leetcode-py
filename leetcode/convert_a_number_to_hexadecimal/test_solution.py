import pytest

from leetcode_py import logged_test

from .helpers import assert_to_hex, run_to_hex
from .solution import Solution


class TestConvertANumberToHexadecimal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, expected",
        [
            (26, "1a"),
            (-1, "ffffffff"),
            (0, "0"),
            (1, "1"),
            (15, "f"),
            (16, "10"),
            (255, "ff"),
            (4096, "1000"),
            (2147483647, "7fffffff"),
            (-2, "fffffffe"),
            (-16, "fffffff0"),
            (-2147483648, "80000000"),
            (-2147483647, "80000001"),
            (536870911, "1fffffff"),
            (-1960523826, "8b24c7ce"),
            (952878404, "38cbc544"),
            (1428206383, "5520b32f"),
            (395488441, "1792acb9"),
        ],
    )
    def test_to_hex(self, num: int, expected: str):
        result = run_to_hex(Solution, num)
        assert_to_hex(result, expected)
