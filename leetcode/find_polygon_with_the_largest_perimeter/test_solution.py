import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_perimeter, run_largest_perimeter
from .solution import Solution


class TestFindPolygonWithTheLargestPerimeter:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([5, 5, 5], 15),
            ([1, 12, 1, 2, 5, 50, 3], 12),
            ([5, 5, 50], -1),
            ([1, 1, 1], 3),
            ([1, 2, 3], -1),
            ([2, 3, 4], 9),
            ([1, 1, 3], -1),
            ([1, 1, 2, 3], 7),
            ([3, 6, 2, 3], 14),
            ([4, 2, 1], -1),
            ([1000000000, 1000000000, 1000000000], 3000000000),
            ([1000000000, 999999999, 1], -1),
            ([1000000000, 999999999, 2], 2000000001),
            ([1, 1, 1, 100], 3),
            ([1, 1, 2, 4, 8], -1),
            ([5, 5, 5, 5], 20),
            ([7, 4, 3, 2, 1], 17),
            ([2, 2, 2, 9], 6),
        ],
    )
    def test_largest_perimeter(self, nums: list[int], expected: int):
        result = run_largest_perimeter(Solution, nums)
        assert_largest_perimeter(result, expected)
