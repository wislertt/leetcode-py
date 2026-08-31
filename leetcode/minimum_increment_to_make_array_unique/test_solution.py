import pytest

from leetcode_py import logged_test

from .helpers import assert_min_increment_for_unique, run_min_increment_for_unique
from .solution import Solution


class TestMinimumIncrementToMakeArrayUnique:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 2], 1),
            ([3, 2, 1, 2, 1, 7], 6),
            ([0], 0),
            ([5], 0),
            ([1, 1], 1),
            ([0, 0], 1),
            ([1, 2, 3], 0),
            ([2, 2, 2], 3),
            ([0, 0, 0, 0], 6),
            ([4, 4, 4, 4], 6),
            ([1, 1, 2, 2], 4),
            ([5, 5, 5, 5, 5], 10),
            ([3, 3, 3, 3, 3, 3], 15),
            ([0, 2, 2, 4, 4, 4], 4),
        ],
    )
    def test_min_increment_for_unique(self, nums: list[int], expected: int):
        result = run_min_increment_for_unique(Solution, nums)
        assert_min_increment_for_unique(result, expected)
