import pytest

from leetcode_py import logged_test

from .helpers import assert_find_closest_leaf, run_find_closest_leaf
from .solution import Solution


class TestClosestLeafInABinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, k, expected",
        [
            ([1], 1, 1),
            ([1, 2, 3, 4, None, None, None, 5, None, 6], 2, 3),
            ([1, 2, 3, None, 4, 5, 6, None, None, 7, 8, None, 9], 4, 4),
            ([1, 2, 3], 3, 3),
            ([1, 2, 3, 4, 5], 1, 3),
            ([2, 1, 3, None, 4], 1, 4),
            ([5, 4, 3, None, None, 6], 4, 4),
            ([1, 2, 3, 4], 2, 4),
            ([10, 5, 15, 3, 7, 12, 18], 7, 7),
            ([1, 2], 2, 2),
            ([3, 1, 4, None, 2], 4, 4),
            ([9, 8, 7, 6], 8, 6),
        ],
    )
    def test_find_closest_leaf(self, root_list: list[int | None], k: int, expected: int):
        result = run_find_closest_leaf(Solution, root_list, k)
        assert_find_closest_leaf(result, expected)
