import pytest

from leetcode_py import logged_test

from .helpers import assert_parse_ternary, run_parse_ternary
from .solution import Solution


class TestTernaryExpressionParser:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "expression, expected",
        [
            ("T?2:3", "2"),
            ("F?1:T?4:5", "4"),
            ("T?T?F:5:3", "F"),
            ("T?6:9", "6"),
            ("F?2:0", "0"),
            ("T?T?T?1:2:3:4", "1"),
            ("F?F?F?8:9:7:6", "6"),
            ("T?5:T?3:2", "5"),
            ("F?1:F?1:F?1:2", "2"),
            ("T?7:F?4:3", "7"),
            ("F?T?9:0:1", "1"),
            ("T?F?4:8:T?2:6", "8"),
            ("T?8:3", "8"),
        ],
    )
    def test_parse_ternary(self, expression: str, expected: str):
        result = run_parse_ternary(Solution, expression)
        assert_parse_ternary(result, expected)
