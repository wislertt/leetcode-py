import pytest

from leetcode_py import logged_test

from .helpers import assert_reverse_parentheses, run_reverse_parentheses
from .solution import Solution


class TestReverseSubstringsBetweenEachPairOfParenthesesTest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("(abcd)", "dcba"),
            ("(u(love)i)", "iloveu"),
            ("(ed(et(oc))el)", "leetcode"),
            ("a(bcdefghijkl(mno)p)q", "apmnolkjihgfedcbq"),
            ("(abc)", "cba"),
            ("abc", "abc"),
            ("(())", ""),
            ("((ab))", "ab"),
            ("(ab(cd)ef)", "fecdba"),
            ("ta()usw((((a))))", "tauswa"),
            ("(a)b(c)d", "abcd"),
            ("(ab)", "ba"),
            ("(b)x(az)", "bxza"),
            ("co(de(fight)s)", "cosfighted"),
            ("(nvqzikme)(qqhlashx)", "emkizqvnxhsalhqq"),
            ("(eqkjhjkgi)(mnkjhgfre)", "igkjhjkqeerfghjknm"),
        ],
    )
    def test_reverse_parentheses(self, s: str, expected: str):
        result = run_reverse_parentheses(Solution, s)
        assert_reverse_parentheses(result, expected)
