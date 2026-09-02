import pytest

from leetcode_py import logged_test

from .helpers import assert_can_be_valid, run_can_be_valid
from .solution import Solution


class TestCheckIfAParenthesesStringCanBeValid:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, locked, expected",
        [
            ("))()))", "010100", True),
            ("()()", "0000", True),
            ("(((())(((())", "111111010111", True),
            ("()", "11", True),
            (")(", "00", True),
            ("()", "00", True),
            ("((((", "0000", True),
            ("))))", "0000", True),
            ("(()())((()", "1000111010", True),
            (")", "0", False),
            ("(", "0", False),
            ("(", "1", False),
            (")", "1", False),
            (")(", "11", False),
            ("(()", "000", False),
            ("())", "000", False),
            ("((((", "0011", False),
            ("((", "01", False),
        ],
    )
    def test_can_be_valid(self, s: str, locked: str, expected: bool):
        result = run_can_be_valid(Solution, s, locked)
        assert_can_be_valid(result, expected)
