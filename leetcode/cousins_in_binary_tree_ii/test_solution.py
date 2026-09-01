import pytest

from leetcode_py import logged_test

from .helpers import assert_replace_value_in_tree, run_replace_value_in_tree
from .solution import Solution


class TestCousinsInBinaryTreeII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([5, 4, 9, 1, 10, None, 7], [0, 0, 0, 7, 7, None, 11]),
            ([3, 1, 2], [0, 0, 0]),
            ([1], [0]),
            ([1, 2], [0, 0]),
            ([1, 2, 3], [0, 0, 0]),
            ([1, 2, 3, 4, 5], [0, 0, 0, 0, 0]),
            ([5, 4, 8, 11, None, 13, 4, 7, 2], [0, 0, 0, 17, None, 11, 11, 0, 0]),
            ([1, 2, None, 3, None, 4, None, 5], [0, 0, None, 0, None, 0, None, 0]),
            ([1, None, 2, None, 3, None, 4], [0, None, 0, None, 0, None, 0]),
            ([10, 5, 15, 3, 7, None, 20], [0, 0, 0, 20, 20, None, 10]),
            ([2, 3, 3, 4, 4, 4, 4], [0, 0, 0, 8, 8, 8, 8]),
            ([7, 7, 7, 7, 7], [0, 0, 0, 0, 0]),
            ([4, 9, None, None, 3, 5], [0, 0, None, None, 0, 0]),
            ([8, 4, 3, 2, 9, 5, None, 1], [0, 0, 0, 5, 5, 11, None, 0]),
            ([8, 7, 7, 3, 3, 1, 1, None, 5, 4], [0, 0, 0, 2, 2, 6, 6, None, 4, 5]),
            ([3, None, 7, 4, 5, 2, 4, 6, 1, 8, 1, 1], [0, None, 0, 0, 0, 7, 7, 6, 6, 1, 1, 9]),
            (
                [5, 4, 8, 9, 7, 6, 5, 8, None, None, 7, 5, 8, 8],
                [0, 0, 0, 11, 11, 16, 16, 28, None, None, 29, 23, 23, 28],
            ),
            (
                [4, 2, 1, 7, 2, 8, 5, 3, 3, 1, 1, 1, 4, 1, 3, 1],
                [0, 0, 0, 13, 13, 9, 9, 11, 11, 15, 15, 12, 12, 13, 13, 0],
            ),
        ],
    )
    def test_replace_value_in_tree(
        self, root_list: list[int | None], expected_list: list[int | None]
    ):
        result = run_replace_value_in_tree(Solution, root_list)
        assert_replace_value_in_tree(result, expected_list)
