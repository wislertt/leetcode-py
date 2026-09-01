import pytest

from leetcode_py import logged_test

from .helpers import assert_survived_robots_healths, run_survived_robots_healths
from .solution import Solution


class TestRobotCollisions:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "positions, healths, directions, expected",
        [
            ([5, 4, 3, 2, 1], [2, 17, 9, 15, 10], "RRRRR", [2, 17, 9, 15, 10]),
            ([3, 5, 2, 6], [10, 10, 15, 12], "RLRL", [14]),
            ([1, 2, 5, 6], [10, 10, 11, 11], "RLRL", []),
            ([1], [5], "R", [5]),
            ([1], [5], "L", [5]),
            ([1, 2], [5, 5], "RL", []),
            ([1, 2], [5, 3], "RL", [4]),
            ([1, 2], [3, 5], "RL", [4]),
            ([1, 2, 3], [5, 4, 3], "RRL", [5, 3]),
            ([1, 2, 3], [5, 4, 6], "RRL", []),
            ([1, 2, 3], [5, 4, 9], "RRL", [7]),
            ([3, 1, 2], [7, 8, 9], "LLL", [7, 8, 9]),
            ([2, 1], [4, 4], "LR", []),
            ([10, 3, 7], [9, 5, 8], "RLR", [9, 5, 8]),
            ([1, 2, 3, 4], [4, 3, 2, 1], "RRLL", [4, 1]),
            ([1, 2, 3, 4], [1, 2, 3, 4], "RRLL", [1, 4]),
            ([4, 1, 3, 2], [3, 9, 2, 5], "LRRL", [7]),
            ([1, 2, 3, 4, 5], [1, 1, 1, 1, 9], "RRRLL", [7]),
            ([1, 4, 9, 16, 25], [6, 1, 3, 2, 8], "RLRLR", [5, 2, 8]),
            ([8, 2, 5, 11], [4, 4, 4, 4], "LLRL", [4, 4]),
            ([2, 1, 9, 3, 7, 8], [9, 2, 6, 1, 9, 5], "RRRRLL", [7, 2, 6]),
            ([10, 3, 6, 5, 1], [3, 8, 5, 3, 6], "RRLLL", [3, 6, 6]),
            ([1, 12, 2], [5, 5, 9], "LLR", [5, 8]),
            ([7, 10], [9, 6], "LL", [9, 6]),
            ([4, 2], [9, 8], "RL", [9, 8]),
            ([5], [8], "R", [8]),
            ([2, 4, 1, 12, 3, 5], [8, 7, 1, 4, 4, 8], "LRRLRL", [7, 4, 6]),
            ([12], [2], "R", [2]),
            ([4, 8, 11], [2, 2, 6], "RRR", [2, 2, 6]),
            ([5], [5], "R", [5]),
        ],
    )
    def test_survived_robots_healths(
        self, positions: list[int], healths: list[int], directions: str, expected: list[int]
    ):
        result = run_survived_robots_healths(Solution, positions, healths, directions)
        assert_survived_robots_healths(result, expected)
