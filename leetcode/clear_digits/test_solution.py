import pytest

from leetcode_py import logged_test

from .helpers import assert_clear_digits, run_clear_digits
from .solution import Solution


class TestClearDigits:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("abc", "abc"),
            ("cb34", ""),
            ("a1b2c3", ""),
            ("abc12", "a"),
            ("ab1c2", "a"),
            ("a", "a"),
            ("z9", ""),
            ("aa1bb1", "ab"),
            ("a1b1c1", ""),
            ("ab", "ab"),
            ("a1", ""),
            ("abcdefg1h2", "abcdef"),
            ("xy3z", "xz"),
            ("p5q5r5", ""),
            ("leet1code2", "leecod"),
            ("acb2b2", "ac"),
        ],
    )
    def test_clear_digits(self, s: str, expected: str):
        result = run_clear_digits(Solution, s)
        assert_clear_digits(result, expected)
