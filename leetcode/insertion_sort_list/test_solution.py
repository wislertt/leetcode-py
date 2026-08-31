import pytest

from leetcode_py import logged_test

from .helpers import assert_insertion_sort_list, run_insertion_sort_list
from .solution import Solution


class TestInsertionSortList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_vals, expected_vals",
        [
            ([4, 2, 1, 3], [1, 2, 3, 4]),
            ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
            ([1], [1]),
            ([5], [5]),
            ([1, 2], [1, 2]),
            ([2, 1], [1, 2]),
            ([1, 2, 3], [1, 2, 3]),
            ([3, 2, 1], [1, 2, 3]),
            ([1, 1, 1], [1, 1, 1]),
            ([2, 1, 2], [1, 2, 2]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([1, 2, 4, 3, 5], [1, 2, 3, 4, 5]),
            ([0, -1], [-1, 0]),
            ([-5000, 5000, 0], [-5000, 0, 5000]),
            ([3, 1, 2, 3, 1], [1, 1, 2, 3, 3]),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ],
    )
    def test_insertion_sort_list(self, head_vals: list[int], expected_vals: list[int]):
        result = run_insertion_sort_list(Solution, head_vals)
        assert_insertion_sort_list(result, expected_vals)
