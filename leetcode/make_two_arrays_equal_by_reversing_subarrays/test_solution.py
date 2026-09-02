import pytest

from leetcode_py import logged_test

from .helpers import assert_can_be_equal, run_can_be_equal
from .solution import Solution


class TestMakeTwoArraysEqualByReversingSubarrays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "target, arr, expected",
        [
            ([1, 2, 3, 4], [2, 4, 1, 3], True),
            ([7], [7], True),
            ([3, 7, 9], [3, 7, 11], False),
            ([1], [2], False),
            ([1, 2], [2, 1], True),
            ([1, 2], [1, 1], False),
            ([1, 2, 3], [3, 2, 1], True),
            ([1, 1, 2], [1, 2, 1], True),
            ([1, 1, 2], [2, 2, 1], False),
            ([4, 5, 6], [6, 5, 4], True),
            ([1, 2, 2, 3], [3, 2, 2, 1], True),
            ([1, 2, 2, 3], [1, 2, 3, 3], False),
            ([1000, 999], [999, 1000], True),
            ([1, 3, 5, 7], [7, 5, 3, 1], True),
            ([1, 3, 5, 7], [1, 3, 5, 8], False),
            ([2, 2, 2, 2], [2, 2, 2, 2], True),
        ],
    )
    def test_can_be_equal(self, target: list[int], arr: list[int], expected: bool):
        result = run_can_be_equal(Solution, target, arr)
        assert_can_be_equal(result, expected)
