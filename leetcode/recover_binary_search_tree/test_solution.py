import pytest

from leetcode_py import logged_test

from .helpers import assert_recover_tree, run_recover_tree
from .solution import Solution


class TestRecoverBinarySearchTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([1, 3, None, None, 2], [3, 1, None, None, 2]),
            ([3, 1, 4, None, None, 2], [2, 1, 4, None, None, 3]),
            ([2, 3, 1], [2, 1, 3]),
            ([3, 1, 2, None, None, None, 4], [2, 1, 3, None, None, None, 4]),
            ([5, 3, 8, 9, 4, 7, 1], [5, 3, 8, 1, 4, 7, 9]),
            ([5, 7, 8, 1, 4, 3, 9], [5, 3, 8, 1, 4, 7, 9]),
            ([1, 2], [2, 1]),
            ([3, None, 2, None, 1], [1, None, 2, None, 3]),
            (
                [10, 13, 15, 3, 7, 5, 18, 1, None, 6, None],
                [10, 5, 15, 3, 7, 13, 18, 1, None, 6, None],
            ),
            ([1, -3, None, None, 2], [2, -3, None, None, 1]),
            ([1, 2, 6, 4, 3, 5, 7], [4, 2, 6, 1, 3, 5, 7]),
            ([3, 4, None, 2, None, 1, None], [4, 3, None, 2, None, 1, None]),
            ([100, 50, 200, 250, 75, 150, 25], [100, 50, 200, 25, 75, 150, 250]),
            ([2, 1, None, None, 3], [3, 1, None, None, 2]),
        ],
    )
    def test_recover_tree(self, root_list: list[int | None], expected_list: list[int | None]):
        result = run_recover_tree(Solution, root_list)
        assert_recover_tree(result, expected_list)
