import pytest

from leetcode_py import logged_test

from .helpers import assert_max_product_difference, run_max_product_difference
from .solution import Solution


class TestMaximumProductDifferenceBetweenTwoPairs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([5, 6, 2, 7, 4], 34),
            ([4, 2, 5, 9, 7, 4, 8], 64),
            ([5, 6, 2, 7], 32),
            ([1, 2, 3, 4], 10),
            ([4, 3, 2, 1], 10),
            ([3, 3, 3, 3], 0),
            ([10000, 10000, 1, 1], 99999999),
            ([1, 10000, 1, 10000], 99999999),
            ([7, 7, 7, 7, 7], 0),
            ([10, 3, 5, 6, 20], 185),
            ([2, 9, 4, 8, 1, 6], 70),
            ([8242, 6658, 2567, 2283, 4863, 6042, 8992], 68251603),
            ([2423, 8175, 5259, 5915, 4256, 9275, 2192, 7407], 70511909),
            ([4020, 5531, 4975, 3505, 5224, 4725, 5935, 2034, 9888], 51556110),
            ([4341, 3951, 3297, 7999, 7872, 3543, 8526, 145, 6139, 7900], 67721409),
            ([6265, 7573, 567, 6496, 905, 3201, 6166, 5305, 1867, 286], 49032046),
            ([1617, 4266, 8365, 4662, 1839, 4480, 7659, 5818, 4380, 8067, 7762, 2894], 64506792),
        ],
    )
    def test_max_product_difference(self, nums: list[int], expected: int):
        result = run_max_product_difference(Solution, nums)
        assert_max_product_difference(result, expected)
