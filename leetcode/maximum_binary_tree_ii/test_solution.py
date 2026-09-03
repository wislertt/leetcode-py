import pytest

from leetcode_py import logged_test

from .helpers import assert_insert_into_max_tree, run_insert_into_max_tree
from .solution import Solution


class TestMaximumBinaryTreeII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, val, expected_list",
        [
            ([4, 1, 3, None, None, 2], 5, [5, 4, None, 1, 3, None, None, 2]),
            ([5, 2, 4, None, 1], 3, [5, 2, 4, None, 1, None, 3]),
            ([5, 2, 3, None, 1], 4, [5, 2, 4, None, 1, 3]),
            ([5], 6, [6, 5]),
            ([5], 4, [5, None, 4]),
            ([5, 4, None, 3, None, 2, None, 1], 6, [6, 5, None, 4, None, 3, None, 2, None, 1]),
            ([3, None, 2, 1], 100, [100, 3, None, None, 2, 1]),
            ([5, None, 4], 6, [6, 5, None, None, 4]),
            ([7, None, 5, 4, 1], 3, [7, None, 5, 4, 3, None, None, 1]),
            ([100, None, 1], 99, [100, None, 99, 1]),
            ([100, 1], 99, [100, 1, 99]),
            ([75, 50, 60, None, 25, 10], 55, [75, 50, 60, None, 25, 10, 55]),
            ([77, 62], 70, [77, 62, 70]),
            ([93, 72, None, 25, None, 24], 89, [93, 72, 89, 25, None, None, None, 24]),
            ([100, None, 92, 87, None, 23], 4, [100, None, 92, 87, 4, 23]),
            ([99, 98, 33, 46, 36], 85, [99, 98, 85, 46, 36, 33]),
        ],
    )
    def test_insert_into_max_tree(
        self, root_list: list[int | None], val: int, expected_list: list[int | None]
    ):
        result = run_insert_into_max_tree(Solution, root_list, val)
        assert_insert_into_max_tree(result, expected_list)
