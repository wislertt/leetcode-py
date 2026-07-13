import pytest

from leetcode_py import logged_test

from .helpers import assert_sort_array, run_sort_array
from .solution import Solution


class TestSortAnArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([5, 2, 3, 1], [1, 2, 3, 5]),
            ([5, 1, 1, 2, 0, 0], [0, 0, 1, 1, 2, 5]),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([1, 2], [1, 2]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([3, 3, 3, 3], [3, 3, 3, 3]),
            ([-1, -3, -2, 0, 2, 1], [-3, -2, -1, 0, 1, 2]),
            ([0, 0, 0], [0, 0, 0]),
            ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
            ([100, -100, 50, -50, 0], [-100, -50, 0, 50, 100]),
            ([1, 2, 1, 2, 1, 2], [1, 1, 1, 2, 2, 2]),
            ([42], [42]),
            ([-5, -10, 0, 5, 10], [-10, -5, 0, 5, 10]),
            (
                [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3],
                [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
            ),
            ([1, 5, 2, 5, 3, 5, 4], [1, 2, 3, 4, 5, 5, 5]),
            ([500, -500, 250, -250, 0, 0, 125], [-500, -250, 0, 0, 125, 250, 500]),
        ],
    )
    def test_sort_array(self, nums: list[int], expected: list[int]):
        result = run_sort_array(Solution, nums)
        assert_sort_array(result, expected)
