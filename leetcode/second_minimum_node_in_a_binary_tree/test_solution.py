import pytest

from leetcode_py import logged_test

from .helpers import assert_find_second_minimum_value, run_find_second_minimum_value
from .solution import Solution


class TestSecondMinimumNodeInABinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([2, 2, 5, None, None, 5, 7], 5),
            ([2, 2, 2], -1),
            ([1], -1),
            ([1, 1, 2], 2),
            ([5, 5, 6], 6),
            ([2, 2, 3], 3),
            ([1, 1, 1, 1, 1], -1),
            ([1, 1, 2, 1, 2], 2),
            ([3, 3, 5, 3, 4], 4),
            ([2, 2, 3, 2, 2, 3, 3], 3),
            ([2147483647, 2147483647, 2147483647], -1),
            ([2147483646, 2147483646, 2147483647], 2147483647),
            ([3, 4, 3], 4),
            ([1, 1, 1, 3, 1, 1, 2], 2),
            ([1, 1, 3, 2, 1, 4, 3], 2),
            ([2, 4, 2, None, None, 2, 3, 2, 4], 3),
            ([1, 2, 1, 5, 2, 1, 3], 2),
            ([3], -1),
        ],
    )
    def test_find_second_minimum_value(self, root_list: list[int | None], expected: int):
        result = run_find_second_minimum_value(Solution, root_list)
        assert_find_second_minimum_value(result, expected)
