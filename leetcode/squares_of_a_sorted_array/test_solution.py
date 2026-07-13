import pytest

from leetcode_py import logged_test

from .helpers import assert_sorted_squares, run_sorted_squares
from .solution import Solution


class TestTestSquaresOfASortedArray:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
            ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121]),
            ([0], [0]),
            ([1], [1]),
            ([-1], [1]),
            ([1, 2, 3], [1, 4, 9]),
            ([-3, -2, -1], [1, 4, 9]),
            ([-5, 5], [25, 25]),
            ([], []),
            ([-10000, 10000], [100000000, 100000000]),
            ([-2, 0, 2], [0, 4, 4]),
            ([-3, -1, 2, 4, 5], [1, 4, 9, 16, 25]),
            ([-10, -9, -8, -7], [49, 64, 81, 100]),
            ([0, 0, 0], [0, 0, 0]),
        ],
    )
    def test_sorted_squares(self, nums: list[int], expected: list[int]):
        result = run_sorted_squares(Solution, nums)
        assert_sorted_squares(result, expected)
