import pytest

from leetcode_py import logged_test

from .helpers import assert_search_bst, run_search_bst
from .solution import Solution


class TestSearchInABinarySearchTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, val, expected_list",
        [
            ([4, 2, 7, 1, 3], 2, [2, 1, 3]),
            ([4, 2, 7, 1, 3], 5, []),
            ([5], 5, [5]),
            ([5], 3, []),
            ([5], 8, []),
            ([2, 1, 3], 1, [1]),
            ([2, 1, 3], 3, [3]),
            ([2, 1, 3], 4, []),
            ([4, 2, 6, 1, 3, 5], 5, [5]),
            ([4, 2, 7, 1, 3], 1, [1]),
            ([4, 2, 7, 1, 3], 3, [3]),
            ([4, 2, 7, 1, 3], 4, [4, 2, 7, 1, 3]),
            ([4, 2, 7, 1, 3], 6, []),
            ([1, None, 2, None, 3, None, 4, None, 5], 4, [4, None, 5]),
            ([1, None, 2, None, 3, None, 4, None, 5], 9, []),
            ([5, 4, None, 3, None, 2, None, 1], 2, [2, 1]),
            ([5, 4, None, 3, None, 2, None, 1], 6, []),
            ([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15], 11, [11]),
            ([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15], 16, []),
            ([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15], 5, [5]),
            ([10000000], 10000000, [10000000]),
            ([5000000, 2500000, 7500000, None, None, None, 10000000], 10000000, [10000000]),
            ([5000000, 2500000, 7500000, 1], 1, [1]),
            ([5000000, 2500000, 7500000, 1], 9999999, []),
        ],
    )
    def test_search_bst(
        self, root_list: list[int | None], val: int, expected_list: list[int | None]
    ):
        result = run_search_bst(Solution, root_list, val)
        assert_search_bst(result, expected_list)
