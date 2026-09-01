import pytest

from leetcode_py import logged_test

from .helpers import assert_get_maximum_xor, run_get_maximum_xor
from .solution import Solution


class TestMaximumXorForEachQuery:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, maximum_bit, expected",
        [
            ([0, 1, 1, 3], 2, [0, 3, 2, 3]),
            ([2, 3, 4, 7], 3, [5, 2, 6, 5]),
            ([0, 1, 2, 2, 5, 7], 3, [4, 3, 6, 4, 6, 7]),
            ([0], 1, [1]),
            ([1], 1, [0]),
            ([0, 0, 0], 1, [1, 1, 1]),
            ([1, 1], 2, [3, 2]),
            ([0, 1], 1, [0, 1]),
            ([3, 3, 3, 3], 2, [3, 0, 3, 0]),
            ([1, 2, 3], 2, [3, 0, 2]),
            ([5, 6, 7], 3, [3, 4, 2]),
            ([2, 2, 2, 2, 2], 2, [1, 3, 1, 3, 1]),
            ([4], 3, [3]),
            ([7, 7], 3, [7, 0]),
            ([0, 3], 2, [0, 3]),
            ([1, 1, 2, 2], 2, [3, 1, 3, 2]),
            ([2, 4, 5], 3, [4, 1, 5]),
            ([0, 1, 3, 3, 3, 3], 2, [2, 1, 2, 1, 2, 3]),
            ([0, 1, 5, 1048574, 1048575], 20, [1048570, 5, 1048571, 1048574, 1048575]),
        ],
    )
    def test_get_maximum_xor(self, nums: list[int], maximum_bit: int, expected: list[int]):
        result = run_get_maximum_xor(Solution, nums, maximum_bit)
        assert_get_maximum_xor(result, expected)
