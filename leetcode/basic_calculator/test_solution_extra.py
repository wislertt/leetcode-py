import pytest

from leetcode_py import logged_test

from .solution import Solution


class TestBasicCalculatorExtra:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, error_msg",
        [
            ("(1+2", "Mismatched parentheses"),
            ("1+2)", "Mismatched parentheses"),
            ("((1+2)", "Mismatched parentheses"),
            ("1+2))", "Mismatched parentheses"),
            ("1*2", r"Invalid character: '\*'"),
            ("1/2", "Invalid character: '/'"),
            ("1%2", "Invalid character: '%'"),
            ("1^2", r"Invalid character: '\^'"),
            ("1&2", "Invalid character: '&'"),
            ("a+b", "Invalid character: 'a'"),
            ("1+2.5", r"Invalid character: '\.'"),
        ],
    )
    def test_calculate_invalid_input(self, s: str, error_msg: str):
        with pytest.raises(ValueError, match=error_msg):
            self.solution.calculate(s)
