import pytest

from leetcode_py import logged_test

from .helpers import assert_delete_duplicates, run_delete_duplicates
from .solution import Solution


class TestRemoveDuplicatesFromSortedListII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_list, expected_list",
        [
            ([1, 2, 3, 3, 4, 4, 5], [1, 2, 5]),
            ([1, 1, 1, 2, 3], [2, 3]),
            ([], []),
            ([1], [1]),
            ([1, 1], []),
            ([1, 1, 1, 1, 1], []),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([-100, -100, -99, 0, 0, 100], [-99, 100]),
            ([0, 0], []),
            ([-1, -1, -1], []),
            ([1, 1, 2, 2, 3, 3], []),
            ([1, 2, 2, 3, 3, 3, 4], [1, 4]),
            ([-100, -100], []),
            ([-3, -2, -1, 0, 1, 2, 3], [-3, -2, -1, 0, 1, 2, 3]),
            ([1, 1, 1, 2, 3, 3, 3, 4, 5, 5], [2, 4]),
            ([7], [7]),
            ([1, 1, 2, 3, 3, 4, 4, 5], [2, 5]),
            ([3, 4], [3, 4]),
            ([-2, -2, -2, 0], [0]),
            ([-4, -3, -3, -3, -2, -1, 0, 1, 2, 3, 3, 4], [-4, -2, -1, 0, 1, 2, 4]),
            ([-6, -5, -3, 1, 2, 2, 3, 5, 5, 6], [-6, -5, -3, 1, 3, 6]),
            (
                [-6, -6, -5, -5, -4, -3, -2, -1, 0, 0, 1, 2, 2, 3, 5, 6],
                [-4, -3, -2, -1, 1, 3, 5, 6],
            ),
            ([-5, -5, -3, 1, 3, 3, 5, 5, 6, 6], [-3, 1]),
        ],
    )
    def test_delete_duplicates(self, head_list: list[int], expected_list: list[int]):
        result = run_delete_duplicates(Solution, head_list)
        assert_delete_duplicates(result, expected_list)
