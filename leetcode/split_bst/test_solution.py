import pytest

from leetcode_py import logged_test

from .helpers import assert_split_bst, run_split_bst
from .solution import Solution


class TestSplitBST:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, target, expected_lists",
        [
            ([4, 2, 6, 1, 3, 5, 7], 2, [[2, 1], [4, 3, 6, None, None, 5, 7]]),
            ([1], 1, [[1], []]),
            ([1], 0, [[], [1]]),
            ([2, 1, 3], 1, [[1], [2, None, 3]]),
            ([2, 1, 3], 2, [[2, 1], [3]]),
            ([2, 1, 3], 0, [[], [2, 1, 3]]),
            ([2, 1, 3], 3, [[2, 1, 3], []]),
            ([3, 1, 5, None, 2, 4, 6], 2, [[1, None, 2], [3, None, 5, 4, 6]]),
            ([3, 1, 5, None, 2, 4, 6], 3, [[3, 1, None, None, 2], [5, 4, 6]]),
            ([10, 5, 15, 3, 7, None, 18], 7, [[5, 3, 7], [10, None, 15, None, 18]]),
            ([10, 5, 15, 3, 7, None, 18], 5, [[5, 3], [10, 7, 15, None, None, None, 18]]),
            ([10, 5, 15, 3, 7, None, 18], 11, [[10, 5, None, 3, 7], [15, None, 18]]),
            ([5, 3, 8, 1, 4, 7, 9, None, 2], 4, [[3, 1, 4, None, 2], [5, None, 8, 7, 9]]),
            ([1000], 1000, [[1000], []]),
            ([1000], 0, [[], [1000]]),
            ([1, None, 1000], 500, [[1], [1000]]),
            ([6, 4, 8, 3, 5, 7, 9], 5, [[4, 3, 5], [6, None, 8, 7, 9]]),
            ([6, 4, 8, 3, 5, 7, 9], 8, [[6, 4, 8, 3, 5, 7], [9]]),
            ([959], 500, [[], [959]]),
            ([93, None, 442, 127, 452], 741, [[93, None, 442, 127, 452], []]),
            ([583], 704, [[583], []]),
            ([738, 439, None, 159], 971, [[738, 439, None, 159], []]),
            ([490, 250, 818], 392, [[250], [490, None, 818]]),
            ([388, None, 819, None, 855], 615, [[388], [819, None, 855]]),
        ],
    )
    def test_split_bst(
        self, root_list: list[int | None], target: int, expected_lists: list[list[int | None]]
    ):
        result = run_split_bst(Solution, root_list, target)
        assert_split_bst(result, expected_lists)
