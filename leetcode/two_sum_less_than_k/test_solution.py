import pytest

from leetcode_py import logged_test

from .helpers import assert_two_sum_less_than_k, run_two_sum_less_than_k
from .solution import Solution


class TestTwoSumLessThanK:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([34, 23, 1, 24, 75, 33, 54, 8], 60, 58),
            ([10, 20, 30], 15, -1),
            ([10, 20, 30], 100, 50),
            ([1, 2], 4, 3),
            ([1, 2], 3, -1),
            ([5], 100, -1),
            ([1, 1, 1, 1], 3, 2),
            ([100, 200, 300], 1000, 500),
            ([25, 33, 42, 60, 89], 90, 85),
            ([34, 23], 60, 57),
            ([57, 44, 92, 28, 66, 13], 100, 94),
            ([9, 8, 7, 6, 5], 12, 11),
        ],
    )
    def test_two_sum_less_than_k(self, nums: list[int], k: int, expected: int):
        result = run_two_sum_less_than_k(Solution, nums, k)
        assert_two_sum_less_than_k(result, expected)
