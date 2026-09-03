import pytest

from leetcode_py import logged_test

from .helpers import assert_subtree_with_all_deepest, run_subtree_with_all_deepest
from .solution import Solution


class TestSmallestSubtreeWithAllTheDeepestNodes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [2, 7, 4]),
            ([1], [1]),
            ([0, 1, 3, None, 2], [2]),
            ([1, 2], [2]),
            ([1, None, 2], [2]),
            ([1, 2, 3], [1, 2, 3]),
            ([1, 2, 3, 4], [4]),
            ([1, 2, 3, None, 4], [4]),
            ([1, 2, 3, 4, 5], [2, 4, 5]),
            ([1, 2, 3, None, 4, None, 5], [1, 2, 3, None, 4, None, 5]),
            ([4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6], [6]),
            ([1, 2, 3, 4, None, 5, 6], [1, 2, 3, 4, None, 5, 6]),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8], [3, 7, 8]),
            ([485, 470, 407, 383, 143, 423, 8], [485, 470, 407, 383, 143, 423, 8]),
            ([215, 246, 330, 168, 362, 395, 361, None, None, None, None, 140], [140]),
            ([429, 167, 480, 256, 159, 341, 191, 83, 53], [256, 83, 53]),
        ],
    )
    def test_subtree_with_all_deepest(
        self, root_list: list[int | None], expected_list: list[int | None]
    ):
        result = run_subtree_with_all_deepest(Solution, root_list)
        assert_subtree_with_all_deepest(result, expected_list)
