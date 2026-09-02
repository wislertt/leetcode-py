import pytest

from leetcode_py import logged_test

from .helpers import assert_find_least_num_of_unique_ints, run_find_least_num_of_unique_ints
from .solution import Solution


class TestLeastNumberOfUniqueIntegersAfterKRemovals:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, k, expected",
        [
            ([5, 5, 4], 1, 1),
            ([4, 3, 1, 1, 3, 3, 2], 3, 2),
            ([2, 2, 2], 2, 1),
            ([1], 0, 1),
            ([1], 1, 0),
            ([1, 2], 1, 1),
            ([1, 2, 3, 4, 5], 5, 0),
            ([1, 1, 2, 2, 3, 3], 3, 2),
            ([9, 9, 9, 9, 1], 1, 1),
            ([1000000000, 1, 1000000000], 2, 1),
            ([7, 7, 7, 8, 8, 9, 9, 9], 4, 2),
            ([3, 1, 2, 3, 2, 1], 2, 2),
            ([4], 0, 1),
            ([1, 3, 2, 1, 3], 4, 1),
            ([5], 1, 0),
            ([5, 3, 4, 3], 0, 3),
            ([1, 2, 2, 4, 4, 3, 1, 2, 3], 2, 3),
            ([1, 6, 1, 5, 5, 2, 6], 5, 1),
        ],
    )
    def test_find_least_num_of_unique_ints(self, arr: list[int], k: int, expected: int):
        result = run_find_least_num_of_unique_ints(Solution, arr, k)
        assert_find_least_num_of_unique_ints(result, expected)
