import pytest

from leetcode_py import logged_test

from .helpers import assert_split_array, run_split_array
from .solution import Solution


class TestSplitArrayLargestSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([7, 2, 5, 10, 8], 2, 18),
            ([1, 2, 3, 4, 5], 2, 9),
            ([1, 4, 4], 3, 4),
            ([7, 2, 5, 10, 8], 1, 32),
            ([7, 2, 5, 10, 8], 5, 10),
            ([1], 1, 1),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 17),
            ([0, 0, 0], 2, 0),
            ([10], 1, 10),
            ([5, 5, 5, 5], 2, 10),
            ([1, 1, 1, 1, 1], 3, 2),
            ([100, 1, 1, 1, 100], 2, 102),
            ([7, 2, 5, 10, 8], 3, 14),
            ([2, 3, 1, 2, 4, 3], 5, 4),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2, 24),
        ],
    )
    def test_split_array(self, nums: list[int], k: int, expected: int):
        result = run_split_array(Solution, nums, k)
        assert_split_array(result, expected)
