import pytest

from leetcode_py import logged_test

from .helpers import assert_can_reorder_doubled, run_can_reorder_doubled
from .solution import Solution


class TestArrayOfDoubledPairs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arr, expected",
        [
            ([3, 1, 3, 6], False),
            ([2, 1, 2, 6], False),
            ([4, -2, 2, -4], True),
            ([1, 2], True),
            ([2, 1], True),
            ([1, 1], False),
            ([0, 0], True),
            ([0, 1], False),
            ([-2, -4], True),
            ([-1, -4], False),
            ([-1, -2, -4, -8], True),
            ([1, 2, 4, 8], True),
            ([1, 2, 3, 6], True),
            ([2, 4, 1, 3], False),
            ([10, 5, 20, 40], True),
            ([4, 2, 4, 2, 4, 8], True),
            ([0, 0, 0, 0], True),
            ([-4, -2, 2, 4], True),
            ([1, 2, 1, 2], True),
            ([-2, -1, 2, 4], True),
            ([-4, -4, -2, -2, 2, 2, 4, 4], True),
            ([-8, -8, -4, -4, -2, -2, -1, -1], True),
            ([2, 1, 2, 1, 1, 1, 2, 2], True),
            ([-3, -6, 3, 6, 12, 24, -12, -24], True),
            ([0, 0, 0, 1, 1, 2], False),
            ([-5, -10, 5, 10, -20, -20, -10, -10], True),
            ([-20, 66, -36, -18, -68, -40, 33, -34], True),
            ([8, -10, -64, -25, -14, 4, -5, -28, -32, -50], True),
            ([-40, 4, -2, 46, 2, 18, 23, 68, 36, -80, -1, 34], True),
            ([64, -22, 7, -6, -11, -34, 42, 32, 21, -12, 14, -68], True),
        ],
    )
    def test_can_reorder_doubled(self, arr: list[int], expected: bool):
        result = run_can_reorder_doubled(Solution, arr)
        assert_can_reorder_doubled(result, expected)
