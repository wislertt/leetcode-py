import pytest

from leetcode_py import logged_test

from .helpers import assert_is_robot_bounded, run_is_robot_bounded
from .solution import Solution


class TestRobotBoundedInCircle:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "instructions, expected",
        [
            ("GGLLGG", True),
            ("GG", False),
            ("GL", True),
            ("G", False),
            ("L", True),
            ("R", True),
            ("GR", True),
            ("GLGLGLG", True),
            ("GGGR", True),
            ("GGRGGRGGG", True),
            ("GLRLLGLL", True),
            ("GLGLG", True),
            ("GGLL", True),
            ("GLLGLLGGLL", True),
            ("GGLGLLGG", True),
            ("RGGRGGRG", True),
        ],
    )
    def test_is_robot_bounded(self, instructions: str, expected: bool):
        result = run_is_robot_bounded(Solution, instructions)
        assert_is_robot_bounded(result, expected)
