import pytest

from leetcode_py import logged_test

from .helpers import assert_min_remove_to_make_valid, run_min_remove_to_make_valid
from .solution import Solution


class TestMinimumRemoveToMakeValidParenthesesTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("lee(t(c)o)de)", "lee(t(c)o)de"),
            ("a)b(c)d", "ab(c)d"),
            ("))((", ""),
            ("(a(b(c)d)", "a(b(c)d)"),
            ("abc", "abc"),
            ("a", "a"),
            ("(", ""),
            (")", ""),
            ("()", "()"),
            ("((", ""),
            ("))", ""),
            ("()())(()", "()()()"),
            ("(t(e)s)t)ing", "(t(e)s)ting"),
            ("ab(a(b)b)c)d(", "ab(a(b)b)cd"),
            ("(x(y)z)", "(x(y)z)"),
            ("x)y(z", "xyz"),
            ("mi)(()(fake)", "mi()(fake)"),
            ("e(a)v(i)l)", "e(a)v(i)l"),
            ("())()(((", "()()"),
            ("word", "word"),
            ("h(e)l(l)o)(w)o(r)ld", "h(e)l(l)o(w)o(r)ld"),
        ],
    )
    def test_min_remove_to_make_valid(self, s: str, expected: str):
        result = run_min_remove_to_make_valid(Solution, s)
        assert_min_remove_to_make_valid(result, expected)
