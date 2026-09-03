import pytest

from leetcode_py import logged_test

from .helpers import assert_escape_ghosts, run_escape_ghosts
from .solution import Solution


class TestEscapeTheGhosts:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "ghosts, target, expected",
        [
            ([[1, 0], [0, 3]], [0, 1], True),
            ([[1, 0]], [2, 0], False),
            ([[2, 0]], [1, 0], False),
            ([[0, 0]], [1, 0], False),
            ([[0, 0]], [0, 1], False),
            ([[0, 0]], [1, 1], False),
            ([[5, 5]], [1, 1], True),
            ([[-3, -3]], [1, 1], True),
            ([[1, 1]], [1, 1], False),
            ([[0, 1]], [0, 2], False),
            ([[0, 3]], [0, 1], True),
            ([[100, 100]], [50, 50], False),
            ([[100, 100]], [49, 49], True),
            ([[-1, 0], [0, -1]], [1, 1], True),
            ([[1, 0], [0, 1]], [0, 1], False),
            ([[0, 0], [0, 0]], [1, 1], False),
            ([[3, 4]], [0, 5], False),
            ([[-10000, -10000]], [10000, 10000], True),
            ([[10000, 10000]], [10000, 10000], False),
            ([[10000, 10000]], [9999, 9999], False),
            ([[10, -9], [5, -6], [2, 7], [-1, 6]], [-1, 8], False),
            ([[9, 0], [-1, 1]], [-1, -1], False),
            ([[10, -4], [-2, 7], [-3, 2]], [4, 9], False),
            ([[1, 6], [-5, 3]], [-8, 8], False),
        ],
    )
    def test_escape_ghosts(self, ghosts: list[list[int]], target: list[int], expected: bool):
        result = run_escape_ghosts(Solution, ghosts, target)
        assert_escape_ghosts(result, expected)
