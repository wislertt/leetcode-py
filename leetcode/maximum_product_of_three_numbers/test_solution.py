import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_product, run_maximum_product
from .solution import Solution


class TestMaximumProductOfThreeNumbers:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3], 6),
            ([1, 2, 3, 4], 24),
            ([-1, -2, -3], -6),
            ([-1, -2, -3, -4], -6),
            ([-1000, -1000, 1000], 1000000000),
            ([-1000, -1000, -1000], -1000000000),
            ([-1000, 0, 1000, 500], 0),
            ([-5, -4, -3, -2, -1], -6),
            ([0, 0, 0], 0),
            ([-1, 0, 1], 0),
            ([1, 1, 1, 1], 1),
            ([-10, -10, 1, 3, 2], 300),
            ([7, 3, 1, 0, -5, 12], 252),
            ([-1000, 1000, 0, -999, 2], 999000000),
            ([-8, 7, 7, -7, 4, -6], 392),
            ([7, 10, 4, 5], 350),
        ],
    )
    def test_maximum_product(self, nums: list[int], expected: int):
        result = run_maximum_product(Solution, nums)
        assert_maximum_product(result, expected)
