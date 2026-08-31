import pytest

from leetcode_py import logged_test

from .helpers import assert_can_win, run_can_win
from .solution import Solution


class TestFlipGameII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "current_state, expected",
        [
            ("++++", True),
            ("+", False),
            ("++", True),
            ("+++", True),
            ("+++++", False),
            ("-++", True),
            ("+--+", False),
            ("+---+", False),
            ("++--++", False),
            ("+++-++", False),
            ("--", False),
            ("+-+-", False),
            ("++++-", True),
            ("+++-", True),
            ("+++++++", True),
            ("++-++-++", True),
        ],
    )
    def test_can_win(self, current_state: str, expected: bool):
        result = run_can_win(Solution, current_state)
        assert_can_win(result, expected)
