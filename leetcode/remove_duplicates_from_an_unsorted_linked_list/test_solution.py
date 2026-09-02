import pytest

from leetcode_py import logged_test

from .helpers import assert_delete_duplicates_unsorted, run_delete_duplicates_unsorted
from .solution import Solution


class TestRemoveDuplicatesFromAnUnsortedLinkedList:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "head_vals, expected_vals",
        [
            ([1, 2, 3, 2], [1, 3]),
            ([2, 1, 1, 2], []),
            ([3, 2, 2, 1, 3, 2, 4], [1, 4]),
            ([1], [1]),
            ([1, 1], []),
            ([1, 2], [1, 2]),
            ([5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
            ([7, 7, 7, 7], []),
            ([1, 2, 3, 1, 2, 3], []),
            ([1, 1, 2], [2]),
            ([2, 2, 1], [1]),
            ([9, 8, 9, 8, 7], [7]),
            ([4, 5, 4, 5, 6, 7, 6], [7]),
            ([10, 20, 10, 30, 20, 40], [30, 40]),
            ([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], []),
            ([100000], [100000]),
            ([100000, 1, 100000], [1]),
            ([3, 3, 3, 1, 2, 2, 4, 5, 5], [1, 4]),
            ([3, 6, 8, 1], [3, 6, 8, 1]),
            ([4, 7, 7, 5, 7, 8, 3], [4, 5, 8, 3]),
            ([6], [6]),
            ([1, 3, 2], [1, 3, 2]),
            ([7, 8], [7, 8]),
            ([3, 8, 1, 4, 2, 2, 4, 8], [3, 1]),
        ],
    )
    def test_delete_duplicates_unsorted(self, head_vals: list[int], expected_vals: list[int]):
        result = run_delete_duplicates_unsorted(Solution, head_vals)
        assert_delete_duplicates_unsorted(result, expected_vals)
