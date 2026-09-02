import pytest

from leetcode_py import logged_test

from .helpers import assert_next_greater_elements, run_next_greater_elements
from .solution import Solution


class TestNextGreaterElementII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 1], [2, -1, 2]),
            ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),
            ([5], [-1]),
            ([3], [-1]),
            ([-1], [-1]),
            ([1, 1, 1, 1], [-1, -1, -1, -1]),
            ([2, 2, 2], [-1, -1, -1]),
            ([5, 4, 3, 2, 1], [-1, 5, 5, 5, 5]),
            ([1, 2, 3, 4, 5], [2, 3, 4, 5, -1]),
            ([100, 1, 100, 1, 100], [-1, 100, -1, 100, -1]),
            ([-1000000000, 1000000000], [1000000000, -1]),
            ([1000000000, -1000000000], [-1, 1000000000]),
            ([3, 8, 4, 1, 9, 7], [8, 9, 9, 9, -1, 8]),
            ([-5, -3, -10, -1], [-3, -1, -1, -1]),
            ([2, 1, 2, 1, 3], [3, 2, 3, 3, -1]),
            ([6, 5, 4, 3, 2, 1, 7], [7, 7, 7, 7, 7, 7, -1]),
            ([0, -1, 0, -1, 0], [-1, 0, -1, 0, -1]),
            ([-2, 1, -1], [1, -1, 1]),
            ([0, -2, -4, -4, 2], [2, 2, 2, 2, -1]),
            ([-3, -4, -4, 4, 3, 2, -4], [4, 4, 4, -1, 4, 4, -3]),
            ([-3, 4, 1, 3, 2, 3, 0, 2], [4, -1, 3, 4, 3, 4, 2, 4]),
        ],
    )
    def test_next_greater_elements(self, nums: list[int], expected: list[int]):
        result = run_next_greater_elements(Solution, nums)
        assert_next_greater_elements(result, expected)
