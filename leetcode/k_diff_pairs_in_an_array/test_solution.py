import pytest

from leetcode_py import logged_test

from .helpers import assert_find_pairs, run_find_pairs
from .solution import Solution


class TestKDiffPairsInAnArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([3, 1, 4, 1, 5], 2, 2),
            ([1, 2, 3, 4, 5], 1, 4),
            ([1, 3, 1, 5, 4], 0, 1),
            ([1, 1, 1, 1], 0, 1),
            ([1], 0, 0),
            ([1], 1, 0),
            ([1, 5, 9], 4, 2),
            ([1, 2, 3], 10, 0),
            ([-1, -2, -3], 1, 2),
            ([-1, 0, 1], 1, 2),
            ([6, 7, 6, 7, 8], 1, 2),
            ([1, 3, 1, 5, 4], 3, 1),
            ([2, 2, 2, 2, 2], 0, 1),
            ([10000000, -10000000], 10000000, 0),
            ([10000000, 0], 10000000, 1),
            ([4, 3, -4, -5], 3, 0),
        ],
    )
    def test_find_pairs(self, nums: list[int], k: int, expected: int):
        result = run_find_pairs(Solution, nums, k)
        assert_find_pairs(result, expected)
