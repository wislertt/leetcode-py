import pytest

from leetcode_py import logged_test

from .helpers import assert_is_number, run_is_number
from .solution import Solution


class TestValidNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("0", True),
            ("e", False),
            (".", False),
            ("2", True),
            ("0089", True),
            ("-0.1", True),
            ("+3.14", True),
            ("4.", True),
            ("-.9", True),
            ("2e10", True),
            ("-90E3", True),
            ("3e+7", True),
            ("+6e-1", True),
            ("53.5e93", True),
            ("-123.456e789", True),
            ("abc", False),
            ("1a", False),
            ("1e", False),
            ("e3", False),
            ("99e2.5", False),
            ("--6", False),
            ("-+3", False),
            ("95a54e53", False),
            ("1", True),
            ("+", False),
            ("-", False),
            ("3.", True),
            (".5", True),
            ("5.e1", True),
            ("6e+", False),
            ("6e-", False),
            ("+E3", False),
            ("-1E-10", True),
            ("1e5e5", False),
            ("1.2.3", False),
            ("+-3", False),
            ("..", False),
            ("e5", False),
            ("4e+", False),
            ("inf", False),
            ("0e", False),
            ("+.8", True),
            ("000.000", True),
            ("-.7e+42", True),
            ("1234567890123456789", True),
        ],
    )
    def test_is_number(self, s: str, expected: bool):
        result = run_is_number(Solution, s)
        assert_is_number(result, expected)
