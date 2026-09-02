import pytest

from leetcode_py import logged_test

from .helpers import assert_has_path, run_has_path
from .solution import Solution


class TestTheMaze:
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
                True,
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
                False,
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
                False,
            ),
            ([[0, 0], [0, 0]], [0, 0], [1, 1], True),
            ([[0, 0, 0], [0, 1, 0], [0, 0, 0]], [0, 0], [2, 2], True),
            (
                [
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 0, 1, 0],
                    [1, 1, 0, 1, 1],
                    [0, 0, 0, 0, 0],
                ],
                [0, 4],
                [2, 0],
                True,
            ),
            ([[0, 1, 0], [0, 1, 0], [0, 1, 0]], [0, 0], [0, 2], False),
            ([[0, 1, 0], [0, 1, 0], [0, 0, 0]], [0, 0], [2, 0], True),
            ([[0, 0, 0], [1, 1, 0], [0, 0, 0]], [0, 0], [2, 0], True),
            ([[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0]], [0, 0], [3, 3], True),
            ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [1, 1], [0, 0], True),
            ([[0, 0, 0, 0, 0], [1, 1, 1, 1, 0], [0, 0, 0, 0, 0]], [0, 0], [2, 0], True),
        ],
    )
    def test_has_path(
        self, maze: list[list[int]], start: list[int], destination: list[int], expected: bool
    ):
        result = run_has_path(Solution, maze, start, destination)
        assert_has_path(result, expected)
