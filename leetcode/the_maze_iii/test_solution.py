import pytest

from leetcode_py import logged_test

from .helpers import assert_find_shortest_way, run_find_shortest_way
from .solution import Solution


class TestTheMazeIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "maze, ball, hole, expected",
        [
            (
                [
                    [0, 0, 0, 0, 0],
                    [1, 1, 0, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1],
                    [0, 1, 0, 0, 0],
                ],
                [4, 3],
                [0, 1],
                "lul",
            ),
            (
                [
                    [0, 0, 0, 0, 0],
                    [1, 1, 0, 0, 1],
                    [0, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1],
                    [0, 1, 0, 0, 0],
                ],
                [4, 3],
                [3, 0],
                "impossible",
            ),
            (
                [
                    [0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 1],
                ],
                [0, 4],
                [3, 5],
                "dldr",
            ),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0], [2, 2], "dr"),
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [0, 0], [2, 0], "d"),
            ([[0, 1, 0], [0, 0, 0], [0, 1, 0]], [0, 0], [2, 2], "impossible"),
            (
                [
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 0, 0, 0, 0],
                ],
                [0, 4],
                [1, 2],
                "ldl",
            ),
            ([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]], [0, 0], [3, 0], "d"),
            ([[0, 0], [0, 0]], [0, 0], [0, 1], "r"),
            ([[0, 0, 0], [1, 0, 0], [0, 0, 0]], [0, 0], [2, 1], "rdl"),
            ([[0, 0, 0, 0], [1, 1, 0, 0], [0, 0, 0, 0], [0, 1, 0, 0]], [0, 0], [3, 3], "rd"),
        ],
    )
    def test_find_shortest_way(
        self, maze: list[list[int]], ball: list[int], hole: list[int], expected: str
    ):
        result = run_find_shortest_way(Solution, maze, ball, hole)
        assert_find_shortest_way(result, expected)
