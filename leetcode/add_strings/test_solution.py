import pytest

from leetcode_py import logged_test

from .helpers import assert_add_strings, run_add_strings
from .solution import Solution


class TestAddStrings:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize("num1, num2, expected", [])
    def test_add_strings(self, num1: str, num2: str, expected: str):
        result = run_add_strings(Solution, num1, num2)
        assert_add_strings(result, expected)
