import pytest

from leetcode_py import logged_test

from .helpers import assert_move_zeroes, run_move_zeroes
from .solution import Solution


class TestMoveZeroes:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
            ([0], [0]),
            ([1, 2, 3], [1, 2, 3]),
            ([0, 0, 0], [0, 0, 0]),
            ([1, 0], [1, 0]),
            ([0, 1], [1, 0]),
            ([1], [1]),
            ([1, 0, 2, 0, 3], [1, 2, 3, 0, 0]),
            ([0, 0, 1], [1, 0, 0]),
            ([1, 0, 0, 2, 0, 3], [1, 2, 3, 0, 0, 0]),
            ([2, 1], [2, 1]),
            ([0, 0, 0, 0, 1], [1, 0, 0, 0, 0]),
            ([1, 2, 3, 0, 4, 0, 5], [1, 2, 3, 4, 5, 0, 0]),
            ([4, 2, 4, 0, 0, 3, 0, 5, 1, 0], [4, 2, 4, 3, 5, 1, 0, 0, 0, 0]),
            ([-1, 0, -2, 0, -3], [-1, -2, -3, 0, 0]),
        ],
    )
    def test_move_zeroes(self, nums: list[int], expected: list[int]):
        result = run_move_zeroes(Solution, nums)
        assert_move_zeroes(result, expected)
