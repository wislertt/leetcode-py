import pytest

from leetcode_py import logged_test

from .helpers import assert_upside_down_binary_tree, run_upside_down_binary_tree
from .solution import Solution


class TestBinaryTreeUpsideDown:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected_list",
        [
            ([1, 2, 3, 4, 5], [4, 5, 2, None, None, 3, 1]),
            ([], []),
            ([1], [1]),
            ([1, 2, 3], [2, 3, 1]),
            ([1, 2], [2, None, 1]),
            ([1, 2, None, 3], [3, None, 2, None, 1]),
            ([1, 2, 3, 4], [4, None, 2, 3, 1]),
            ([1, 2, 3, 4, 5, None, None, 8, 9], [8, 9, 4, None, None, 5, 2, None, None, 3, 1]),
            ([5, 3, 8, 1, 4], [1, 4, 3, None, None, 8, 5]),
            ([1, 2, 2, 3, 3], [3, 3, 2, None, None, 2, 1]),
            ([2, 1, 3], [1, 3, 2]),
            ([7, 5, 9, 3, 6], [3, 6, 5, None, None, 9, 7]),
            ([4, 2, None, 1], [1, None, 2, None, 4]),
            ([0, 1, 2], [1, 2, 0]),
        ],
    )
    def test_upside_down_binary_tree(
        self, root_list: list[int | None], expected_list: list[int | None]
    ):
        result = run_upside_down_binary_tree(Solution, root_list)
        assert_upside_down_binary_tree(result, expected_list)
