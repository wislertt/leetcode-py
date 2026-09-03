import pytest

from leetcode_py import logged_test

from .helpers import assert_longest_mountain, run_longest_mountain
from .solution import Solution


class TestLongestMountainInArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([2, 1, 4, 7, 3, 2, 5], 5),
            ([2, 2, 2], 0),
            ([0, 1, 0, 0, 1, 0, 0, 1, 2, 2, 3], 3),
            ([1], 0),
            ([1, 2], 0),
            ([1, 2, 3], 0),
            ([3, 2, 1], 0),
            ([1, 2, 1], 3),
            ([1, 2, 2, 1], 0),
            ([1, 2, 3, 2, 1], 5),
            ([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0], 11),
            ([1, 1, 1, 1], 0),
            ([5, 6, 1, 2, 3, 2, 1, 0, 4], 6),
            ([2, 1, 4, 7, 3, 2, 5, 6, 6, 8], 5),
            ([3, 3, 4, 5, 2, 1], 5),
            ([2, 0, 4], 0),
            ([4, 1, 0, 1, 3], 0),
            ([1, 2, 2, 3, 0, 3, 2, 3, 3, 0], 3),
            ([3, 3, 3, 1, 1, 3, 0, 1, 1, 1, 3], 3),
            ([1, 4, 1, 1, 1, 3, 1, 3, 1, 0, 1], 4),
            ([4, 2, 1, 1, 4], 0),
        ],
    )
    def test_longest_mountain(self, arr: list[int], expected: int):
        result = run_longest_mountain(Solution, arr)
        assert_longest_mountain(result, expected)
