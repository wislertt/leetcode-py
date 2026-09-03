import pytest

from leetcode_py import logged_test

from .helpers import assert_smallest_range_ii, run_smallest_range_ii
from .solution import Solution


class TestSmallestRangeII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([1], 0, 0),
            ([0, 10], 2, 6),
            ([1, 3, 6], 3, 3),
            ([0], 0, 0),
            ([1], 10000, 0),
            ([0, 10], 5, 0),
            ([0, 10000], 10000, 10000),
            ([0, 10000], 9999, 9998),
            ([2, 7, 2], 1, 3),
            ([1, 5, 9], 2, 4),
            ([3, 1, 10], 4, 2),
            ([10, 0, 5, 5], 0, 10),
            ([5, 5, 5, 5], 7, 0),
            ([9, 1, 4, 4, 7], 3, 3),
            ([0, 6, 2, 12, 0, 4], 6, 6),
            ([5, 11, 10, 7, 4, 10], 1, 5),
            ([1, 2, 3, 4, 5, 6, 7, 8], 4, 7),
            ([7, 0, 3, 9, 2, 8, 5, 6], 2, 5),
            ([4, 1, 8, 0, 6, 2, 9, 3, 7, 5], 3, 5),
            ([100, 0, 50], 25, 50),
            ([2878, 2944, 5635, 5873, 7873], 1222, 2551),
            ([143, 7354, 8845, 9125, 9304], 9087, 9161),
            ([2426, 4010, 5582, 7142, 8105, 9402, 9682], 2425, 3290),
            ([779, 1053, 3844, 4896, 4904, 7770, 9626], 2183, 4481),
        ],
    )
    def test_smallest_range_ii(self, nums: list[int], k: int, expected: int):
        result = run_smallest_range_ii(Solution, nums, k)
        assert_smallest_range_ii(result, expected)
