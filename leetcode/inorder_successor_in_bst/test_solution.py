import pytest

from leetcode_py import logged_test

from .helpers import assert_inorder_successor, run_inorder_successor
from .solution import Solution


class TestInorderSuccessorInBST:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, p_val, expected_val",
        [
            ([2, 1, 3], 1, 2),
            ([5, 3, 6, 2, 4, None, None, 1], 6, None),
            ([5, 3, 6, 2, 4, None, None, 1], 1, 2),
            ([5, 3, 6, 2, 4, None, None, 1], 2, 3),
            ([5, 3, 6, 2, 4, None, None, 1], 3, 4),
            ([5, 3, 6, 2, 4, None, None, 1], 4, 5),
            ([5, 3, 6, 2, 4, None, None, 1], 5, 6),
            ([2, 1], 1, 2),
            ([2, 1], 2, None),
            ([2, None, 3], 2, 3),
            ([2, None, 3], 3, None),
            ([1], 1, None),
            ([20, 10, 30, 5, 15, None, 40, None, None, 12, 17], 15, 17),
            ([20, 10, 30, 5, 15, None, 40, None, None, 12, 17], 17, 20),
            ([20, 10, 30, 5, 15, None, 40, None, None, 12, 17], 12, 15),
            ([3, 1, 4, None, 2], 2, 3),
        ],
    )
    def test_inorder_successor(
        self, root_list: list[int | None], p_val: int, expected_val: int | None
    ):
        result = run_inorder_successor(Solution, root_list, p_val)
        assert_inorder_successor(result, expected_val)
