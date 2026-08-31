import pytest

from leetcode_py import logged_test

from .helpers import assert_generate_possible_next_moves, run_generate_possible_next_moves
from .solution import Solution


class TestFlipGame:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "current_state, expected",
        [
            ("++++", ["++--", "+--+", "--++"]),
            ("+", []),
            ("-", []),
            ("--", []),
            ("++", ["--"]),
            ("-++-", ["----"]),
            ("++--", ["----"]),
            ("--++", ["----"]),
            ("+-+-+", []),
            ("++++++", ["++++--", "+++--+", "++--++", "+--+++", "--++++"]),
            ("-+-+-+", []),
            ("+++", ["+--", "--+"]),
            ("--++++--", ["--++----", "--+--+--", "----++--"]),
            ("++-++", ["++---", "---++"]),
        ],
    )
    def test_generate_possible_next_moves(self, current_state: str, expected: list[str]):
        result = run_generate_possible_next_moves(Solution, current_state)
        assert_generate_possible_next_moves(result, expected)
