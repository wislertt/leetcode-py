import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_bst_subtree, run_largest_bst_subtree
from .solution import Solution


class TestLargestBSTSubtree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([10, 5, 15, 1, 8, None, 7], 3),
            ([4, 2, 7, 2, 3, 5, None, 2, None, None, None, None, None, 1], 2),
            ([], 0),
            ([1], 1),
            ([2, 1, 3], 3),
            ([5, 6, 7], 1),
            ([3, 2, 4, 1], 4),
            ([10, 5, 15, 1, 8, 7, 9], 3),
            ([1, None, 2, None, 3, None, 4], 4),
            ([2, 2, 2], 1),
            ([-1, None, 0, None, 1, None, 2], 4),
            ([10, 4, 15, 2, 6, 12, 20], 7),
            ([10, 5, 15, 1, 8, None, 7, None, 9], 2),
            ([50, 30, 70, 20, 40, 60, 80], 7),
            ([50, 30, 70, None, None, 60, 80, None, None, 55], 2),
        ],
    )
    def test_largest_bst_subtree(self, root_list: list[int | None], expected: int):
        result = run_largest_bst_subtree(Solution, root_list)
        assert_largest_bst_subtree(result, expected)
