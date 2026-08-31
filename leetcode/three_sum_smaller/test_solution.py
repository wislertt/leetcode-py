import pytest

from leetcode_py import logged_test

from .helpers import assert_three_sum_smaller, run_three_sum_smaller
from .solution import Solution


class TestThreeSumSmaller:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([-2, 0, 1, 3], 2, 2),
            ([], 0, 0),
            ([0], 0, 0),
            ([1, 1, 1], 3, 0),
            ([0, 0, 0], 0, 0),
            ([-1, -1, -1], 0, 1),
            ([1, 2, 3], 6, 0),
            ([1, 2, 3], 7, 1),
            ([1, 1, 1, 1], 4, 4),
            ([-5, -4, -3, -2, -1], 0, 10),
            ([3, 1, -2, 0], 2, 2),
            ([100, -100, 50, -50, 25], 25, 4),
            ([-2, 0, 1, 3], 100, 4),
            ([-2, 0, 1, 3], -2, 0),
        ],
    )
    def test_three_sum_smaller(self, nums: list[int], target: int, expected: int):
        result = run_three_sum_smaller(Solution, nums, target)
        assert_three_sum_smaller(result, expected)
