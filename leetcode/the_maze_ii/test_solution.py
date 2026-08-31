import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_distance, run_shortest_distance
from .solution import Solution


class TestTheMazeII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "maze, start, destination, expected",
        [
            (
                [
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 0, 0, 0, 0],
                ],
                [0, 4],
                [4, 4],
                12,
            ),
            (
                [
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 0, 0, 0, 0],
                ],
                [0, 4],
                [3, 2],
                -1,
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
                [0, 1],
                -1,
            ),
            ([[0, 0], [0, 0]], [0, 0], [1, 1], 2),
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [0, 0], [2, 2], 4),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [1, 1], [0, 0], 2),
            ([[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]], [0, 0], [3, 3], 6),
            ([[0, 1, 0], [0, 1, 0], [0, 0, 0]], [0, 0], [0, 2], 6),
            ([[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0]], [0, 0], [2, 0], 10),
            (
                [
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 0, 0, 0, 0],
                ],
                [0, 4],
                [1, 1],
                -1,
            ),
            ([[0, 0, 0], [1, 1, 0], [0, 0, 0]], [0, 0], [2, 2], 4),
            ([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]], [0, 0], [0, 3], 3),
        ],
    )
    def test_shortest_distance(
        self, maze: list[list[int]], start: list[int], destination: list[int], expected: int
    ):
        result = run_shortest_distance(Solution, maze, start, destination)
        assert_shortest_distance(result, expected)
