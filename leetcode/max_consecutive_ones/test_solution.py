import pytest

from leetcode_py import logged_test

from .helpers import assert_find_max_consecutive_ones, run_find_max_consecutive_ones
from .solution import Solution


class TestMaxConsecutiveOnes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 1, 0, 1, 1, 1], 3),
            ([1, 0, 1, 1, 0, 1], 2),
            ([1], 1),
            ([0], 0),
            ([1, 1, 1, 1], 4),
            ([0, 0, 0], 0),
            ([1, 0, 1], 1),
            ([0, 1, 0], 1),
            ([1, 1, 0, 1], 2),
            ([0, 1, 1, 1, 0, 1, 1], 3),
            ([1, 1, 1, 0, 1], 3),
            ([0, 0, 1, 1, 1, 1, 0, 0], 4),
        ],
    )
    def test_find_max_consecutive_ones(self, nums: list[int], expected: int):
        result = run_find_max_consecutive_ones(Solution, nums)
        assert_find_max_consecutive_ones(result, expected)
