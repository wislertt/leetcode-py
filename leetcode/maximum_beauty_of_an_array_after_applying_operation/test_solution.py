import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_beauty, run_maximum_beauty
from .solution import Solution


class TestMaximumBeautyOfAnArrayAfterApplyingOperation:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([4, 6, 1, 2], 2, 3),
            ([1, 1, 1, 1], 10, 4),
            ([1], 0, 1),
            ([5], 100000, 1),
            ([0, 0], 0, 2),
            ([1, 2], 0, 1),
            ([1, 3], 1, 2),
            ([1, 4], 1, 1),
            ([2, 4, 6, 8], 1, 2),
            ([2, 4, 6, 8], 2, 3),
            ([10, 1, 10, 1], 0, 2),
            ([3, 1, 2], 1, 3),
            ([0, 100000], 50000, 2),
            ([0, 100000], 49999, 1),
            ([100000, 0], 100000, 2),
            ([7, 7, 7], 0, 3),
            ([6, 15, 13, 9, 1, 14, 12], 4, 5),
            ([20, 8, 10], 2, 2),
        ],
    )
    def test_maximum_beauty(self, nums: list[int], k: int, expected: int):
        result = run_maximum_beauty(Solution, nums, k)
        assert_maximum_beauty(result, expected)
