import pytest

from leetcode_py import logged_test

from .helpers import assert_special_array, run_special_array
from .solution import Solution


class TestSpecialArrayWithXElementsGreaterThanOrEqualX:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1], 1),
            ([1000], 1),
            ([0, 1], 1),
            ([0, 2], 1),
            ([3, 5], 2),
            ([2, 2], 2),
            ([0, 4, 3, 0, 4], 3),
            ([9, 5, 8], 3),
            ([2, 1, 5, 1, 6, 6], 3),
            ([5, 5, 5, 5, 5], 5),
            ([0, 0], -1),
            ([0], -1),
            ([0, 0, 0, 0], -1),
            ([1, 1, 1], -1),
            ([3, 6, 7, 7, 0], -1),
            ([1, 4], -1),
            ([6, 5, 10, 7, 5, 6, 0], -1),
            ([9, 4, 10, 4, 3, 4, 7, 3], -1),
        ],
    )
    def test_special_array(self, nums: list[int], expected: int):
        result = run_special_array(Solution, nums)
        assert_special_array(result, expected)
