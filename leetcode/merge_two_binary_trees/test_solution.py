import pytest

from leetcode_py import logged_test

from .helpers import assert_merge_trees, run_merge_trees
from .solution import Solution


class TestMergeTwoBinaryTrees:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root1_list, root2_list, expected",
        [
            ([1, 3, 2, 5], [2, 1, 3, None, 4, None, 7], [3, 4, 5, 5, 4, None, 7]),
            ([1], [1, 2], [2, 2]),
            ([], [], []),
            ([], [1, 2, 3], [1, 2, 3]),
            ([1, 2, 3], [], [1, 2, 3]),
            ([1, 2, 3], [4, 5, 6], [5, 7, 9]),
            ([1, None, 3], [2, 4], [3, 4, 3]),
            ([1, 2, None], [1, None, 3], [2, 2, 3]),
            ([-1, -2, -3], [1, 2, 3], [0, 0, 0]),
            ([1, 2, 3, 4, 5], [10, 20, 30], [11, 22, 33, 4, 5]),
            ([1], [1, 2, 3, 4, 5, 6, 7], [2, 2, 3, 4, 5, 6, 7]),
            ([1, 2, None, 4], [1, None, 3], [2, 2, 3, 4]),
        ],
    )
    def test_merge_trees(
        self, root1_list: list[int | None], root2_list: list[int | None], expected: list[int | None]
    ):
        result = run_merge_trees(Solution, root1_list, root2_list)
        assert_merge_trees(result, expected)
