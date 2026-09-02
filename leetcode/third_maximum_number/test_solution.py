import pytest

from leetcode_py import logged_test

from .helpers import assert_third_max, run_third_max
from .solution import Solution


class TestThirdMaximumNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 2, 1], 1),
            ([1, 2], 2),
            ([2, 2, 3, 1], 1),
            ([1], 1),
            ([2, 2], 2),
            ([3, 3, 3], 3),
            ([1, 2, 3], 1),
            ([5, 5, 4, 3, 3], 3),
            ([-1, -2, -3], -3),
            ([-2147483648, 2147483647, 0], -2147483648),
            ([2147483647, 2147483647, 2147483646], 2147483647),
            ([1, 1, 2, 2, 3, 3], 1),
            ([10, 9, 8, 7, 6, 5], 8),
            ([0, -1], 0),
            ([2, 18, -6, 19, -3, -2, -16], 2),
            ([14, -12, 2, 4, -12], 2),
            ([11, -10, -20, 18, -1], -1),
            ([-1], -1),
            ([-12, 20, -19, 18, -3, -9, -10, 6], 6),
            ([8, 16, -1, -9, -3, -11, 10], 8),
        ],
    )
    def test_third_max(self, nums: list[int], expected: int):
        result = run_third_max(Solution, nums)
        assert_third_max(result, expected)
