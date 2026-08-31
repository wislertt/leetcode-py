import pytest

from leetcode_py import logged_test

from .helpers import assert_find_peak_element, run_find_peak_element
from .solution import Solution


class TestFindPeakElement:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 1], 2),
            ([1, 2, 1, 3, 5, 6, 4], 5),
            ([1], 0),
            ([1, 2], 1),
            ([2, 1], 0),
            ([1, 2, 3, 4, 5], 4),
            ([5, 4, 3, 2, 1], 0),
            ([1, 3, 2, 1], 1),
            ([3, 1, 2, 1, 3], 2),
            ([1, 2, 1, 2, 1], 3),
            ([-2147483648], 0),
            ([1, 2, 3, 1, 2, 1, 4], 6),
            ([10, 20, 15, 2, 23, 90, 67], 5),
            ([1, 5, 1], 1),
            ([3, 4, 3, 2, 1], 1),
            ([6, 3, 5, 4], 2),
        ],
    )
    def test_find_peak_element(self, nums: list[int], expected: int):
        result = run_find_peak_element(Solution, nums)
        assert_find_peak_element(result, expected)
