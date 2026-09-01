import pytest

from leetcode_py import logged_test

from .helpers import assert_lowest_common_ancestor, run_lowest_common_ancestor
from .solution import Solution


class TestLowestCommonAncestorOfABinaryTreeIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, p_val, q_val, expected_val",
        [
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1, 3),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4, 5),
            ([1, 2], 1, 2, 1),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 7, 4, 2),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 8, 3),
            ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 0, 3),
            ([1, 2, 3, 4, 5, 6, 7], 4, 5, 2),
            ([1, 2, 3, 4, 5, 6, 7], 2, 3, 1),
            ([1, 2, 3, 4, 5, 6, 7], 4, 7, 1),
            ([1, 2, 3, 4, 5, 6, 7], 5, 6, 1),
            ([1, 2, 3, 4, 5, 6, 7], 6, 7, 3),
            ([1, 2, None, 3, None, 4, None, 5], 5, 2, 2),
            ([-1, None, 9, -8, None, None, 7], -1, 7, -1),
            ([2, 1], 2, 1, 2),
            ([1, 2, None, 3, None, 4], 4, 2, 2),
            ([1, 2, None, 3, None, 4, None, 5, None, 6], 3, 1, 1),
            ([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8], 6, 4, 4),
            ([1, 2, None, 3, None, 4, None, 5, None, 6, None, 7, None, 8, None, 9], 2, 3, 2),
        ],
    )
    def test_lowest_common_ancestor(
        self, root_list: list[int | None], p_val: int, q_val: int, expected_val: int
    ):
        result = run_lowest_common_ancestor(Solution, root_list, p_val, q_val)
        assert_lowest_common_ancestor(result, expected_val)
