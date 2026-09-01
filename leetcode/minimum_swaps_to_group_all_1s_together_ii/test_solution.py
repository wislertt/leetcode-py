import pytest

from leetcode_py import logged_test

from .helpers import assert_min_swaps, run_min_swaps
from .solution import Solution


class TestMinimumSwapsToGroupAll1sTogetherII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([0, 1, 0, 1, 1, 0, 0], 1),
            ([0, 1, 1, 1, 0, 0, 1, 1, 0], 2),
            ([1, 1, 0, 0, 1], 0),
            ([1], 0),
            ([0], 0),
            ([1, 0], 0),
            ([0, 1], 0),
            ([1, 1, 1, 1], 0),
            ([0, 0, 0, 0], 0),
            ([1, 0, 0, 0, 1], 0),
            ([0, 1, 0, 0, 0, 1, 0], 1),
            ([1, 0, 1, 0, 1, 0], 1),
            ([1, 1, 1, 0, 0, 0, 0], 0),
            ([0, 0, 1, 1, 1, 0, 0, 0], 0),
            ([1, 1, 1, 0, 1, 0, 0, 0, 1], 1),
            ([0, 0, 0, 0, 1, 0, 1], 1),
            ([1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0], 2),
            ([0, 0, 1], 0),
            ([0, 1, 1], 0),
            ([0, 0, 1, 0, 0, 0, 1, 1, 1], 1),
        ],
    )
    def test_min_swaps(self, nums: list[int], expected: int):
        result = run_min_swaps(Solution, nums)
        assert_min_swaps(result, expected)
