import pytest

from leetcode_py import logged_test

from .helpers import assert_sort_array_by_parity_ii, run_sort_array_by_parity_ii
from .solution import Solution


class TestSortArrayByParityII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 2, 5, 7], [4, 5, 2, 7]),
            ([2, 3], [2, 3]),
            ([1, 2], [2, 1]),
            ([0, 1], [0, 1]),
            ([1, 0], [0, 1]),
            ([2, 3], [2, 3]),
            ([6, 7], [6, 7]),
            ([9, 4], [4, 9]),
            ([0, 5], [0, 5]),
            ([1000, 999], [1000, 999]),
            ([0, 999], [0, 999]),
            ([999, 1000], [1000, 999]),
            ([2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7]),
            ([4, 2, 5, 7, 8, 9, 10, 3], [4, 5, 2, 7, 8, 9, 10, 3]),
            ([2, 3, 2, 3], [2, 3, 2, 3]),
            ([0, 1, 2, 3, 4, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]),
            ([5, 4, 3, 2, 1, 0], [4, 5, 2, 3, 0, 1]),
            ([1000, 1000, 999, 999], [1000, 999, 1000, 999]),
            ([0, 3, 2, 1, 6, 7, 4, 5], [0, 3, 2, 1, 6, 7, 4, 5]),
            ([2, 1, 4, 3, 6, 5, 8, 7, 10, 9], [2, 1, 4, 3, 6, 5, 8, 7, 10, 9]),
        ],
    )
    def test_sort_array_by_parity_ii(self, nums: list[int], expected: list[int]):
        result = run_sort_array_by_parity_ii(Solution, nums)
        assert_sort_array_by_parity_ii(result, expected)
