import pytest

from leetcode_py import logged_test

from .helpers import assert_find_frequent_tree_sum, run_find_frequent_tree_sum
from .solution import Solution


class TestMostFrequentSubtreeSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([5, 2, -3], [-3, 2, 4]),
            ([5, 2, -5], [2]),
            ([1], [1]),
            ([0], [0]),
            ([-1], [-1]),
            ([3, 1, 3], [1, 3, 7]),
            ([2, 2, 2], [2]),
            ([1, 2, 3], [2, 3, 6]),
            ([1, -2, -3], [-4, -3, -2]),
            ([5, 5, 5, 5, None, 5, 5], [5]),
            ([-3, -2, -1], [-6, -2, -1]),
            ([1, 1, 1, 1], [1]),
            ([1, None, 1, -2, -2, None, None, 0], [-2]),
            ([0, 0, -1], [-1]),
            ([-1, 2, None, 2], [2, 3, 4]),
            ([0, -2, -2, None, 0, None, None, None, 0], [-2, 0]),
            ([-1, -2, -2, -2], [-2]),
            ([1, -2, 0, None, None, -2], [-2]),
            ([-1, 0, 2, 0, None, None, None, -1], [-1]),
            ([1, -1, 2], [2]),
            ([-1, -1, 2], [-1, 0, 2]),
            ([2, 0, 0], [0]),
        ],
    )
    def test_find_frequent_tree_sum(self, root_list: list[int | None], expected: list[int]):
        result = run_find_frequent_tree_sum(Solution, root_list)
        assert_find_frequent_tree_sum(result, expected)
