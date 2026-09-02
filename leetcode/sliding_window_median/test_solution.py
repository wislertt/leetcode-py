import pytest

from leetcode_py import logged_test

from .helpers import assert_median_sliding_window, run_median_sliding_window
from .solution import Solution


class TestTestSlidingWindowMedian:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 3, -1, -3, 5, 3, 6, 7], 3, [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]),
            ([1, 2, 3, 4, 2, 3, 1, 4, 2], 3, [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]),
            ([1], 1, [1.0]),
            ([2, 1], 2, [1.5]),
            ([5, 2, 2, 7, 3, 7, 9, 0, 2, 3], 4, [3.5, 2.5, 5.0, 7.0, 5.0, 4.5, 2.5]),
            ([-1, -2, -3, -4, -5], 2, [-1.5, -2.5, -3.5, -4.5]),
            ([1, 1, 1, 1, 1], 3, [1.0, 1.0, 1.0]),
            ([2147483647, 2147483647, 2147483647], 2, [2147483647.0, 2147483647.0]),
            ([-2147483648, 2147483647], 2, [-0.5]),
            ([3, 1, 2], 3, [2.0]),
            ([1, 2, 3, 4], 1, [1.0, 2.0, 3.0, 4.0]),
            ([1, 4, 2, 3], 2, [2.5, 3.0, 2.5]),
            ([-5, 8, -1, 0, 3, -7, 6], 5, [0.0, 0.0, 0.0]),
            ([4, 0, -4, 3, 1, -2, 5, 2], 6, [0.5, 0.5, 1.5]),
            ([0, 7, 5, -3, 0], 5, [0.0]),
            ([-2, -6], 1, [-2.0, -6.0]),
        ],
    )
    def test_median_sliding_window(self, nums: list[int], k: int, expected: list[float]):
        result = run_median_sliding_window(Solution, nums, k)
        assert_median_sliding_window(result, expected)
