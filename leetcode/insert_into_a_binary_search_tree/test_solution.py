import pytest

from leetcode_py import logged_test

from .helpers import assert_insert_into_bst, run_insert_into_bst
from .solution import Solution


class TestInsertIntoABinarySearchTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, val, expected",
        [
            ([4, 2, 7, 1, 3], 5, [1, 2, 3, 4, 5, 7]),
            ([40, 20, 60, 10, 30, 50, 70], 25, [10, 20, 25, 30, 40, 50, 60, 70]),
            ([4, 2, 7, 1, 3, None, None, None, None, None, None], 5, [1, 2, 3, 4, 5, 7]),
            ([], 5, [5]),
            ([5], 3, [3, 5]),
            ([5], 7, [5, 7]),
            ([2, 1, 3], 4, [1, 2, 3, 4]),
            ([2, 1, 3], 0, [0, 1, 2, 3]),
            ([5, 3, 6, 2, 4, None, 7], 8, [2, 3, 4, 5, 6, 7, 8]),
            ([5, 3, 6, 2, 4, None, 7], 1, [1, 2, 3, 4, 5, 6, 7]),
            ([1, None, 2], 3, [1, 2, 3]),
            ([3, 1, None, None, 2], 4, [1, 2, 3, 4]),
            ([10, 5, 15, None, None, 12, 20], 8, [5, 8, 10, 12, 15, 20]),
            ([10, 5, 15, None, None, 12, 20], 17, [5, 10, 12, 15, 17, 20]),
        ],
    )
    def test_insert_into_bst(self, root_list: list[int | None], val: int, expected: list[int]):
        result = run_insert_into_bst(Solution, root_list, val)
        assert_insert_into_bst(result, expected)
