import pytest

from leetcode_py import logged_test

from .helpers import assert_modified_list, run_modified_list
from .solution import Solution


class TestDeleteNodesFromLinkedListPresentInArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, head_vals, expected_vals",
        [
            ([1, 2, 3], [1, 2, 3, 4, 5], [4, 5]),
            ([1], [1, 2, 1, 2, 1, 2], [2, 2, 2]),
            ([5], [1, 2, 3, 4], [1, 2, 3, 4]),
            ([2], [1], [1]),
            ([1], [1, 2, 3, 1], [2, 3]),
            ([3, 1], [1, 2, 3, 4], [2, 4]),
            ([2, 3], [2, 2, 3, 2, 5], [5]),
            ([1, 2], [6, 1, 1, 5, 1], [6, 5]),
            ([3, 5, 1, 2], [3, 6, 5], [6]),
            ([3, 4, 7], [3, 2, 4, 5, 1], [2, 5, 1]),
            ([6, 3, 7], [5, 8, 8], [5, 8, 8]),
            ([6, 4, 3], [8, 6, 7], [8, 7]),
            ([1, 3, 6, 2], [6, 8, 4, 3], [8, 4]),
            ([7], [2, 3, 7, 2], [2, 3, 2]),
            ([3], [6, 2, 8, 6], [6, 2, 8, 6]),
            ([7, 3, 2], [5, 5, 4, 4], [5, 5, 4, 4]),
        ],
    )
    def test_modified_list(self, nums: list[int], head_vals: list[int], expected_vals: list[int]):
        result = run_modified_list(Solution, nums, head_vals)
        assert_modified_list(result, expected_vals)
