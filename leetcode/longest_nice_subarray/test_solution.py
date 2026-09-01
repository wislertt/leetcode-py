import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_nice_subarray, run_longest_nice_subarray
from .solution import Solution


class TestLongestNiceSubarray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 3, 8, 48, 10], 3),
            ([3, 1, 5, 11, 13], 1),
            ([1], 1),
            ([1, 2, 4, 8], 4),
            ([1, 1, 1, 1], 1),
            ([5, 5], 1),
            ([3, 4], 2),
            ([1, 2, 1, 2], 2),
            ([1, 2, 4, 1, 2, 4, 8], 4),
            ([999999999, 1, 2, 999999999], 2),
            ([1048576, 2097152, 1], 3),
            ([536870912, 536870912], 1),
            ([2, 3, 5, 7, 11, 13], 1),
            ([7, 8, 9, 10, 11], 2),
            ([1, 2, 4, 8, 16], 5),
            ([16, 8, 4, 2, 1, 3], 5),
            ([1000000000, 512, 256, 128, 64], 4),
            ([2003, 1791, 1521, 1821, 417, 442], 1),
            ([853, 1495, 1484, 1719, 1952, 869, 1003, 1710, 596, 1837, 1729, 590], 1),
            ([1641, 832, 244, 1665, 289, 467, 537], 1),
        ],
    )
    def test_longest_nice_subarray(self, nums: list[int], expected: int):
        result = run_longest_nice_subarray(Solution, nums)
        assert_longest_nice_subarray(result, expected)
