import pytest

from leetcode_py import logged_test

from .helpers import assert_to_lower_case, run_to_lower_case
from .solution import Solution


class TestToLowerCase:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("Hello", "hello"),
            ("here", "here"),
            ("LOVELY", "lovely"),
            ("a", "a"),
            ("A", "a"),
            ("z", "z"),
            ("Z", "z"),
            ("AzZa", "azza"),
            ("AbCdEfG", "abcdefg"),
            ("123!@#", "123!@#"),
            ("Hello World 123", "hello world 123"),
            ("MiXeD CaSe StRiNg", "mixed case string"),
            ("ALL CAPS WITH SPACES", "all caps with spaces"),
            ("  leading and trailing  ", "  leading and trailing  "),
            ("PyThOn3.12+Is-FuN", "python3.12+is-fun"),
            ("aBcDeFgHiJkLmNoPqRsTuVw", "abcdefghijklmnopqrstuvw"),
        ],
    )
    def test_to_lower_case(self, s: str, expected: str):
        result = run_to_lower_case(Solution, s)
        assert_to_lower_case(result, expected)
