import pytest

from leetcode_py import logged_test

from .helpers import assert_min_moves, run_min_moves
from .solution import Solution


class TestMinimumMovesToEqualArrayElements:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([1, 2, 3], 3),
            ([1, 1, 1], 0),
            ([1], 0),
            ([0], 0),
            ([1, 2], 1),
            ([1, 2, 3, 4], 6),
            ([3, 1, 2], 3),
            ([1, 1, 2], 1),
            ([5, 5, 5, 5], 0),
            ([1, 10], 9),
            ([0, 5], 5),
            ([-1, 0, 1], 3),
            ([-5, -3, -1], 6),
            ([-1000000000, 1000000000], 2000000000),
            ([1, 1000000000], 999999999),
            ([2, 2, 3, 4], 3),
            ([7, 7, 7, 8], 1),
            ([0, 0, 0, 1], 1),
            ([4, 7], 3),
            ([4, 8, 4, -1, 6, -8], 61),
            ([7, -6, 5], 24),
            ([-1, -8], 7),
            ([-6], 0),
            ([-7, 4, 5, 2], 32),
            ([-8, 2, 4, 1], 31),
            ([-8, 0], 8),
        ],
    )
    def test_min_moves(self, nums: list[int], expected: int):
        result = run_min_moves(Solution, nums)
        assert_min_moves(result, expected)
