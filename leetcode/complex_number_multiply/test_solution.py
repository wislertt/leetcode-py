import pytest

from leetcode_py import logged_test

from .helpers import assert_complex_number_multiply, run_complex_number_multiply
from .solution import Solution


class TestComplexNumberMultiply:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num1, num2, expected",
        [
            ("1+1i", "1+1i", "0+2i"),
            ("1+-1i", "1+-1i", "0+-2i"),
            ("0+0i", "0+0i", "0+0i"),
            ("1+0i", "1+0i", "1+0i"),
            ("1+-1i", "1+1i", "2+0i"),
            ("2+3i", "4+5i", "-7+22i"),
            ("-3+4i", "1+-2i", "5+10i"),
            ("0+1i", "0+1i", "-1+0i"),
            ("100+100i", "100+100i", "0+20000i"),
            ("-100+-100i", "100+100i", "0+-20000i"),
            ("1+1i", "1+-1i", "2+0i"),
            ("-1+0i", "1+0i", "-1+0i"),
            ("5+-3i", "-2+7i", "11+41i"),
            ("0+-1i", "0+1i", "1+0i"),
            ("86+13i", "-37+-43i", "-2623+-4179i"),
            ("-90+17i", "32+83i", "-4291+-6926i"),
            ("10+-65i", "79+36i", "3130+-4775i"),
            ("-29+-20i", "45+67i", "35+-2843i"),
        ],
    )
    def test_complex_number_multiply(self, num1: str, num2: str, expected: str):
        result = run_complex_number_multiply(Solution, num1, num2)
        assert_complex_number_multiply(result, expected)
