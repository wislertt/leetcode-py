import pytest

from leetcode_py import logged_test

from .helpers import assert_min_k_bit_flips, run_min_k_bit_flips
from .solution import Solution


class TestMinimumNumberOfKConsecutiveBitFlips:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([0, 1, 0], 1, 2),
            ([1, 1, 0], 2, -1),
            ([0, 0, 0, 1, 0, 1, 1, 0], 3, 3),
            ([0], 1, 1),
            ([1], 1, 0),
            ([0, 0], 2, 1),
            ([1, 0, 1], 2, -1),
            ([1, 1, 1, 1], 2, 0),
            ([0, 1, 0, 1], 2, 2),
            ([0, 0, 0], 3, 1),
            ([1, 0, 0, 1, 0, 1], 3, -1),
            ([0, 0, 1, 0, 0, 1, 0], 3, -1),
            ([1, 1, 0, 0, 1, 1, 0, 0], 4, 2),
            ([0, 1, 0], 3, -1),
        ],
    )
    def test_min_k_bit_flips(self, nums: list[int], k: int, expected: int):
        result = run_min_k_bit_flips(Solution, nums, k)
        assert_min_k_bit_flips(result, expected)
