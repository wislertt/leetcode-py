import pytest

from leetcode_py import logged_test

from .helpers import assert_find_in_mountain_array, run_find_in_mountain_array
from .solution import Solution


class TestFindInMountainArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, target, expected",
        [
            ([1, 2, 3, 4, 5, 3, 1], 3, 2),
            ([0, 1, 2, 4, 2, 1], 3, -1),
            ([1, 2, 3, 4, 5, 3, 1], 5, 4),
            ([1, 2, 3, 4, 5, 3, 1], 1, 0),
            ([1, 2, 3, 4, 5, 3, 1], 6, -1),
            ([1, 5, 2], 5, 1),
            ([1, 5, 2], 2, 2),
            ([1, 5, 2], 0, -1),
            ([0, 5, 3, 1], 3, 2),
            ([1, 3, 1], 1, 0),
            ([1, 3, 1], 3, 1),
            ([1, 2, 3, 2, 1], 2, 1),
            ([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1], 6, 5),
            ([1, 3, 5, 7, 6, 4, 2], 7, 3),
            ([1, 3, 5, 7, 6, 4, 2], 2, 6),
            ([3, 5, 3, 2, 0], 2, 3),
        ],
    )
    def test_find_in_mountain_array(self, arr: list[int], target: int, expected: int):
        result = run_find_in_mountain_array(Solution, arr, target)
        assert_find_in_mountain_array(result, expected)
