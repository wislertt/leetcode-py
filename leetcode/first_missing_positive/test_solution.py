import pytest

from leetcode_py import logged_test

from .helpers import assert_first_missing_positive, run_first_missing_positive
from .solution import Solution


class TestFirstMissingPositive:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 0], 3),
            ([3, 4, -1, 1], 2),
            ([7, 8, 9, 11, 12], 1),
            ([1], 2),
            ([2], 1),
            ([1, 1], 2),
            ([1, 2, 3], 4),
            ([2, 3, 4], 1),
            ([1, 2, 3, 4, 5], 6),
            ([3, 4, 2, 1], 5),
            ([-5, -3, -1], 1),
            ([0], 1),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11),
            ([2, 2, 2, 2], 1),
            ([-1, -2, -3], 1),
            ([1, 2, 3, 1, 2, 3], 4),
            ([2, 1, 4, 3, 6, 5], 7),
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 11], 10),
            ([2], 1),
            ([1000000], 1),
        ],
    )
    def test_first_missing_positive(self, nums: list[int], expected: int):
        result = run_first_missing_positive(Solution, nums)
        assert_first_missing_positive(result, expected)
