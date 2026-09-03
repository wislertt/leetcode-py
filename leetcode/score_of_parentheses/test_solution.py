import pytest

from leetcode_py import logged_test

from .helpers import assert_score_of_parentheses, run_score_of_parentheses
from .solution import Solution


class TestScoreOfParentheses:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("()", 1),
            ("(())", 2),
            ("()()", 2),
            ("((()))", 4),
            ("(()())", 4),
            ("()()()()", 4),
            ("(()(()))", 6),
            ("((((()))))", 16),
            ("(()())(())", 6),
            ("((()())())", 10),
            ("(())()", 3),
            ("(()(()()))", 10),
            ("((())(())(()))", 12),
            ("((()()))", 8),
            ("(())((()))(((((())()())(()))()()))()", 95),
            ("((()))((((())))(()))((()())())()()", 36),
            ("(((()))()())((((())()))()(())()(()())(()))()", 57),
            ("(()())(((()))())()((()))", 19),
            ("(((())((()())((())())()))()(()))()(()())((()()))()", 116),
            ("((()())())((((())(()))(()))(())())", 56),
            ("(((())()))()()", 14),
            ("(((()(())())((())))())", 50),
            ("((((((((((((((((((((((((()))))))))))))))))))))))))", 16777216),
        ],
    )
    def test_score_of_parentheses(self, s: str, expected: int):
        result = run_score_of_parentheses(Solution, s)
        assert_score_of_parentheses(result, expected)
