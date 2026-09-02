import pytest

from leetcode_py import logged_test

from .helpers import assert_increasing_triplet, run_increasing_triplet
from .solution import Solution


class TestIncreasingTripletSubsequence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3, 4, 5], True),
            ([5, 4, 3, 2, 1], False),
            ([2, 1, 5, 0, 4, 6], True),
            ([1], False),
            ([1, 2], False),
            ([1, 1, 1], False),
            ([1, 2, 2], False),
            ([1, 2, 3], True),
            ([2, 4, 1, 3], False),
            ([1, 5, 0, 4, 1, 3], True),
            ([-2147483648, 0, 2147483647], True),
            ([20, 100, 10, 12, 5, 13], True),
            ([1, 2, 1, 2, 1, 2], False),
            ([3, 4, 2, 5], True),
            ([0, -1, 1], False),
            ([2, 6, 0, 0], False),
            ([-1, 6, -1], False),
            ([6, 6, -3, -6, -2, 6], True),
            ([5, -6, 2, 6, -3, -6, 0], True),
            ([-5, -5], False),
            ([4, -2, -2], False),
            ([1, 2, -6], False),
        ],
    )
    def test_increasing_triplet(self, nums: list[int], expected: bool):
        result = run_increasing_triplet(Solution, nums)
        assert_increasing_triplet(result, expected)
