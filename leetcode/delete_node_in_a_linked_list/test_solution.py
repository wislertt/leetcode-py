import pytest

from leetcode_py import logged_test

from .helpers import assert_delete_node, run_delete_node
from .solution import Solution


class TestDeleteNodeInALinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, node_val, expected_list",
        [
            ([4, 5, 1, 9], 5, [4, 1, 9]),
            ([4, 5, 1, 9], 1, [4, 5, 9]),
            ([1, 2], 1, [2]),
            ([1, 2, 4], 2, [1, 4]),
            ([0, 1], 0, [1]),
            ([2, 4, 3], 4, [2, 3]),
            ([10, 20, 30, 40], 20, [10, 30, 40]),
            ([-1, -2, -3], -2, [-1, -3]),
            ([100, -100, 0], -100, [100, 0]),
            ([1, 2, 3, 4, 5], 4, [1, 2, 3, 5]),
            ([5, 1, 9], 1, [5, 9]),
            ([3, 6, 2, 8, 7], 8, [3, 6, 2, 7]),
            ([-1000, 1000], -1000, [1000]),
            ([0, -3, 9, -7, 4], -7, [0, -3, 9, 4]),
            ([1, 3, 5, 7, 9, 11], 7, [1, 3, 5, 9, 11]),
        ],
    )
    def test_delete_node(self, head_list: list[int], node_val: int, expected_list: list[int]):
        result = run_delete_node(Solution, head_list, node_val)
        assert_delete_node(result, expected_list)
