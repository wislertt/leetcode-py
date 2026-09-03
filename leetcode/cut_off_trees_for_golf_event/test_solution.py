import pytest

from leetcode_py import logged_test

from .helpers import assert_cut_off_tree, run_cut_off_tree
from .solution import Solution


class TestCutOffTreesForGolfEvent:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "forest, expected",
        [
            ([[1, 2, 3], [0, 0, 4], [7, 6, 5]], 6),
            ([[1, 2, 3], [0, 0, 0], [7, 6, 5]], -1),
            ([[2, 3, 4], [0, 0, 5], [8, 7, 6]], 6),
            ([[2]], 0),
            ([[1, 2]], 1),
            ([[2, 1]], 0),
            ([[1, 1], [1, 2]], 2),
            ([[1, 1], [0, 3], [2, 1]], 6),
            ([[3, 1], [2, 1]], 2),
            ([[4, 2, 3], [0, 0, 1], [0, 0, 5]], 8),
            ([[2, 0, 0], [0, 0, 0], [0, 0, 3]], -1),
            ([[1, 2, 1], [1, 0, 1], [1, 9, 1]], 5),
            ([[9, 8, 7, 6], [1, 1, 1, 1], [2, 3, 4, 5]], 10),
            ([[1000000000, 1, 1], [1, 0, 1], [1, 1, 1]], 0),
            ([[1, 1, 1, 27], [1, 1, 1, 1], [1, 1, 1, 1]], 3),
            ([[1, 1, 1, 35], [1, 1, 1, 14], [1, 1, 1, 1]], 5),
            ([[1, 49, 1, 0], [1, 0, 1, 0]], 1),
            ([[1, 1], [1, 1], [1, 9], [1, 1]], 3),
        ],
    )
    def test_cut_off_tree(self, forest: list[list[int]], expected: int):
        result = run_cut_off_tree(Solution, forest)
        assert_cut_off_tree(result, expected)
