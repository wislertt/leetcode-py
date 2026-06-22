import pytest

from leetcode_py import logged_test

from .helpers import assert_max_coins, run_max_coins
from .solution import Solution


class TestBurstBalloons:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 1, 5, 8], 167),
            ([1, 5], 10),
            ([5], 5),
            ([1], 1),
            ([0], 0),
            ([100], 100),
            ([0, 0, 0], 0),
            ([2], 2),
            ([1, 2], 4),
            ([2, 2], 6),
            ([1, 2, 3], 12),
            ([3, 2, 1], 12),
            ([3, 1, 5], 35),
            ([4, 6, 7, 9], 639),
        ],
    )
    def test_max_coins(self, nums: list[int], expected: int):
        result = run_max_coins(Solution, nums)
        assert_max_coins(result, expected)
