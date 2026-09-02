import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_invalid_parentheses, run_remove_invalid_parentheses
from .solution import Solution


class TestRemoveInvalidParentheses:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("()())()", ["(())()", "()()()"]),
            ("(a)())()", ["(a())()", "(a)()()"]),
            (")(", [""]),
            ("()()", ["()()"]),
            ("(a", ["a"]),
            ("a)", ["a"]),
            ("((((", [""]),
            ("))))", [""]),
            ("(", [""]),
            (")", [""]),
            ("a", ["a"]),
            ("()())(", ["(())", "()()"]),
            ("(()", ["()"]),
            ("())", ["()"]),
            ("(a(b(c)d)", ["(a(bc)d)", "(ab(c)d)", "a(b(c)d)"]),
            ("x)", ["x"]),
            ("(u)", ["(u)"]),
            ("(()())", ["(()())"]),
            (")()(", ["()"]),
            ("n())m(", ["n()m"]),
            ("((a)", ["(a)"]),
            ("a)b(c", ["abc"]),
            ("(())())(", ["(()())", "(())()"]),
            ("ab)c(d)e(", ["abc(d)e"]),
        ],
    )
    def test_remove_invalid_parentheses(self, s: str, expected: list[str]):
        result = run_remove_invalid_parentheses(Solution, s)
        assert_remove_invalid_parentheses(result, expected)
