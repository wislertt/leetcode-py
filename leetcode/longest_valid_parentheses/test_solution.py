import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_valid_parentheses, run_longest_valid_parentheses
from .solution import Solution


class TestLongestValidParentheses:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("(()", 2),
            (")()())", 4),
            ("", 0),
            ("(", 0),
            (")", 0),
            ("()", 2),
            ("()()", 4),
            ("(())", 4),
            ("(()())", 6),
            ("(()()", 4),
            (")(())", 4),
            ("()(()", 2),
            ("(((((", 0),
            (")))))", 0),
            ("((()))", 6),
            ("(())(())", 8),
        ],
    )
    def test_longest_valid_parentheses(self, s: str, expected: int):
        result = run_longest_valid_parentheses(Solution, s)
        assert_longest_valid_parentheses(result, expected)
