import pytest

from leetcode_py import logged_test

from .helpers import assert_min_time, run_min_time
from .solution import Solution


class TestMinimumTimeToCollectAllApplesInATree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, has_apple, expected",
        [
            (
                7,
                [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                [False, False, True, False, True, True, False],
                8,
            ),
            (
                7,
                [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                [False, False, True, False, False, True, False],
                6,
            ),
            (
                7,
                [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                [False, False, False, False, False, False, False],
                0,
            ),
            (1, [], [True], 0),
            (1, [], [False], 0),
            (2, [[0, 1]], [True, True], 2),
            (2, [[0, 1]], [True, False], 0),
            (2, [[0, 1]], [False, True], 2),
            (3, [[0, 1], [1, 2]], [True, False, True], 4),
            (3, [[0, 1], [1, 2]], [False, False, True], 4),
            (4, [[0, 1], [0, 2], [2, 3]], [True, True, False, True], 6),
            (4, [[0, 1], [0, 2], [2, 3]], [False, True, False, False], 2),
            (
                8,
                [[0, 1], [0, 2], [1, 6], [2, 3], [2, 5], [3, 4], [5, 7]],
                [True, True, True, True, True, True, True, True],
                14,
            ),
            (
                12,
                [
                    [0, 1],
                    [0, 2],
                    [0, 3],
                    [0, 4],
                    [0, 5],
                    [0, 9],
                    [1, 8],
                    [1, 10],
                    [5, 6],
                    [5, 7],
                    [9, 11],
                ],
                [
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                ],
                0,
            ),
            (
                7,
                [[0, 1], [1, 2], [1, 3], [1, 5], [2, 4], [2, 6]],
                [True, True, True, True, True, True, True],
                12,
            ),
            (
                11,
                [[0, 1], [0, 2], [0, 3], [0, 8], [1, 5], [1, 10], [3, 4], [4, 9], [5, 6], [6, 7]],
                [True, True, True, True, True, True, True, True, True, True, True],
                20,
            ),
            (
                8,
                [[0, 1], [0, 3], [1, 2], [3, 4], [4, 5], [4, 6], [4, 7]],
                [False, False, False, False, False, False, False, False],
                0,
            ),
            (5, [[0, 1], [0, 4], [1, 2], [2, 3]], [False, False, False, False, False], 0),
        ],
    )
    def test_min_time(self, n: int, edges: list[list[int]], has_apple: list[bool], expected: int):
        result = run_min_time(Solution, n, edges, has_apple)
        assert_min_time(result, expected)
