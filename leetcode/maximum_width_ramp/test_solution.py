import pytest

from leetcode_py import logged_test

from .helpers import assert_max_width_ramp, run_max_width_ramp
from .solution import Solution


class TestMaximumWidthRamp:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([6, 0, 8, 2, 1, 5], 4),
            ([9, 8, 1, 0, 1, 9, 4, 0, 4, 1], 7),
            ([1, 2], 1),
            ([2, 1], 0),
            ([5, 5], 1),
            ([1, 2, 3, 4, 5], 4),
            ([5, 4, 3, 2, 1], 0),
            ([3, 3, 3, 3], 3),
            ([1, 0, 1, 0, 1], 4),
            ([2, 2, 1, 1, 3], 4),
            ([0, 1, 0, 1, 0, 1], 5),
            ([4, 2, 3, 1, 5, 0, 6], 6),
            ([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], 0),
            ([6, 0, 8, 2, 1, 5, 4, 3, 2, 9], 9),
            ([1, 0, 2, 1, 3, 2, 4, 3, 9], 8),
        ],
    )
    def test_max_width_ramp(self, nums: list[int], expected: int):
        result = run_max_width_ramp(Solution, nums)
        assert_max_width_ramp(result, expected)
