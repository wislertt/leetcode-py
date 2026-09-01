import pytest

from leetcode_py import logged_test

from .helpers import assert_find_length_of_shortest_subarray, run_find_length_of_shortest_subarray
from .solution import Solution


class TestShortestSubarrayToBeRemovedToMakeArraySorted:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([1, 2, 3, 10, 4, 2, 3, 5], 3),
            ([5, 4, 3, 2, 1], 4),
            ([1, 2, 3], 0),
            ([11, 10, 18, 14, 12, 11, 16, 20, 13, 11], 8),
            ([17, 32, 32, 29, 4, 29, 19, 5, 26, 35, 35, 6, 10, 27, 11, 35, 0, 31], 15),
            ([1, 8, 34, 2, 3, 22, 18, 27, 3, 1, 0, 12, 21, 23, 8, 7, 17], 14),
            ([1], 0),
            ([1, 1, 1, 1], 0),
            ([1, 2, 3, 3, 4, 5], 0),
            ([2, 1], 1),
            ([1, 3, 2, 4], 1),
            ([1, 2, 5, 3, 4, 6], 1),
            ([4, 5, 1, 2, 3], 2),
            ([1, 2, 3, 4, 0], 1),
            ([9, 1, 2, 3, 4], 1),
            ([0, 1000000000, 0, 1000000000], 1),
            ([1000000000, 999999999, 1000000000], 1),
            ([3, 3, 1, 2, 2, 3], 2),
            ([4, 7, 6, 15, 13, 12, 16, 19], 3),
            ([8, 17, 10, 8, 2, 4], 4),
            ([15, 7, 18], 1),
            ([15, 3, 19, 7], 3),
        ],
    )
    def test_find_length_of_shortest_subarray(self, arr: list[int], expected: int):
        result = run_find_length_of_shortest_subarray(Solution, arr)
        assert_find_length_of_shortest_subarray(result, expected)
