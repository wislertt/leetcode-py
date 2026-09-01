import pytest

from leetcode_py import logged_test

from .helpers import assert_has_all_codes, run_has_all_codes
from .solution import Solution


class TestCheckIfAStringContainsAllBinaryCodesOfSizeK:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, k, expected",
        [
            ("00110110", 2, True),
            ("0110", 1, True),
            ("0110", 2, False),
            ("0", 1, False),
            ("1", 1, False),
            ("01", 1, True),
            ("10", 1, True),
            ("0000", 1, False),
            ("0000", 2, False),
            ("00110", 2, True),
            ("011100", 3, False),
            ("000111010100", 3, True),
            ("00", 1, False),
            ("110", 1, True),
            ("1011", 2, False),
            ("000001", 2, False),
            ("00100011", 3, False),
            ("1100110110", 3, False),
            ("100000111100000", 4, False),
            ("101001011110110111", 4, False),
            ("01010", 2, False),
            ("1101010110", 3, False),
            ("010101001", 3, False),
            ("1010001010101101101", 4, False),
            ("1010111000101001", 4, False),
        ],
    )
    def test_has_all_codes(self, s: str, k: int, expected: bool):
        result = run_has_all_codes(Solution, s, k)
        assert_has_all_codes(result, expected)
