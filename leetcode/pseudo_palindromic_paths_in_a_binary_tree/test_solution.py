import pytest

from leetcode_py import logged_test

from .helpers import assert_pseudo_palindromic_paths, run_pseudo_palindromic_paths
from .solution import Solution


class TestPseudoPalindromicPathsInABinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([2, 3, 1, 3, 1, None, 1], 2),
            ([2, 1, 1, 1, 3, None, None, None, None, None, 1], 1),
            ([9], 1),
            ([1], 1),
            ([1, 2], 0),
            ([1, 1], 1),
            ([1, 2, 3], 0),
            ([1, 2, 2], 0),
            ([1, 1, 1], 2),
            ([1, 2, None, 3], 0),
            ([1, None, 2, None, 3], 0),
            ([1, 2, 3, 4, None, None, 5], 0),
            ([2, 3, 1, 3, 1, None, 1, None, 1], 1),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0),
            ([1, 4, None, 2, 4, 8, None, None], 1),
            ([6, None, 6, 3, None, 5, 4, None, None, 4, 9, 9, 3], 1),
            ([1, 3, None, None, 7, 3, 4], 0),
            ([1, None, 4, None, 4, None], 1),
            ([3, None, 7], 0),
            ([5, None, 1, None, 5, None, 7, None, 6, 6, None, 6], 0),
            ([1, 9, 3, 9, 2, 6, 6, None, 2, 4, 6, None, 4], 0),
            ([8, None, 9, 7, None, None, 3, None, 9, 8, None], 0),
            ([3, 6, None, 3, 9, None, 2, None, None, 8, None, 1, 2, 2, 2], 0),
            ([8, 8, None, 8], 1),
            ([1, None, None], 1),
            ([1, 2, 2, 9, 6, 1, 1, None, 6, 7, 2, 5], 1),
            ([9, 4, None], 0),
            ([3, None, 9, None, 2, 6, 2, 6, None, 5, 3, 2], 1),
        ],
    )
    def test_pseudo_palindromic_paths(self, root_list: list[int | None], expected: int):
        result = run_pseudo_palindromic_paths(Solution, root_list)
        assert_pseudo_palindromic_paths(result, expected)
