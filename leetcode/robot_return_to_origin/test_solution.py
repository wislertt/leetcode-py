import pytest

from leetcode_py import logged_test

from .helpers import assert_judge_circle, run_judge_circle
from .solution import Solution


class TestRobotReturnToOrigin:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "moves, expected",
        [
            ("UD", True),
            ("LL", False),
            ("RRDD", False),
            ("LDRRLRUULR", False),
            ("UDLR", True),
            ("RL", True),
            ("UUDDLRLR", True),
            ("L", False),
            ("R", False),
            ("U", False),
            ("D", False),
            ("UUDDLLRR", True),
            ("UUDDLRR", False),
            ("LDRRLRUULRUDLR", False),
            ("RRUULLDD", True),
            ("RRDDLLUU", True),
            ("DR", False),
            ("UL", False),
            ("LLLLLRURRRRU", False),
            ("U", False),
            ("UUURL", False),
            ("LRULDLRDLLDU", False),
            ("L", False),
            ("LDDURRD", False),
            ("LURL", False),
            ("RURRDUDRLDDUDLDRLDDR", False),
            ("ULULDLUDLUDL", False),
            ("LRURRD", False),
            ("LLU", False),
            ("URLRUUUULDUDDDUDRRRL", False),
            ("URLULR", False),
            ("DURLUDRLRLDL", False),
        ],
    )
    def test_judge_circle(self, moves: str, expected: bool):
        result = run_judge_circle(Solution, moves)
        assert_judge_circle(result, expected)
