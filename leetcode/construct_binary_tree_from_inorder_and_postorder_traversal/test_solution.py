import pytest

from leetcode_py import logged_test

from .helpers import assert_build_tree, run_build_tree
from .solution import Solution


class TestConstructBinaryTreeFromInorderAndPostorderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "inorder, postorder, expected_list",
        [
            ([9, 3, 15, 20, 7], [9, 15, 7, 20, 3], [3, 9, 20, None, None, 15, 7]),
            ([-1], [-1], [-1]),
            ([1], [1], [1]),
            ([1, 2], [2, 1], [1, None, 2]),
            ([2, 1], [2, 1], [1, 2]),
            ([2, 1, 3], [2, 3, 1], [1, 2, 3]),
            ([1, 2, 3, 4], [1, 3, 2, 4], [4, 2, None, 1, 3]),
            ([3, 2, 1], [3, 2, 1], [1, 2, None, 3]),
            ([4, 3, 2, 1], [4, 3, 2, 1], [1, 2, None, 3, None, 4]),
            ([1, 2, 3, 4], [4, 3, 2, 1], [1, None, 2, None, 3, None, 4]),
            ([4, 2, 5, 1, 6, 3, 7], [4, 5, 2, 6, 7, 3, 1], [1, 2, 3, 4, 5, 6, 7]),
            ([-3, -1, 2], [-3, 2, -1], [-1, -3, 2]),
            ([2, 3, 1], [3, 2, 1], [1, 2, None, None, 3]),
            ([1, 3, 2], [3, 2, 1], [1, None, 2, 3]),
            (
                [8, 4, 9, 2, 10, 5, 11, 1, 12, 6, 13, 3, 14, 7, 15],
                [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1],
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
            ),
        ],
    )
    def test_build_tree(
        self, inorder: list[int], postorder: list[int], expected_list: list[int | None]
    ):
        result = run_build_tree(Solution, inorder, postorder)
        assert_build_tree(result, expected_list)
