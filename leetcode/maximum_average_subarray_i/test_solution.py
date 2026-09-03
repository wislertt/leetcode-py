import pytest

from leetcode_py import logged_test

from .helpers import assert_find_max_average, run_find_max_average
from .solution import Solution


class TestMaximumAverageSubarrayI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 12, -5, -6, 50, 3], 4, 12.75),
            ([5], 1, 5.0),
            ([1, 2, 3], 2, 2.5),
            ([4, 2, 1, 7], 2, 4.0),
            ([0, 0, 0], 1, 0.0),
            ([-1, -2, -3], 2, -1.5),
            ([1, 12, -5, -6, 50, 3], 1, 50.0),
            ([10, 10, 10], 3, 10.0),
            ([7, 4, 5, 8, 8, 3, 2], 3, 7.0),
            ([1, 2], 2, 1.5),
            ([-6, -7, -8, -9], 1, -6.0),
            ([3, 1, 4, 1, 5], 4, 2.75),
            ([100, -100, 100, -100, 100], 2, 0.0),
            ([2, 2, 2, 2, 9], 5, 3.4),
            ([9, -1, -5, -4, -11, 10, -6, -6, -8, 6], 4, -0.25),
            ([2, 6, 0, 6, -4, -8, -1, -3, 1], 1, 6.0),
            ([10, -4, 8, 1, 4, -9, 4], 1, 10.0),
            ([2, -5, 2, -3, -8, -6, 1], 2, -0.5),
        ],
    )
    def test_find_max_average(self, nums: list[int], k: int, expected: float):
        result = run_find_max_average(Solution, nums, k)
        assert_find_max_average(result, expected)
