import pytest

from leetcode_py import logged_test

from .helpers import assert_three_sum_closest, run_three_sum_closest
from .solution import Solution


class TestThreeSumClosest:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([-1, 2, 1, -4], 1, 2),
            ([0, 0, 0], 1, 0),
            ([1, 1, -1, -1, 3], -1, -1),
            ([1, 2, 3, 4, 5], 9, 9),
            ([0, 1, 2], 0, 3),
            ([0, 1, 2], 3, 3),
            ([-4, -2, -1, 0, 3, 5], 1, 1),
            ([1, 2, 5, 10, 11], 12, 13),
            ([2, 3, 4, 5], 50, 12),
            ([1, 1, 1], 3, 3),
            ([100, 200, 300, 400], 200, 600),
            ([-5, -4, -3, -2, -1], -12, -12),
            ([5, 5, 5, 5], 10, 15),
            ([1, 2, 4, 8, 16], 10, 11),
            ([1, 2, 3], 1, 6),
            ([-1, 0, 1, 2, -1, -4], 0, 0),
        ],
    )
    def test_three_sum_closest(self, nums: list[int], target: int, expected: int):
        result = run_three_sum_closest(Solution, nums, target)
        assert_three_sum_closest(result, expected)
