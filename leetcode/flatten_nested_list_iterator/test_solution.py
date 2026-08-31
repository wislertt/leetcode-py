from typing import Any

import pytest

from leetcode_py import logged_test

from .helpers import assert_flatten_nested_list_iterator, run_flatten_nested_list_iterator
from .solution import NestedIterator


class TestFlattenNestedListIterator:
    @logged_test
    @pytest.mark.parametrize(
        "nested_list, expected",
        [
            ([[1, 1], 2, [1, 1]], [1, 1, 2, 1, 1]),
            ([1, [4, [6]]], [1, 4, 6]),
            ([1], [1]),
            ([[]], []),
            ([[], [[]]], []),
            ([[], 1, []], [1]),
            ([[[[[5]]]]], [5]),
            ([1, [2, [3, [4, [5]]]]], [1, 2, 3, 4, 5]),
            ([[-1, [0], 1], [-2]], [-1, 0, 1, -2]),
            ([[1000000], [[-1000000]]], [1000000, -1000000]),
            ([[1, 2], [3, [4, 5]], [6, [7, [8, [9, [10]]]]]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ([[], [1, []], [2, [[]]], 3], [1, 2, 3]),
            ([0, [0, [0]]], [0, 0, 0]),
            ([[[], []], [], [[]]], []),
        ],
    )
    def test_flatten_nested_list_iterator(self, nested_list: list[Any], expected: list[Any]):
        result = run_flatten_nested_list_iterator(NestedIterator, nested_list)
        assert_flatten_nested_list_iterator(result, expected)
