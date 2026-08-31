import pytest

from leetcode_py import logged_test

from .helpers import assert_parse_bool_expr, run_parse_bool_expr
from .solution import Solution


class TestParsingABooleanExpression:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "expression, expected",
        [
            ("&(|(f))", False),
            ("|(f,f,f,t)", True),
            ("!(&(f,t))", True),
            ("t", True),
            ("f", False),
            ("!(&(t))", False),
            ("!(t)", False),
            ("&(t,t,t)", True),
            ("&(t,f)", False),
            ("|(f,f)", False),
            ("|(t,f)", True),
            ("!(&(|(t,f),f))", True),
            ("|(&(t,f,t),!(f))", True),
            ("&(|(f,t),&(t),!(f))", True),
            ("!(!(!(f)))", True),
            ("|(&(f,t),&(f,f),|(t,t))", True),
            ("&(t,|(f,t),&(t,t))", True),
        ],
    )
    def test_parse_bool_expr(self, expression: str, expected: bool):
        result = run_parse_bool_expr(Solution, expression)
        assert_parse_bool_expr(result, expected)
