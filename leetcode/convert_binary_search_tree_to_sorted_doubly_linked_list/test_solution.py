import pytest

from leetcode_py import logged_test

from .helpers import assert_tree_to_doubly_list, run_tree_to_doubly_list
from .solution import Solution


class TestConvertBinarySearchTreeToSortedDoublyLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([4, 2, 5, 1, 3], [1, 2, 3, 4, 5]),
            ([2, 1, 3], [1, 2, 3]),
            ([], None),
            ([1], [1]),
            ([5, 3, 6, 2, 4, None, 7, 1], [1, 2, 3, 4, 5, 6, 7]),
            ([2, 1], [1, 2]),
            ([1, None, 2], [1, 2]),
            ([6, 2, 8, 1, 4, 7, 9, None, None, 3, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
            (
                [10, 4, 16, 2, 8, 12, 20, 1, 3, 6, 9, 11, 14, 18, 22],
                [1, 2, 3, 4, 6, 8, 9, 10, 11, 12, 14, 16, 18, 20, 22],
            ),
            (
                [15, 9, 21, 5, 12, 18, 25, 2, 7, 10, 13, 16, 20, 23, 27, 1, 3],
                [1, 2, 3, 5, 7, 9, 10, 12, 13, 15, 16, 18, 20, 21, 23, 25, 27],
            ),
            ([3, 1, 5, None, 2, 4, 6], [1, 2, 3, 4, 5, 6]),
            ([8, 3, 10, 1, 6, None, 14, None, None, 4, 7, 12], [1, 3, 4, 6, 7, 8, 10, 12, 14]),
        ],
    )
    def test_tree_to_doubly_list(
        self, root_list: list[int | None], expected_list: list[int] | None
    ):
        result = run_tree_to_doubly_list(Solution, root_list)
        assert_tree_to_doubly_list(result, expected_list)
