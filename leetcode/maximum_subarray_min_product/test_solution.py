import pytest

from leetcode_py import logged_test

from .helpers import assert_max_sum_min_product, run_max_sum_min_product
from .solution import Solution


class TestMaximumSubarrayMinProduct:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 2], 14),
            ([2, 3, 3, 1, 2], 18),
            ([3, 1, 5, 6, 4, 2], 60),
            ([1], 1),
            ([5], 25),
            ([7, 7, 7, 7], 196),
            ([1, 2], 4),
            ([2, 1], 4),
            ([1, 1, 1, 1, 1], 5),
            ([2, 3, 4], 21),
            ([4, 3, 2], 21),
            ([5, 4, 3, 2, 1], 36),
            ([3, 1, 4, 1, 5, 9, 2, 6], 81),
            ([999999, 1000000, 999998, 1000001, 999997, 1000002], 978958016),
            ([2, 9999999, 3, 9999999, 2], 979300008),
            ([1000000, 999999, 1000001, 999998, 1000002], 989965007),
            ([8, 5, 4, 4, 7, 7, 7], 168),
            ([6, 1, 8, 2, 5, 9, 5], 95),
            ([2, 7, 3, 9, 8, 7, 2], 168),
            ([6, 9], 90),
            ([556086, 249542, 66857], 231637233),
            ([286551, 98795, 931218], 166957455),
        ],
    )
    def test_max_sum_min_product(self, nums: list[int], expected: int):
        result = run_max_sum_min_product(Solution, nums)
        assert_max_sum_min_product(result, expected)
