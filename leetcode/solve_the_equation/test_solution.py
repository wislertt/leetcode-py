import pytest

from leetcode_py import logged_test

from .helpers import assert_solve_equation, run_solve_equation
from .solution import Solution


class TestSolveTheEquation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "equation, expected",
        [
            ("x+5-3+x=6+x-2", "x=2"),
            ("x=x", "Infinite solutions"),
            ("2x=x", "x=0"),
            ("x=x+1", "No solution"),
            ("-x=-1", "x=1"),
            ("0x=0", "Infinite solutions"),
            ("x+1=x+2", "No solution"),
            ("3x-2-x=2x+4", "No solution"),
            ("99x=99", "x=1"),
            ("x-100=100-x", "x=100"),
            ("-1+x=0", "x=1"),
            ("x=5", "x=5"),
            ("5=5", "Infinite solutions"),
            ("5=6", "No solution"),
            ("-x+1=-x+1", "Infinite solutions"),
            ("100x-100=0", "x=1"),
            ("x+2x+3x=6x-6", "No solution"),
            ("-x+2x=3", "x=3"),
        ],
    )
    def test_solve_equation(self, equation: str, expected: str):
        result = run_solve_equation(Solution, equation)
        assert_solve_equation(result, expected)
