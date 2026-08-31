import pytest

from leetcode_py import logged_test

from .helpers import assert_robot_sim, run_robot_sim
from .solution import Solution


class TestWalkingRobotSimulation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "commands, obstacles, expected",
        [
            ([4, -1, 3], [], 25),
            ([4, -1, 4, -2, 4], [[2, 4]], 65),
            ([-1, 9], [[5, 0], [2, 0]], 1),
            ([6, -1, -1, 6], [], 36),
            ([], [], 0),
            ([9], [], 81),
            ([4, -1, 4, -2, 4], [], 80),
            ([1, 2, -2, 3], [[0, 3]], 13),
            ([7, -2, -2, 7, 5], [[-3, 2], [-2, 1], [0, 1], [-5, 0]], 144),
            ([3, 4, -1, 2, -2, 4], [[2, 4]], 125),
            ([-1, -2, 9, -1, -2, 9], [], 324),
            ([2, 2, 2, -1, 2], [[0, 3], [1, 2]], 4),
            ([5, -1, 5, -2, 5], [[3, 3], [3, 4]], 125),
            ([1, -2, 1, -2, 1], [[0, 2], [2, 0]], 2),
        ],
    )
    def test_robot_sim(self, commands: list[int], obstacles: list[list[int]], expected: int):
        result = run_robot_sim(Solution, commands, obstacles)
        assert_robot_sim(result, expected)
