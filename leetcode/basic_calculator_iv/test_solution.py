import pytest

from leetcode_py import logged_test

from .helpers import assert_basic_calculator_iv, run_basic_calculator_iv
from .solution import Solution


class TestBasicCalculatorIV:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "expression, evalvars, evalints, expected",
        [
            ("e + 8 - a + 5", ["e"], [1], ["-1*a", "14"]),
            ("e - 8 + temp - p", ["e", "temp"], [1, 12], ["-1*p", "5"]),
            ("(e + 8) * (e - 8)", [], [], ["1*e*e", "-64"]),
            ("1 + 2 * 3", [], [], ["7"]),
            ("0", [], [], []),
            ("a * b * c + b * a * c", [], [], ["2*a*b*c"]),
            ("a + b + c + a + b + c", [], [], ["2*a", "2*b", "2*c"]),
            ("(a - b) * (a + b)", [], [], ["1*a*a", "-1*b*b"]),
            ("(a + b) * (a + b)", [], [], ["1*a*a", "2*a*b", "1*b*b"]),
            ("x * x * x", ["x"], [2], ["8"]),
            ("a * b + c", ["a", "b"], [2, 3], ["1*c", "6"]),
            ("(a + 3) * (b + 4)", ["a", "b"], [1, 2], ["24"]),
            ("a - a", [], [], []),
            ("(x + y) * (x - y) + y * y", [], [], ["1*x*x"]),
            ("a * a * a * a", [], [], ["1*a*a*a*a"]),
            ("(a + b) * (c + d)", [], [], ["1*a*c", "1*a*d", "1*b*c", "1*b*d"]),
            ("2 * x + y * y - 3 * x", [], [], ["1*y*y", "-1*x"]),
            ("(a + 1) * (a + 2) * (a + 3)", [], [], ["1*a*a*a", "6*a*a", "11*a", "6"]),
            ("x + y", ["x"], [-3], ["1*y", "-3"]),
            ("b + aa + c", [], [], ["1*aa", "1*b", "1*c"]),
            ("temp * press + zz", [], [], ["1*press*temp", "1*zz"]),
        ],
    )
    def test_basic_calculator_iv(
        self, expression: str, evalvars: list[str], evalints: list[int], expected: list[str]
    ):
        result = run_basic_calculator_iv(Solution, expression, evalvars, evalints)
        assert_basic_calculator_iv(result, expected)
