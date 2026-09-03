import pytest

from leetcode_py import logged_test

from .helpers import assert_largest_perimeter, run_largest_perimeter
from .solution import Solution


class TestLargestPerimeterTriangle:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 1, 2], 5),
            ([1, 2, 1, 10], 0),
            ([1, 1, 1], 3),
            ([1, 2, 3], 0),
            ([3, 2, 3, 4], 10),
            ([3, 6, 2, 3], 8),
            ([4, 2, 1], 0),
            ([5, 5, 50], 0),
            ([10, 50, 5, 1], 0),
            ([2, 2, 2, 2, 2], 6),
            ([1, 1, 2, 1], 3),
            ([1000000, 1000000, 1000000], 3000000),
            ([999999, 1, 1], 0),
            ([7, 1, 14, 11, 1, 1], 32),
            ([24, 22, 7, 28, 23], 75),
            ([10, 18, 19], 47),
            ([26, 25, 29, 11, 8, 29], 84),
            ([30, 20, 28, 1, 9, 22, 21], 80),
            ([15, 22, 2, 16, 29, 30, 18], 81),
            ([25, 5, 1, 17, 24, 11], 66),
        ],
    )
    def test_largest_perimeter(self, nums: list[int], expected: int):
        result = run_largest_perimeter(Solution, nums)
        assert_largest_perimeter(result, expected)
