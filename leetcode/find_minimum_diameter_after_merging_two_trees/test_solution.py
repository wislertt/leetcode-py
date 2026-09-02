import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_diameter_after_merge, run_minimum_diameter_after_merge
from .solution import Solution


class TestFindMinimumDiameterAfterMergingTwoTrees:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "edges1, edges2, expected",
        [
            ([], [], 1),
            ([], [[0, 1]], 2),
            ([[0, 1]], [], 2),
            ([[0, 1]], [[0, 1]], 3),
            ([[0, 1], [0, 2], [0, 3]], [[0, 1]], 3),
            ([[0, 1], [0, 2], [0, 3]], [], 2),
            ([], [[0, 1], [0, 2], [0, 3]], 2),
            ([[0, 1], [1, 2], [2, 3]], [[0, 1]], 4),
            ([[0, 1], [0, 2], [0, 3]], [[0, 1], [1, 2], [2, 3]], 4),
            ([[0, 1], [0, 2], [1, 3], [1, 4]], [[0, 1], [0, 2], [2, 3]], 5),
            ([[0, 1], [1, 2], [2, 3], [3, 4]], [[0, 1], [1, 2]], 4),
            ([[0, 1], [0, 2], [0, 3], [3, 4]], [[0, 1], [0, 2], [2, 3]], 5),
            ([[0, 1], [1, 2], [0, 3], [0, 4]], [[0, 1]], 4),
            ([[0, 1], [1, 2], [0, 3], [1, 4]], [[0, 1], [1, 2], [0, 3], [0, 4]], 5),
            ([[0, 1], [0, 2], [2, 3]], [[0, 1], [0, 2], [1, 3], [0, 4], [3, 5]], 5),
            ([[0, 1], [0, 2], [1, 3], [0, 4]], [[0, 1], [0, 2], [2, 3], [2, 4], [1, 5]], 5),
            ([[0, 1], [1, 2], [1, 3], [0, 4]], [[0, 1], [1, 2], [1, 3]], 4),
            ([[0, 1], [1, 2], [0, 3], [1, 4]], [[0, 1], [0, 2], [1, 3]], 5),
        ],
    )
    def test_minimum_diameter_after_merge(
        self, edges1: list[list[int]], edges2: list[list[int]], expected: int
    ):
        result = run_minimum_diameter_after_merge(Solution, edges1, edges2)
        assert_minimum_diameter_after_merge(result, expected)
