import pytest

from leetcode_py import logged_test

from .helpers import assert_array_pair_sum, run_array_pair_sum
from .solution import Solution


class TestArrayPartition:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 4, 3, 2], 4),
            ([6, 2, 6, 5, 1, 2], 9),
            ([1, 2], 1),
            ([2, 1], 1),
            ([1, 1], 1),
            ([-1, -2], -2),
            ([-10000, 10000], -10000),
            ([-10000, -10000], -10000),
            ([1, 2, 3, 4], 4),
            ([4, 3, 2, 1], 4),
            ([7, 3, 1, 0, 5, 9], 10),
            ([0, 0, 0, 0], 0),
            ([-3, -1, -4, -2], -6),
            ([5, 5, 5, 5, 5, 5, 5, 5], 20),
            ([7333, -3560, -4124, 8360, -584, -3472, -3360, -2630, 1443, 7445], -1338),
            ([4480, 8215, -3191, 4213, 6767, -9699, -7557, 7461, -5742, 6141], 2374),
            ([7139, 4637], 4637),
            ([-7577, -3162, -804, -6125], -10739),
            ([-4340, -7424], -7424),
            ([-5919, 7342, 89, 9444, -3904, -7401], -3963),
        ],
    )
    def test_array_pair_sum(self, nums: list[int], expected: int):
        result = run_array_pair_sum(Solution, nums)
        assert_array_pair_sum(result, expected)
