import pytest

from leetcode_py import logged_test

from .helpers import assert_min_distance, run_min_distance
from .solution import Solution


class TestSquirrelSimulation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "height, width, tree, squirrel, nuts, expected",
        [
            (5, 7, [2, 2], [4, 4], [[3, 0], [2, 5]], 12),
            (1, 3, [0, 1], [0, 0], [[0, 2]], 3),
            (1, 1, [0, 0], [0, 0], [[0, 0]], 0),
            (3, 3, [1, 1], [1, 1], [[0, 0]], 4),
            (3, 3, [1, 1], [2, 2], [[1, 1]], 2),
            (3, 3, [0, 0], [1, 2], [[1, 2], [0, 3]], 9),
            (5, 5, [2, 2], [2, 0], [[2, 0], [2, 4]], 6),
            (10, 10, [5, 5], [0, 9], [[5, 5], [6, 6]], 11),
            (100, 100, [50, 50], [0, 0], [[49, 49], [51, 51], [49, 51]], 108),
            (2, 2, [0, 0], [1, 1], [[0, 1]], 2),
            (4, 4, [2, 2], [3, 1], [[2, 2], [2, 2]], 2),
            (5, 5, [2, 2], [2, 2], [[2, 2], [3, 3]], 4),
            (7, 8, [3, 4], [6, 0], [[0, 7], [3, 0], [6, 4]], 25),
            (3, 4, [1, 2], [2, 3], [[1, 2], [1, 2], [1, 2]], 2),
            (4, 4, [1, 1], [1, 1], [[0, 0], [3, 3]], 12),
            (9, 9, [4, 4], [7, 7], [[7, 7], [0, 0]], 22),
            (6, 6, [3, 3], [0, 5], [[5, 1], [0, 0], [5, 5]], 27),
            (8, 9, [4, 4], [7, 8], [[0, 0], [7, 0], [4, 8], [2, 2]], 45),
        ],
    )
    def test_min_distance(
        self,
        height: int,
        width: int,
        tree: list[int],
        squirrel: list[int],
        nuts: list[list[int]],
        expected: int,
    ):
        result = run_min_distance(Solution, height, width, tree, squirrel, nuts)
        assert_min_distance(result, expected)
