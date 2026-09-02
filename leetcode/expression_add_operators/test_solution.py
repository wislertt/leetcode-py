import pytest

from leetcode_py import logged_test

from .helpers import assert_add_operators, run_add_operators
from .solution import Solution


class TestExpressionAddOperators:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num, target, expected",
        [
            ("123", 6, ["1*2*3", "1+2+3"]),
            ("232", 8, ["2*3+2", "2+3*2"]),
            ("3456237490", 9191, []),
            ("1", 1, ["1"]),
            ("0", 0, ["0"]),
            ("9", 9, ["9"]),
            ("00", 0, ["0*0", "0+0", "0-0"]),
            ("105", 5, ["1*0+5", "10-5"]),
            ("105", -5, ["1*0-5"]),
            ("105", 0, ["1*0*5"]),
            ("123", 123, ["123"]),
            ("123", 45, []),
            ("232", 13, []),
            ("345", 12, ["3+4+5"]),
            ("100", 1, ["1+0*0", "1+0+0", "1+0-0", "1-0*0", "1-0+0", "1-0-0"]),
            ("22", 4, ["2*2", "2+2"]),
            ("22", 5, []),
            ("222", 6, ["2*2+2", "2+2*2", "2+2+2"]),
            ("222", 24, ["2+22", "22+2"]),
            ("001", 1, ["0*0+1", "0+0+1", "0-0+1"]),
            ("605", 65, ["60+5"]),
            ("1234", 11, ["1+2*3+4", "1-2+3*4", "12+3-4"]),
            ("1234", 1, ["1*2+3-4"]),
            ("12345", 15, ["1*2*3+4+5", "1+2+3+4+5", "1+23-4-5", "1-2*3+4*5"]),
        ],
    )
    def test_add_operators(self, num: str, target: int, expected: list[str]):
        result = run_add_operators(Solution, num, target)
        assert_add_operators(result, expected)
