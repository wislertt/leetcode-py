import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_operations, run_minimum_operations
from .solution import Solution


class TestMinimumOperationsToSortBinaryTreeByLevel:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root_list, expected",
        [
            ([1, 4, 3, 7, 6, 8, 5, None, None, None, None, 9, None, 10], 3),
            ([1, 3, 2, 7, 6, 5, 4], 3),
            ([1, 2, 3, 4, 5, 6], 0),
            ([1], 0),
            ([2, 1], 0),
            ([1, 2], 0),
            ([3, 1, 2], 0),
            ([1, 3, 2, 4], 1),
            ([4, 1, 6, 3, 2, 5], 1),
            ([1, 2, 3, 4, 6, 5, 7], 1),
            ([5, 3, 8, 1, 4, 7, 9, 2, 6], 0),
            ([10, 5, 15, 3, 8, 12, 20, 1, 4, 6, 9, 11, 14, 19, 21], 0),
            ([92, 17, 55, None, 28, 31, None, 39, 56, 65], 0),
            ([42, 92, 68], 1),
            ([58, 52, 8, 5, 2, 42, 60, 30, None, 57, 48], 3),
            ([96, 49, None, 10, 93, 30, 56, 88, None, 34], 0),
            ([60, 77, 35, 34, 87, None, 70], 2),
            ([5, 88, 21, 65, 96], 1),
            ([34, None, 25, 37, 23, None, 29, 9, 33, 11, 74, 10, 81], 4),
            ([69, 61, 84, 97, None, 26, 31, 4], 2),
        ],
    )
    def test_minimum_operations(self, root_list: list[int | None], expected: int):
        result = run_minimum_operations(Solution, root_list)
        assert_minimum_operations(result, expected)
