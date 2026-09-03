import pytest

from leetcode_py import logged_test

from .helpers import assert_ambiguous_coordinates, run_ambiguous_coordinates
from .solution import Solution


class TestAmbiguousCoordinates:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("(123)", ["(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"]),
            ("(00011)", ["(0, 0.011)", "(0.001, 1)"]),
            ("(11)", ["(1, 1)"]),
            ("(12)", ["(1, 2)"]),
            ("(21)", ["(2, 1)"]),
            ("(101)", ["(1, 0.1)", "(10, 1)"]),
            ("(100)", ["(10, 0)"]),
            ("(010)", ["(0, 10)", "(0.1, 0)"]),
            ("(0010)", ["(0.01, 0)"]),
            ("(0100)", ["(0, 100)"]),
            ("(0000)", []),
            ("(1000)", ["(100, 0)"]),
            ("(999)", ["(9, 9.9)", "(9, 99)", "(9.9, 9)", "(99, 9)"]),
            ("(01)", ["(0, 1)"]),
            ("(000)", []),
            ("(00000)", []),
            ("(0101)", ["(0, 1.01)", "(0, 10.1)", "(0, 101)", "(0.1, 0.1)"]),
            ("(0011)", ["(0, 0.11)", "(0.01, 1)"]),
            ("(10001)", ["(1, 0.001)", "(10, 0.01)", "(100, 0.1)", "(1000, 1)"]),
            ("(9001)", ["(9, 0.01)", "(90, 0.1)", "(900, 1)"]),
        ],
    )
    def test_ambiguous_coordinates(self, s: str, expected: list[str]):
        result = run_ambiguous_coordinates(Solution, s)
        assert_ambiguous_coordinates(result, expected)
