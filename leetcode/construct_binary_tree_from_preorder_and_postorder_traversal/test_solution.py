import pytest

from leetcode_py import logged_test

from .helpers import assert_construct_from_pre_post, run_construct_from_pre_post
from .solution import Solution


class TestConstructBinaryTreeFromPreorderAndPostorderTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "preorder, postorder, expected",
        [
            (
                [1, 2, 4, 5, 3, 6, 7],
                [4, 5, 2, 6, 7, 3, 1],
                [[1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]],
            ),
            ([1], [1], [[1], [1]]),
            ([2, 1], [1, 2], [[2, 1], [1, 2]]),
            ([1, 2, 3], [3, 2, 1], [[1, 2, 3], [3, 2, 1]]),
            ([1, 2, 3], [2, 3, 1], [[1, 2, 3], [2, 3, 1]]),
            ([3, 4, 1, 2], [1, 4, 2, 3], [[3, 4, 1, 2], [1, 4, 2, 3]]),
            ([1, 2, 4, 5, 3], [4, 5, 2, 3, 1], [[1, 2, 4, 5, 3], [4, 5, 2, 3, 1]]),
            ([2, 1, 3], [3, 1, 2], [[2, 1, 3], [3, 1, 2]]),
            ([3, 1, 2, 4], [2, 1, 4, 3], [[3, 1, 2, 4], [2, 1, 4, 3]]),
            ([1, 2, 4, 3, 5], [3, 5, 4, 2, 1], [[1, 2, 4, 3, 5], [3, 5, 4, 2, 1]]),
            ([1, 2, 6, 4, 3, 5], [3, 5, 4, 6, 2, 1], [[1, 2, 6, 4, 3, 5], [3, 5, 4, 6, 2, 1]]),
            (
                [2, 1, 3, 8, 4, 5, 6, 7],
                [1, 7, 6, 5, 4, 8, 3, 2],
                [[2, 1, 3, 8, 4, 5, 6, 7], [1, 7, 6, 5, 4, 8, 3, 2]],
            ),
            (
                [1, 3, 2, 5, 4, 7, 6],
                [2, 4, 6, 7, 5, 3, 1],
                [[1, 3, 2, 5, 4, 7, 6], [2, 4, 6, 7, 5, 3, 1]],
            ),
            (
                [9, 2, 1, 7, 4, 3, 5, 6, 8],
                [1, 3, 6, 5, 4, 8, 7, 2, 9],
                [[9, 2, 1, 7, 4, 3, 5, 6, 8], [1, 3, 6, 5, 4, 8, 7, 2, 9]],
            ),
            (
                [9, 2, 1, 7, 4, 3, 6, 5, 8, 10],
                [1, 3, 5, 6, 4, 8, 7, 2, 10, 9],
                [[9, 2, 1, 7, 4, 3, 6, 5, 8, 10], [1, 3, 5, 6, 4, 8, 7, 2, 10, 9]],
            ),
            (
                [6, 3, 1, 2, 4, 5, 11, 10, 8, 7, 9, 12, 13, 15, 14],
                [2, 1, 5, 4, 3, 7, 9, 8, 10, 14, 15, 13, 12, 11, 6],
                [
                    [6, 3, 1, 2, 4, 5, 11, 10, 8, 7, 9, 12, 13, 15, 14],
                    [2, 1, 5, 4, 3, 7, 9, 8, 10, 14, 15, 13, 12, 11, 6],
                ],
            ),
        ],
    )
    def test_construct_from_pre_post(
        self, preorder: list[int], postorder: list[int], expected: list[list[int]]
    ):
        result = run_construct_from_pre_post(Solution, preorder, postorder)
        assert_construct_from_pre_post(result, expected)
