import pytest

from leetcode_py import logged_test

from .helpers import assert_split_array, run_split_array
from .solution import Solution


class TestSplitArrayWithEqualSum:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 1, 2, 1, 2, 1], True),
            ([1, 2, 1, 2, 1, 2, 1, 2], False),
            ([-3, 3, 1, -3, 1, -2, 0, -1, 1, -1, 1, -2], False),
            ([-1, -3, -1, 0, -1, -1, 3, -3, 3, -1, -1], False),
            ([1, 1, -2, -3, -2, -3, 1], False),
            ([0, 3, 2, -3, 3, -3, 0, -3, -3, 1], False),
            ([0, 3, 3, 0, 0, 2, -1, 1, 1, 3, -2, 3], False),
            ([0, -2, 3, 1, 1, 2, -3, 3, -2, 0, -2, -2], False),
            ([2, 0, -3, 1, 2, 0, -3, 0], False),
            ([1, -3, 1, 0, 3, 1, 0, -1, 0, 1], True),
            ([-3, -2, -3, -3, 0, 0, 0, -3], False),
            ([2, 2, -1, -2, 0, -1, 0, 0, -1, 2, -2, 0], False),
            ([-1, -1, 2, 3, -3, -3, -2, -1, 2, 3], False),
            ([-3, 0, -3, 0, 1, 0, 2, -3, -2, 0], False),
            ([-1, -3, -3, -2, -2, 0, -1, 0, 3, -3, -2, 1], False),
            ([2, 3, -3, 0, 2, 2, -2, -3, 0, 1], False),
        ],
    )
    def test_split_array(self, nums: list[int], expected: bool):
        result = run_split_array(Solution, nums)
        assert_split_array(result, expected)
