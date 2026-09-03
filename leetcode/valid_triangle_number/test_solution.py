import pytest

from leetcode_py import logged_test

from .helpers import assert_triangle_number, run_triangle_number
from .solution import Solution


class TestValidTriangleNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 2, 3, 4], 3),
            ([4, 2, 3, 4], 4),
            ([1, 1, 1, 1], 4),
            ([0, 1, 1], 0),
            ([0, 0, 0], 0),
            ([1, 2, 3], 0),
            ([3, 4, 5], 1),
            ([1], 0),
            ([1, 2], 0),
            ([1, 1, 2], 0),
            ([5, 5, 5, 5, 5], 10),
            ([0, 0, 1, 1, 2], 0),
            ([2, 2, 2], 1),
            ([1, 2, 3, 4, 5, 6], 7),
            ([7, 10, 4, 3, 20, 15], 4),
            ([5, 10, 2, 10, 5, 8, 0], 10),
            ([7, 3, 7, 8, 8, 10, 9], 33),
            ([3, 9, 2, 1], 0),
            ([11, 1, 9, 0], 0),
            ([12, 11, 10], 1),
        ],
    )
    def test_triangle_number(self, nums: list[int], expected: int):
        result = run_triangle_number(Solution, nums)
        assert_triangle_number(result, expected)
