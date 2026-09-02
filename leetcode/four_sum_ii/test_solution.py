import pytest

from leetcode_py import logged_test

from .helpers import assert_four_sum_count, run_four_sum_count
from .solution import Solution


class TestTest4SumII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, nums3, nums4, expected",
        [
            ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
            ([0], [0], [0], [0], 1),
            ([1], [2], [3], [4], 0),
            ([0, 0], [0, 0], [0, 0], [0, 0], 16),
            ([1, 1], [-1, -1], [0, 0], [0, 0], 16),
            ([268435456], [-268435456], [0], [0], 1),
            ([268435456, -268435456], [268435456, -268435456], [1, -1], [-1, 1], 4),
            ([1, 2, 3], [-1, -2, -3], [10, 20, 30], [-10, -20, -30], 9),
            ([-1, -1], [-1, -1], [-1, -1], [-1, -1], 0),
            ([1, -1], [1, -1], [1, -1], [1, -1], 6),
            ([1, 2, 0], [2, 1, 1], [0, 1, 2], [0, 2, 1], 0),
            ([-1, -1, 2], [-1, -1, 3], [1, -1, -1], [2, 3, -1], 12),
            ([0, 2, 1, 0], [1, 0, 1, 0], [-1, 1, 0, 1], [-1, -1, 0, 2], 46),
            ([0], [0], [0], [1], 0),
            ([2], [-1], [3], [2], 0),
            ([-1, -1, 2], [-1, -1, -1], [2, -1, 1], [1, 0, 1], 21),
        ],
    )
    def test_four_sum_count(
        self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int], expected: int
    ):
        result = run_four_sum_count(Solution, nums1, nums2, nums3, nums4)
        assert_four_sum_count(result, expected)
