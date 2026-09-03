import pytest

from leetcode_py import logged_test

from .helpers import assert_loud_and_rich, run_loud_and_rich
from .solution import Solution


class TestLoudAndRich:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "richer, quiet, expected",
        [
            (
                [[1, 0], [2, 1], [3, 1], [3, 7], [4, 3], [5, 3], [6, 3]],
                [3, 2, 5, 4, 6, 1, 7, 0],
                [5, 5, 2, 5, 4, 5, 6, 7],
            ),
            ([], [0], [0]),
            ([], [0, 1], [0, 1]),
            ([], [1, 0], [0, 1]),
            ([[0, 1]], [1, 0], [0, 1]),
            ([[1, 0]], [0, 1], [0, 1]),
            ([[0, 1], [1, 2]], [2, 1, 0], [0, 1, 2]),
            ([[0, 1], [0, 2], [1, 3], [2, 3]], [0, 1, 2, 3], [0, 0, 0, 0]),
            ([[0, 2], [1, 2], [2, 3]], [3, 2, 1, 0], [0, 1, 2, 3]),
            ([], [3, 2, 5, 1, 4, 0], [0, 1, 2, 3, 4, 5]),
            (
                [[3, 4], [0, 2], [3, 5], [2, 5], [1, 2], [0, 1], [2, 4], [1, 4], [2, 3]],
                [4, 0, 1, 5, 3, 2],
                [0, 1, 1, 1, 1, 1],
            ),
            ([], [1, 2, 3, 0], [0, 1, 2, 3]),
            ([[3, 4], [0, 3], [0, 2]], [0, 1, 4, 3, 2], [0, 1, 0, 0, 0]),
            ([[0, 3], [2, 3], [1, 2], [0, 2], [1, 3]], [0, 3, 2, 1], [0, 1, 0, 0]),
            ([], [2, 1, 0], [0, 1, 2]),
            ([[0, 2], [0, 1], [0, 3], [2, 3]], [3, 1, 0, 2], [0, 1, 2, 2]),
            ([[0, 1]], [1, 0], [0, 1]),
            ([], [0, 1, 2], [0, 1, 2]),
        ],
    )
    def test_loud_and_rich(self, richer: list[list[int]], quiet: list[int], expected: list[int]):
        result = run_loud_and_rich(Solution, richer, quiet)
        assert_loud_and_rich(result, expected)
