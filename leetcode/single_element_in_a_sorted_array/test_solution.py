import pytest

from leetcode_py import logged_test

from .helpers import assert_single_non_duplicate, run_single_non_duplicate
from .solution import Solution


class TestSingleElementInASortedArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 1, 2, 3, 3, 4, 4, 8, 8], 2),
            ([3, 3, 7, 7, 10, 11, 11], 10),
            ([1], 1),
            ([0, 0, 1], 1),
            ([1, 0, 0], 1),
            ([1, 1, 2], 2),
            ([2, 1, 1], 2),
            ([1, 1, 5, 5, 9], 9),
            ([9, 1, 1, 5, 5], 9),
            ([1, 1, 3, 3, 5, 5, 7], 7),
            ([7, 5, 5, 3, 3, 1, 1], 7),
            ([0, 0, 2, 2, 4, 4, 6, 6, 8], 8),
            ([1, 2, 2, 3, 3], 1),
            ([10, 10, 20, 30, 30], 20),
            ([100000, 100000, 100001], 100001),
        ],
    )
    def test_single_non_duplicate(self, nums: list[int], expected: int):
        result = run_single_non_duplicate(Solution, nums)
        assert_single_non_duplicate(result, expected)
