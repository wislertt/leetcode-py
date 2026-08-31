import pytest

from leetcode_py import logged_test

from .helpers import assert_min_diff_in_bst, run_min_diff_in_bst
from .solution import Solution


class TestMinDistanceBetweenBstNodes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([4, 2, 6, 1, 3], 1),
            ([1, 0, 48, None, None, 12, 49], 1),
            ([27, None, 40, 30, 45], 3),
            ([90, None, 100, 99, 101], 1),
            ([2, 1, 4], 1),
            ([5, 3, 7, 1, 4], 1),
            ([10, 5, 20, 3, 7, 15, 30], 2),
            ([10, 5], 5),
            ([40, None, 70, 60, 80], 10),
            ([236, 104, 701, None, 227, None, 911], 9),
            ([50, 30, 70, 20, 40, 60, 80], 10),
            ([17, 9, 30, None, 12, 24, 45], 3),
        ],
    )
    def test_min_diff_in_bst(self, root_list: list[int | None], expected: int):
        result = run_min_diff_in_bst(Solution, root_list)
        assert_min_diff_in_bst(result, expected)
