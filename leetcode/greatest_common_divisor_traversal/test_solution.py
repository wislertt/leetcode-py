import pytest

from leetcode_py import logged_test

from .helpers import assert_can_traverse_all_pairs, run_can_traverse_all_pairs
from .solution import Solution


class TestTestGreatestCommonDivisorTraversal:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 3, 6], True),
            ([3, 9, 5], False),
            ([4, 3, 12, 8], True),
            ([1], True),
            ([1, 1], False),
            ([2, 2], True),
            ([2, 3, 5], False),
            ([2, 4, 8, 16], True),
            ([1, 2], False),
            ([2], True),
            ([6, 10, 15], True),
            ([2, 3, 6, 12], True),
            ([7, 7, 7], True),
            ([2, 3, 5, 7, 11], False),
            ([6, 7, 14], True),
        ],
    )
    def test_can_traverse_all_pairs(self, nums: list[int], expected: bool):
        result = run_can_traverse_all_pairs(Solution, nums)
        assert_can_traverse_all_pairs(result, expected)
