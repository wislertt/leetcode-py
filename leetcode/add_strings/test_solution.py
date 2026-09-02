import pytest

from leetcode_py import logged_test

from .helpers import assert_add_strings, run_add_strings
from .solution import Solution


class TestAddStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num1, num2, expected",
        [
            ("11", "123", "134"),
            ("456", "77", "533"),
            ("0", "0", "0"),
            ("1", "1", "2"),
            ("9", "9", "18"),
            ("99", "1", "100"),
            ("999", "999", "1998"),
            ("123456789", "987654321", "1111111110"),
            ("0", "999", "999"),
            ("1", "99999", "100000"),
            ("589", "23", "612"),
            ("456789", "543211", "1000000"),
            ("98765", "4321", "103086"),
            ("5", "5", "10"),
            ("12345678901234567890", "98765432109876543210", "111111111011111111100"),
            ("99999999999999999999", "1", "100000000000000000000"),
        ],
    )
    def test_add_strings(self, num1: str, num2: str, expected: str):
        result = run_add_strings(Solution, num1, num2)
        assert_add_strings(result, expected)
