import pytest

from leetcode_py import logged_test

from .helpers import assert_max_rotate_function, run_max_rotate_function
from .solution import Solution


class TestRotateFunction:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([4, 3, 2, 6], 26),
            ([100], 0),
            ([1], 0),
            ([0], 0),
            ([-1], 0),
            ([-100], 0),
            ([1, 2], 2),
            ([2, 1], 2),
            ([-1, -2], -1),
            ([1, 2, 3], 8),
            ([3, 2, 1], 7),
            ([4, 3, 2, 6, 5], 45),
            ([-1, -1, -1], -3),
            ([1, -2, 3, -4, 5], 14),
            ([0, 0, 0, 1], 3),
            ([100, -100, 100], 300),
            ([-5, 4, -3, 2, -1, 0], 0),
            ([7, 1, 5, 3, 6, 4], 80),
            ([-100, 100, -100, 100, -100], 200),
            ([10, -10, 10, -10, 10, -10], 30),
            ([-29], 0),
            ([42, 92, -64, -12, 7], 496),
        ],
    )
    def test_max_rotate_function(self, nums: list[int], expected: int):
        result = run_max_rotate_function(Solution, nums)
        assert_max_rotate_function(result, expected)
