import pytest

from leetcode_py import logged_test

from .helpers import assert_swap_nodes, run_swap_nodes
from .solution import Solution


class TestSwappingNodesInALinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, k, expected",
        [
            ([1, 2, 3, 4, 5], 2, [1, 4, 3, 2, 5]),
            ([7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5, [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]),
            ([1], 1, [1]),
            ([1, 2], 1, [2, 1]),
            ([1, 2], 2, [2, 1]),
            ([1, 2, 3], 1, [3, 2, 1]),
            ([1, 2, 3], 2, [1, 2, 3]),
            ([1, 2, 3], 3, [3, 2, 1]),
            ([1, 2, 3, 4], 1, [4, 2, 3, 1]),
            ([1, 2, 3, 4], 2, [1, 3, 2, 4]),
            ([1, 2, 3, 4], 3, [1, 3, 2, 4]),
            ([1, 2, 3, 4], 4, [4, 2, 3, 1]),
            ([0, 0, 0], 2, [0, 0, 0]),
            ([5, 1, 9], 2, [5, 1, 9]),
            ([10, 20, 30, 40, 50, 60], 3, [10, 20, 40, 30, 50, 60]),
            ([100, 1], 1, [1, 100]),
            ([51, 82, 84, 55], 2, [51, 84, 82, 55]),
            ([46, 93, 0, 87, 11], 4, [46, 87, 0, 93, 11]),
            ([50, 10, 61, 68, 75, 40, 87, 82], 8, [82, 10, 61, 68, 75, 40, 87, 50]),
            ([51, 97, 34, 51, 34, 13, 42, 34], 5, [51, 97, 34, 34, 51, 13, 42, 34]),
            ([74, 42, 0, 90, 28, 99, 22, 82], 2, [74, 22, 0, 90, 28, 99, 42, 82]),
            ([22, 77, 57, 30, 55, 91, 99], 3, [22, 77, 55, 30, 57, 91, 99]),
            ([17, 79], 1, [79, 17]),
            ([9, 9, 36, 23, 93], 1, [93, 9, 36, 23, 9]),
        ],
    )
    def test_swap_nodes(self, head_list: list[int], k: int, expected: list[int]):
        result = run_swap_nodes(Solution, head_list, k)
        assert_swap_nodes(result, expected)
