import pytest

from leetcode_py import logged_test

from .helpers import assert_minimize_max, run_minimize_max
from .solution import Solution


class TestMinimizeTheMaximumDifferenceOfPairs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, p, expected",
        [
            ([10, 1, 2, 7, 1, 3], 2, 1),
            ([4, 2, 1, 2], 1, 0),
            ([1], 0, 0),
            ([1, 3, 1], 1, 0),
            ([0, 0, 0, 0], 2, 0),
            ([1, 6, 1, 1], 1, 0),
            ([3, 4, 2, 3, 2, 1, 2], 3, 1),
            ([10, 1, 2, 7, 1, 3], 1, 0),
            ([0, 5, 3, 4], 2, 3),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 5, 1),
            ([1, 2, 3, 4, 5, 6], 3, 1),
            ([1000000000, 0], 1, 1000000000),
            ([5, 5, 5], 1, 0),
            ([2, 2, 2, 3], 2, 1),
            ([7, 9, 5, 6, 3, 2], 2, 1),
            ([3, 1, 4, 1, 5], 0, 0),
            ([1, 1000000000, 2, 999999999], 2, 1),
            ([4, 2, 1, 2], 0, 0),
            ([1000000000, 999999999, 5, 4, 3, 2], 3, 1),
            ([12, 4, 19, 7, 1, 15, 8, 3], 4, 4),
        ],
    )
    def test_minimize_max(self, nums: list[int], p: int, expected: int):
        result = run_minimize_max(Solution, nums, p)
        assert_minimize_max(result, expected)
