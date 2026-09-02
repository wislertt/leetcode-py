import pytest

from leetcode_py import logged_test

from .helpers import assert_intersection, run_intersection
from .solution import Solution


class TestIntersectionOfTwoArraysII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums1, nums2, expected",
        [
            ([1, 2, 2, 1], [2, 2], [2, 2]),
            ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),
            ([1], [1], [1]),
            ([1], [2], []),
            ([0, 0, 0], [0, 0], [0, 0]),
            ([1, 2, 3], [4, 5, 6], []),
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
            ([7, 8, 9, 10], [10, 9, 8, 7, 6, 5], [7, 8, 9, 10]),
            ([1000, 999, 998], [998, 999, 1000, 1], [998, 999, 1000]),
            ([1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]),
            ([2, 4, 6, 8], [1, 3, 5, 7, 9], []),
            ([3, 3, 5, 7, 9], [7, 5, 3, 3], [3, 3, 5, 7]),
            ([0, 1000], [1000, 0], [0, 1000]),
            ([1, 2, 2, 3, 3, 3], [2, 2, 3, 3, 4], [2, 2, 3, 3]),
        ],
    )
    def test_intersection(self, nums1: list[int], nums2: list[int], expected: list[int]):
        result = run_intersection(Solution, nums1, nums2)
        assert_intersection(result, expected)
