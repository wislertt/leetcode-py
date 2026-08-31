import pytest

from leetcode_py import logged_test

from .helpers import assert_insert, run_insert
from .solution import Solution


class TestInsertIntoASortedCircularLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, insert_val, expected_list",
        [
            ([3, 4, 1], 2, [3, 4, 1, 2]),
            ([], 1, [1]),
            ([1], 0, [1, 0]),
            ([1], 2, [1, 2]),
            ([2, 3, 5], 4, [2, 3, 4, 5]),
            ([1, 3, 5], 0, [1, 3, 5, 0]),
            ([1, 3, 5], 6, [1, 3, 5, 6]),
            ([5, 1, 3], 2, [5, 1, 2, 3]),
            ([2, 2, 2], 2, [2, 2, 2, 2]),
            ([1, 2, 4], 3, [1, 2, 3, 4]),
            ([4, 6, 1, 3], 5, [4, 5, 6, 1, 3]),
            ([10, 20, 30], 15, [10, 15, 20, 30]),
            ([3, 4, 1], 5, [3, 4, 5, 1]),
            ([7, 8, 9, 1], 0, [7, 8, 9, 0, 1]),
            ([6, 1, 2], 6, [6, 6, 1, 2]),
        ],
    )
    def test_insert(self, head_list: list[int], insert_val: int, expected_list: list[int]):
        result = run_insert(Solution, head_list, insert_val)
        assert_insert(result, expected_list)
