import pytest

from leetcode_py import logged_test

from .helpers import assert_good_nodes, run_good_nodes
from .solution import Solution


class TestCountGoodNodesInBinaryTree:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([3, 1, 4, 3, None, 1, 5], 4),
            ([3, 3, None, 4, 2], 3),
            ([1], 1),
            ([], 0),
            ([5], 1),
            ([2, 1], 1),
            ([2, 3], 2),
            ([1, 2, 3], 3),
            ([3, 2, 1], 1),
            ([-1, -2, -3], 1),
            ([-3, -1, -4], 2),
            ([1, 2, 3, 4, 5, 6, 7], 7),
            ([7, 6, 5, 4, 3, 2, 1], 1),
            ([10, 5, 15], 2),
            ([10, 10, 10], 3),
            ([4, 2, 6, 1, 3, 5, 7], 3),
            ([1, 1, 1, 1, None, 1, 1], 6),
        ],
    )
    def test_good_nodes(self, root_list: list[int | None], expected: int):
        result = run_good_nodes(Solution, root_list)
        assert_good_nodes(result, expected)
