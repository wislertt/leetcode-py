import pytest

from leetcode_py import logged_test

from .helpers import assert_relative_sort_array, run_relative_sort_array
from .solution import Solution


class TestRelativeSortArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr1, arr2, expected",
        [
            (
                [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19],
                [2, 1, 4, 3, 9, 6],
                [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19],
            ),
            ([28, 6, 22, 8, 44, 17], [22, 28, 8, 6], [22, 28, 8, 6, 17, 44]),
            ([1], [1], [1]),
            ([2, 1], [1, 2], [1, 2]),
            ([2, 1], [2, 1], [2, 1]),
            ([1, 1, 1], [1], [1, 1, 1]),
            ([5, 3, 5, 3], [3, 5], [3, 3, 5, 5]),
            ([9, 8, 7, 6], [7], [7, 6, 8, 9]),
            ([4, 2, 6, 1, 3, 5], [2, 4, 6], [2, 4, 6, 1, 3, 5]),
            ([0, 0, 1, 2], [0], [0, 0, 1, 2]),
            ([7, 7, 7, 3, 3], [3, 7], [3, 3, 7, 7, 7]),
            ([10, 20, 30, 40], [30], [30, 10, 20, 40]),
            (
                [2, 21, 43, 38, 0, 42, 33, 7, 24, 13],
                [13, 7, 42, 0],
                [13, 7, 42, 0, 2, 21, 24, 33, 38, 43],
            ),
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [5, 4, 3, 2, 1]),
        ],
    )
    def test_relative_sort_array(self, arr1: list[int], arr2: list[int], expected: list[int]):
        result = run_relative_sort_array(Solution, arr1, arr2)
        assert_relative_sort_array(result, expected)
