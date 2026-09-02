import pytest

from leetcode_py import logged_test

from .helpers import assert_linked_list_random_node, run_linked_list_random_node
from .solution import Solution


class TestLinkedListRandomNode:
    @logged_test
    @pytest.mark.parametrize(
        "operations, inputs, expected",
        [
            (["Solution", "get_random"], [[1], []], [1]),
            (["Solution", "get_random", "get_random"], [[2], [], []], [2]),
            (
                ["Solution", "get_random", "get_random", "get_random"],
                [[1, 2, 3], [], [], []],
                [1, 2, 3],
            ),
            (["Solution", "get_random"], [[42], []], [42]),
            (["Solution", "get_random", "get_random"], [[1, 2], [], []], [1, 2]),
            (["Solution", "get_random", "get_random"], [[-3, 7], [], []], [-3, 7]),
            (["Solution", "get_random", "get_random", "get_random"], [[5], [], [], []], [5]),
            (["Solution", "get_random", "get_random", "get_random"], [[8, 8], [], [], []], [8, 8]),
            (["Solution", "get_random"], [[-10000, 10000], []], [-10000, 10000]),
            (["Solution", "get_random", "get_random"], [[10, 20, 30], [], []], [10, 20, 30]),
            (["Solution", "get_random", "get_random"], [[0, 0], [], []], [0, 0]),
            (["Solution", "get_random", "get_random"], [[4, 4, 4, 4], [], []], [4, 4, 4, 4]),
            (["Solution", "get_random", "get_random"], [[-1, 1], [], []], [-1, 1]),
            (["Solution", "get_random"], [[7, 8, 9, 10], []], [7, 8, 9, 10]),
            (
                ["Solution", "get_random", "get_random", "get_random"],
                [[3, 1, 2], [], [], []],
                [3, 1, 2],
            ),
            (["Solution", "get_random", "get_random"], [[100, -100], [], []], [100, -100]),
        ],
    )
    def test_linked_list_random_node(
        self, operations: list[str], inputs: list[list[int]], expected: list[int]
    ):
        result = run_linked_list_random_node(Solution, operations, inputs)
        assert_linked_list_random_node(result, expected)
