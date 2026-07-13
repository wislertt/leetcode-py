import pytest

from leetcode_py import logged_test

from .helpers import assert_delete_node, run_delete_node
from .solution import Solution


class TestDeleteNodeInABST:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, key, expected",
        [
            ([5, 3, 6, 2, 4, None, 7], 3, [2, 4, 5, 6, 7]),
            ([5, 3, 6, 2, 4, None, 7], 0, [2, 3, 4, 5, 6, 7]),
            ([], 0, []),
            ([5], 5, []),
            ([5], 3, [5]),
            ([2, 1, 3], 2, [1, 3]),
            ([5, 3, 6, 2, 4, None, 7], 5, [2, 3, 4, 6, 7]),
            ([5, 3, 6, 2, 4, None, 7], 7, [2, 3, 4, 5, 6]),
            ([5, 3, 6, 2, 4, None, 7], 2, [3, 4, 5, 6, 7]),
            ([1, None, 2], 1, [2]),
            ([2, 1], 2, [1]),
            ([3, 1, 4, None, 2], 3, [1, 2, 4]),
            ([5, 3, 7, 2, 4, 6, 8], 5, [2, 3, 4, 6, 7, 8]),
            ([5, 3, 7, 2, 4, 6, 8], 4, [2, 3, 5, 6, 7, 8]),
            ([5, 3, 7, 2, 4, 6, 8], 6, [2, 3, 4, 5, 7, 8]),
        ],
    )
    def test_delete_node(self, root_list: list[int | None], key: int, expected: list[int]):
        result = run_delete_node(Solution, root_list, key)
        assert_delete_node(result, expected)
