import pytest

from leetcode_py import logged_test

from .helpers import assert_inorder_successor, run_inorder_successor
from .solution import Solution


class TestInorderSuccessorInBSTII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, node_val, expected_val",
        [
            ([2, 1, 3], 1, 2),
            ([5, 3, 6, 2, 4, None, None, 1], 6, None),
            ([5, 3, 6, 2, 4, None, None, 1], 1, 2),
            ([2, 1, 3], 3, None),
            ([2, 1, 3], 2, 3),
            ([6, 2, 8, 1, 4, 7, 9, None, None, 3, 5], 3, 4),
            ([6, 2, 8, 1, 4, 7, 9, None, None, 3, 5], 4, 5),
            ([6, 2, 8, 1, 4, 7, 9, None, None, 3, 5], 8, 9),
            ([6, 2, 8, 1, 4, 7, 9, None, None, 3, 5], 9, None),
            ([1], 1, None),
            ([15, 9, 21, 5, 12, 18, 25, 2, 7, 10, 13, 16, 20, 23, 27, 1, 3], 10, 12),
            ([3, 1, 5, None, 2, 4, 6], 2, 3),
        ],
    )
    def test_inorder_successor(
        self, root_list: list[int | None], node_val: int, expected_val: int | None
    ):
        result = run_inorder_successor(Solution, root_list, node_val)
        assert_inorder_successor(result, expected_val)
