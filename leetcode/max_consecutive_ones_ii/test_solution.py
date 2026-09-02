import pytest

from leetcode_py import logged_test

from .helpers import assert_find_max_ones, run_find_max_ones
from .solution import Solution


class TestMaxConsecutiveOnesII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 0, 1, 1, 0], 4),
            ([1, 0, 1, 1, 0, 1], 4),
            ([1, 1, 1, 1], 4),
            ([0, 0, 0], 1),
            ([0], 1),
            ([1], 1),
            ([1, 0], 2),
            ([1, 1, 0, 1], 4),
            ([1, 0, 0, 1], 2),
            ([0, 1, 1, 0, 1, 1, 1, 0, 1], 6),
            ([1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0], 3),
            ([0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1], 3),
        ],
    )
    def test_find_max_ones(self, nums: list[int], expected: int):
        result = run_find_max_ones(Solution, nums)
        assert_find_max_ones(result, expected)
