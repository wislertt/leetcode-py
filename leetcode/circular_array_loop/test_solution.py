import pytest

from leetcode_py import logged_test

from .helpers import assert_circular_array_loop, run_circular_array_loop
from .solution import Solution


class TestCircularArrayLoop:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, -1, 1, 2, 2], True),
            ([-1, -2, -3, -4, -5, 6], False),
            ([1, -1, 5, 1, 4], True),
            ([-1, -1], True),
            ([1, 2], False),
            ([3, 1, 2], True),
            ([-1, 2], False),
            ([1], False),
            ([1, 1], True),
            ([-1, -2, -3, -4, -5], False),
            ([-2, 1, -1], False),
            ([2, 1, 1], True),
            ([-2, 2, 1, 4, 2, -4, -2, -2], False),
            ([-1, -2, -1, 3, 3, -2, 3], False),
            ([4, -4, -3, 2, -3, -3], True),
            ([1, -1], False),
            ([2, -1, -1, 2, -1], False),
            ([1, 3, -4, 2, -2, -4], True),
            ([2, 1, 2, -2], True),
            ([-4, 3, 1, 2, 4, 2, 2, 3], True),
        ],
    )
    def test_circular_array_loop(self, nums: list[int], expected: bool):
        result = run_circular_array_loop(Solution, nums)
        assert_circular_array_loop(result, expected)
