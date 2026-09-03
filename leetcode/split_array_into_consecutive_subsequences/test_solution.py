import pytest

from leetcode_py import logged_test

from .helpers import assert_is_possible, run_is_possible
from .solution import Solution


class TestSplitArrayIntoConsecutiveSubsequences:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 3, 4, 5], True),
            ([1, 2, 3, 3, 4, 4, 5, 5], True),
            ([1, 2, 3, 4, 4, 5], False),
            ([1, 2, 3], True),
            ([1, 2], False),
            ([1], False),
            ([1, 2, 3, 4], True),
            ([1, 2, 3, 4, 5], True),
            ([3, 4, 5, 6, 7, 8], True),
            ([1, 1, 1, 2, 2, 2, 3, 3, 3], True),
            ([1, 1, 1, 2, 2, 3], False),
            ([1, 2, 3, 5, 6, 7], True),
            ([1, 2, 3, 4, 5, 5, 6, 7], True),
            ([-3, -2, -1, 0, 1, 2], True),
            ([-1000, -999, -998], True),
            ([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3], True),
            ([1, 2, 3, 3, 4, 4, 5], True),
            ([1, 2, 4, 5, 6], False),
            ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], True),
            ([5, 5, 5, 6, 7, 7, 8], False),
            ([-3, -1, -1, 0, 1, 1, 1, 2, 3, 3, 4, 6], False),
            ([3, 6], False),
            ([-2, -1, 0, 1, 2, 3, 4, 5], True),
            ([-3, -2, -1, 0, 0, 0, 2, 3, 4, 5, 5, 6], False),
            ([-3, -2, -2, -1, 0, 1, 1, 1, 5, 6], False),
            ([6], False),
            ([1, 3, 4, 4], False),
            ([3], False),
            ([-3, -1, 5, 5, 5], False),
            ([-3, -3], False),
            ([0, 3, 5], False),
            ([-3, -3, -3, 0, 0, 1, 1, 2, 5, 5], False),
        ],
    )
    def test_is_possible(self, nums: list[int], expected: bool):
        result = run_is_possible(Solution, nums)
        assert_is_possible(result, expected)
