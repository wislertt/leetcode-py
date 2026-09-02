import pytest

from leetcode_py import logged_test

from .helpers import assert_find_max_average, run_find_max_average
from .solution import Solution


class TestMaximumAverageSubarrayII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1, 12, -5, -6, 50, 3], 4, 12.75),
            ([5], 1, 5),
            ([1, 2, 3], 2, 2.5),
            ([4, 2, 1, 7], 2, 4),
            ([0, 0, 0], 1, 0),
            ([-1, -2, -3], 2, -1.5),
            ([1, 12, -5, -6, 50, 3], 1, 50),
            ([10, 10, 10], 3, 10),
            ([7, 4, 5, 8, 8, 3, 2], 3, 7),
            ([1, 2], 2, 1.5),
            ([-6, -7, -8, -9], 1, -6),
            ([3, 1, 4, 1, 5], 4, 2.8),
            ([100, -100, 100, -100, 100], 2, 33.33333),
            ([2, 2, 2, 2, 9], 5, 3.4),
            ([9, -1, -5, -4, -11, 10, -6, -6, -8, 6], 4, -0.25),
        ],
    )
    def test_find_max_average(self, nums: list[int], k: int, expected: float):
        result = run_find_max_average(Solution, nums, k)
        assert_find_max_average(result, expected)
