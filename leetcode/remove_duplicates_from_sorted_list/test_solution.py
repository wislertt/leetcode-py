import pytest

from leetcode_py import logged_test

from .helpers import assert_delete_duplicates, run_delete_duplicates
from .solution import Solution


class TestRemoveDuplicatesFromSortedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, expected_list",
        [
            ([1, 1, 2], [1, 2]),
            ([1, 1, 2, 3, 3], [1, 2, 3]),
            ([], []),
            ([1], [1]),
            ([1, 1], [1]),
            ([1, 1, 1, 1, 1], [1]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([-100, -100, -99, 0, 0, 100], [-100, -99, 0, 100]),
            ([0, 0], [0]),
            ([-1, -1, -1], [-1]),
            ([1, 1, 2, 2, 3, 3], [1, 2, 3]),
            ([1, 2, 2, 3, 3, 3, 4], [1, 2, 3, 4]),
            ([5, 5, 5, 5, 5, 5, 5, 5], [5]),
            ([-3, -2, -1, 0, 1, 2, 3], [-3, -2, -1, 0, 1, 2, 3]),
            ([1, 1, 1, 2, 3, 3, 3, 4, 5, 5], [1, 2, 3, 4, 5]),
        ],
    )
    def test_delete_duplicates(self, head_list: list[int], expected_list: list[int]):
        result = run_delete_duplicates(Solution, head_list)
        assert_delete_duplicates(result, expected_list)
