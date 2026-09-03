import pytest

from leetcode_py import logged_test

from .helpers import assert_is_rational_equal, run_is_rational_equal
from .solution import Solution


class TestEqualRationalNumbers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, t, expected",
        [
            ("0.(52)", "0.5(25)", True),
            ("0.1666(6)", "0.166(66)", True),
            ("0.9(9)", "1.", True),
            ("0.(9)", "1", True),
            ("12", "12.0(0)", True),
            ("0.", "0", True),
            ("1.0", "1.00(0)", True),
            ("0.1(6)", "0.166(6)", True),
            ("0.5", "0.4(9)", True),
            ("1.2(3)", "1.23(3)", True),
            ("0.(3)", "0.3(3)", True),
            ("0.000(1)", "0.0001", False),
            ("0.(52)", "0.5(2)", False),
            ("1.0", "1.1", False),
            ("999.9999(9)", "1000", True),
            ("123.00(1212)", "123.00(12)", True),
            ("0.9(9)", "0.9", False),
            ("0.1(0)", "0.100(0)", True),
        ],
    )
    def test_is_rational_equal(self, s: str, t: str, expected: bool):
        result = run_is_rational_equal(Solution, s, t)
        assert_is_rational_equal(result, expected)
