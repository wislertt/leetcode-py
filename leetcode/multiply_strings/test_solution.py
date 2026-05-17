import pytest

from leetcode_py import logged_test

from .helpers import assert_multiply, run_multiply
from .solution import Solution


class TestMultiplyStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num1, num2, expected",
        [
            ("2", "3", "6"),
            ("123", "456", "56088"),
            ("0", "0", "0"),
            ("0", "123", "0"),
            ("123", "0", "0"),
            ("1", "1", "1"),
            ("9", "9", "81"),
            ("99", "99", "9801"),
            ("999", "999", "998001"),
            ("123456789", "987654321", "121932631112635269"),
            ("2", "50", "100"),
            ("10", "10", "100"),
            ("100", "100", "10000"),
            ("5", "5", "25"),
            ("123", "1", "123"),
            ("1", "999", "999"),
        ],
    )
    def test_multiply(self, num1: str, num2: str, expected: str):
        result = run_multiply(Solution, num1, num2)
        assert_multiply(result, expected)
