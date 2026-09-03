import pytest

from leetcode_py import logged_test

from .helpers import assert_valid_mountain_array, run_valid_mountain_array
from .solution import Solution


class TestValidMountainArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([2, 1], False),
            ([3, 5, 5], False),
            ([0, 3, 2, 1], True),
            ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], False),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], False),
            ([1, 2, 3, 4, 3, 2, 1, 0], True),
            ([1, 2, 3], False),
            ([3, 2, 1], False),
            ([2, 2, 2], False),
            ([1, 3, 2, 4, 1], False),
            ([0, 1, 0], True),
            ([1], False),
            ([1, 2], False),
            ([2, 1, 2], False),
            ([1, 2, 2, 3, 2, 1], False),
            ([1, 2, 3, 2, 2, 1], False),
            ([5, 6, 7, 8, 9, 8, 7, 6, 5], True),
            ([1, 2, 3, 4, 5], False),
            ([4, 3, 2, 1], False),
            ([1, 2, 1], True),
            ([0, 3, 2, 5, 4, 3, 2, 1], False),
            ([1, 2, 3, 4, 5, 4, 3, 2, 1, 0], True),
            ([2, 2, 3, 2], False),
            ([0, 1, 1, 0], False),
        ],
    )
    def test_valid_mountain_array(self, arr: list[int], expected: bool):
        result = run_valid_mountain_array(Solution, arr)
        assert_valid_mountain_array(result, expected)
