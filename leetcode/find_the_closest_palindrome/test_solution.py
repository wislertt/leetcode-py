import pytest

from leetcode_py import logged_test

from .helpers import assert_nearest_palindromic, run_nearest_palindromic
from .solution import Solution


class TestFindTheClosestPalindrome:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, expected",
        [
            ("123", "121"),
            ("1", "0"),
            ("9", "8"),
            ("10", "9"),
            ("11", "9"),
            ("12", "11"),
            ("19", "22"),
            ("88", "77"),
            ("99", "101"),
            ("100", "99"),
            ("101", "99"),
            ("119", "121"),
            ("121", "111"),
            ("122", "121"),
            ("1234", "1221"),
            ("1000", "999"),
            ("9999", "10001"),
            ("12345", "12321"),
            ("99800", "99799"),
            ("1000001", "999999"),
            ("1234567", "1234321"),
            ("12932", "12921"),
            ("1805170081", "1805115081"),
            ("884753610", "884757488"),
            ("100000000000000000", "99999999999999999"),
            ("999999999999999999", "1000000000000000001"),
            ("123456789012345678", "123456788887654321"),
        ],
    )
    def test_nearest_palindromic(self, n: str, expected: str):
        result = run_nearest_palindromic(Solution, n)
        assert_nearest_palindromic(result, expected)
