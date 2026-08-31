import pytest

from leetcode_py import logged_test

from .helpers import assert_trim_bst, run_trim_bst
from .solution import Solution


class TestTrimABinarySearchTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, low, high, expected_list",
        [
            ([1, 0, 2], 1, 2, [1, None, 2]),
            ([3, 0, 4, None, 2, None, None, 1], 1, 3, [3, 2, None, 1]),
            ([1], 1, 1, [1]),
            ([1], 2, 3, []),
            ([2, 1, 3], 2, 3, [2, None, 3]),
            ([2, 1, 3], 1, 3, [2, 1, 3]),
            ([3, 1, 4, None, 2], 3, 4, [3, None, 4]),
            ([10, 5, 15, 3, 7, None, 18], 7, 15, [10, 7, 15]),
            ([1, None, 2], 1, 2, [1, None, 2]),
            ([1, None, 2], 2, 2, [2]),
            ([5, 2, 6, 1, 3, None, 8], 2, 6, [5, 2, 6, None, 3]),
            ([4, 2, 6, 1, 3, 5, 7], 2, 6, [4, 2, 6, None, 3, 5]),
            ([100], 0, 104, [100]),
            ([3, 2, 4, 1], 2, 3, [3, 2]),
            ([6, 4, 8, 2, 5, 7, 9, 1, 3], 3, 7, [6, 4, 7, 3, 5]),
        ],
    )
    def test_trim_bst(
        self, root_list: list[int | None], low: int, high: int, expected_list: list[int | None]
    ):
        result = run_trim_bst(Solution, root_list, low, high)
        assert_trim_bst(result, expected_list)
