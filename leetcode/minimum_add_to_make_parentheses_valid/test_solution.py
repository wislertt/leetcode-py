import pytest

from leetcode_py import logged_test

from .helpers import assert_min_add_to_make_valid, run_min_add_to_make_valid
from .solution import Solution


class TestMinimumAddToMakeParenthesesValid:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("())", 1),
            ("(((", 3),
            ("", 0),
            ("()", 0),
            ("()))(((", 5),
            ("(", 1),
            (")", 1),
            ("()(", 1),
            (")(", 2),
            ("(())", 0),
            ("))((", 4),
            ("()()", 0),
            ("(()())(", 1),
            (")()(", 2),
            ("()()))(()", 3),
        ],
    )
    def test_min_add_to_make_valid(self, s: str, expected: int):
        result = run_min_add_to_make_valid(Solution, s)
        assert_min_add_to_make_valid(result, expected)
