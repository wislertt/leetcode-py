import pytest

from leetcode_py import logged_test

from .helpers import assert_create_binary_tree, run_create_binary_tree
from .solution import Solution


class TestCreateBinaryTreeFromDescriptions:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "descriptions_list, expected_list",
        [
            (
                [[20, 15, 1], [20, 17, 0], [50, 20, 1], [50, 80, 0], [80, 19, 1]],
                [50, 20, 80, 15, 17, 19],
            ),
            ([[1, 2, 1], [2, 3, 0], [3, 4, 1]], [1, 2, None, None, 3, 4]),
            ([[1, 2, 1], [1, 3, 0]], [1, 2, 3]),
            ([[1, 3, 0], [1, 2, 1]], [1, 2, 3]),
            ([[7, 3, 1]], [7, 3]),
            ([[1, 2, 0]], [1, None, 2]),
            ([[1, 2, 1], [2, 3, 1], [3, 4, 1]], [1, 2, None, 3, None, 4]),
            ([[1, 2, 0], [2, 3, 0], [3, 4, 0]], [1, None, 2, None, 3, None, 4]),
            ([[1, 2, 1], [2, 3, 0], [3, 4, 1], [4, 5, 0]], [1, 2, None, None, 3, 4, None, None, 5]),
            ([[100000, 99999, 1], [100000, 50000, 0]], [100000, 99999, 50000]),
            (
                [[50, 20, 1], [20, 15, 1], [20, 17, 0], [50, 80, 0], [80, 19, 1]],
                [50, 20, 80, 15, 17, 19],
            ),
            (
                [[2, 1, 1], [3, 2, 0], [4, 3, 1], [5, 4, 0], [6, 5, 1]],
                [6, 5, None, None, 4, 3, None, None, 2, 1],
            ),
            ([[9, 7, 1], [9, 8, 0], [7, 6, 1], [8, 5, 0]], [9, 7, 8, 6, None, None, 5]),
            ([[6, 4, 1], [6, 5, 0], [4, 3, 1], [5, 2, 0]], [6, 4, 5, 3, None, None, 2]),
            ([[66975, 47924, 1], [66975, 84909, 0]], [66975, 47924, 84909]),
            ([[61408, 44298, 0], [41100, 61408, 0]], [41100, None, 61408, None, 44298]),
        ],
    )
    def test_create_binary_tree(
        self, descriptions_list: list[list[int]], expected_list: list[int | None]
    ):
        result = run_create_binary_tree(Solution, descriptions_list)
        assert_create_binary_tree(result, expected_list)
