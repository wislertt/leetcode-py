import pytest

from leetcode_py import logged_test

from .helpers import assert_find_lhs, run_find_lhs
from .solution import Solution


class TestLongestHarmoniousSubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 3, 2, 2, 5, 2, 3, 7], 5),
            ([1, 2, 3, 4], 2),
            ([1, 1, 1, 1], 0),
            ([1, 2], 2),
            ([1], 0),
            ([1, 2, 2, 1], 4),
            ([1, 3, 5, 7], 0),
            ([-1, 0, -1, 0], 4),
            ([0, 2, 4, 6], 0),
            ([1, 2, 3], 2),
            ([2, 2, 2, 3], 4),
            ([5, 5, 5, 5, 6, 6], 6),
            ([3, 4, 4, 3, 3], 5),
            ([1, 1, 2, 2, 3, 3], 4),
            ([3, -1, 0], 2),
            ([-4], 0),
            ([-1, -4, -4, -3, 4, -2, 2, -4], 4),
            ([3], 0),
            ([2, 4, -2, -1, 3, 4, 4], 4),
            ([2, 4, 1, 2, 4], 3),
            ([-1, 3, -4, 0, 2, -1, 4], 3),
            ([-3, -3, -3], 0),
        ],
    )
    def test_find_lhs(self, nums: list[int], expected: int):
        result = run_find_lhs(Solution, nums)
        assert_find_lhs(result, expected)
