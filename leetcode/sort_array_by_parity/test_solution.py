import pytest

from leetcode_py import logged_test

from .helpers import assert_sort_array_by_parity, run_sort_array_by_parity
from .solution import Solution


class TestSortArrayByParity:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 1, 2, 4], [2, 4, 3, 1]),
            ([0], [0]),
            ([1], [1]),
            ([2], [2]),
            ([0, 1], [0, 1]),
            ([1, 0], [0, 1]),
            ([2, 4, 6], [2, 4, 6]),
            ([1, 3, 5], [1, 3, 5]),
            ([0, 2, 1, 4, 3, 5], [0, 2, 4, 1, 3, 5]),
            ([5000, 4999], [5000, 4999]),
            ([0, 0, 1, 1], [0, 0, 1, 1]),
            ([7, 3, 2, 6, 8], [2, 6, 8, 7, 3]),
            ([1, 2], [2, 1]),
            ([4, 2, 5, 7], [4, 2, 5, 7]),
        ],
    )
    def test_sort_array_by_parity(self, nums: list[int], expected: list[int]):
        result = run_sort_array_by_parity(Solution, nums)
        assert_sort_array_by_parity(result, expected)
