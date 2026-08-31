import pytest

from leetcode_py import logged_test

from .helpers import assert_boundary_of_binary_tree, run_boundary_of_binary_tree
from .solution import Solution


class TestBoundaryOfBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, None, 2, 3, 4], [1, 3, 4, 2]),
            ([1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10], [1, 2, 4, 7, 8, 9, 10, 6, 3]),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([1, None, 2], [1, 2]),
            ([1, 2, 3, 4, 5], [1, 2, 4, 5, 3]),
            ([1, 2, None, 3, None, 4], [1, 2, 3, 4]),
            ([1, None, 2, None, 3, None, 4], [1, 4, 3, 2]),
            ([1, 2, 3, 4, None, 6, 7], [1, 2, 4, 6, 7, 3]),
            (
                [1, 2, 3, None, 5, 6, 7, None, 8, None, None, None, None, 9],
                [1, 2, 5, 8, 9, 6, 7, 3],
            ),
            ([5], [5]),
            ([1, 2, 3, 4, 5, None, None, None, None, None, None, 8, 9], [1, 2, 4, 5, 3]),
        ],
    )
    def test_boundary_of_binary_tree(self, root_list: list[int | None], expected: list[int]):
        result = run_boundary_of_binary_tree(Solution, root_list)
        assert_boundary_of_binary_tree(result, expected)
