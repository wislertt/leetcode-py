import pytest

from leetcode_py import logged_test

from .helpers import assert_max_depth, run_max_depth
from .solution import Solution


class TestMaximumNestingDepthOfTheParentheses:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("(1+(2*3)+((8)/4))+1", 3),
            ("(1)+((2))+(((3)))", 3),
            ("()(())((()()))", 3),
            ("1", 0),
            ("8", 0),
            ("()", 1),
            ("(())", 2),
            ("(()())", 2),
            ("1+2-3*4/5", 0),
            ("((1))", 2),
            ("(1)", 1),
            ("(((1)))", 3),
            ("(1+(2*(3+(4))))", 4),
            ("((((1))))", 4),
            ("(1)((2))((3))", 2),
            ("((()))()(())", 3),
            ("1+(2*3)/((4)-5)", 2),
            ("((1+2)*(3+4))", 2),
            ("()-()-5", 1),
            ("()/()7", 1),
            ("()-(8)(5)()-", 1),
            ("(8)*0", 1),
            ("(5)/()(6)", 1),
            ("()+(9)", 1),
        ],
    )
    def test_max_depth(self, s: str, expected: int):
        result = run_max_depth(Solution, s)
        assert_max_depth(result, expected)
