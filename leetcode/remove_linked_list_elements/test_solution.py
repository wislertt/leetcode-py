import pytest

from leetcode_py import logged_test

from .helpers import assert_remove_linked_list_elements, run_remove_linked_list_elements
from .solution import Solution


class TestRemoveLinkedListElements:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_vals, val, expected_vals",
        [
            ([1, 2, 6, 3, 4, 5, 6], 6, [1, 2, 3, 4, 5]),
            ([], 1, []),
            ([7, 7, 7, 7], 7, []),
            ([1], 1, []),
            ([1], 2, [1]),
            ([1, 2], 1, [2]),
            ([1, 2], 2, [1]),
            ([1, 2, 3], 2, [1, 3]),
            ([1, 1, 2, 1, 3, 1], 1, [2, 3]),
            ([1, 2, 3, 4, 5], 6, [1, 2, 3, 4, 5]),
            ([50, 50, 49], 50, [49]),
            ([1, 2, 2, 2, 3, 3, 4], 2, [1, 3, 3, 4]),
            ([1, 2, 2, 2, 3, 3, 4], 3, [1, 2, 2, 2, 4]),
            ([5], 5, []),
            ([2, 1, 2, 1, 2], 2, [1, 1]),
            ([1, 2, 3, 1, 2, 3], 1, [2, 3, 2, 3]),
        ],
    )
    def test_remove_linked_list_elements(
        self, head_vals: list[int], val: int, expected_vals: list[int]
    ):
        result = run_remove_linked_list_elements(Solution, head_vals, val)
        assert_remove_linked_list_elements(result, expected_vals)
