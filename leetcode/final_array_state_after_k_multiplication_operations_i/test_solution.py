import pytest

from leetcode_py import logged_test

from .helpers import assert_get_final_state, run_get_final_state
from .solution import Solution


class TestFinalArrayStateAfterKMultiplicationOperationsI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, multiplier, expected",
        [
            ([2, 1, 3, 5, 6], 5, 2, [8, 4, 6, 5, 6]),
            ([1, 2], 3, 4, [16, 8]),
            ([5], 10, 3, [295245]),
            ([1], 1, 1, [1]),
            ([7, 7, 7, 7], 4, 2, [14, 14, 14, 14]),
            ([3, 3, 3], 2, 5, [15, 15, 3]),
            ([10, 2, 2, 8], 3, 2, [10, 8, 4, 8]),
            ([100, 99, 98], 10, 5, [12500, 12375, 61250]),
            ([1, 100], 10, 5, [15625, 62500]),
            ([4, 1, 5, 1, 2], 10, 3, [12, 27, 15, 27, 18]),
            ([6, 5, 4, 3, 2, 1], 6, 4, [6, 20, 16, 12, 8, 16]),
            ([2, 2, 1, 1, 3], 7, 2, [4, 4, 4, 4, 6]),
            ([9, 8, 7], 1, 5, [9, 8, 35]),
            ([12, 50, 3], 7, 5, [300, 1250, 375]),
            ([44, 28, 41, 26, 43, 38, 22, 12], 1, 1, [44, 28, 41, 26, 43, 38, 22, 12]),
            ([16, 35, 4, 47], 5, 5, [80, 175, 100, 235]),
            ([37], 9, 1, [37]),
            ([47, 34, 20, 3, 15, 26], 10, 2, [47, 68, 80, 48, 60, 52]),
        ],
    )
    def test_get_final_state(self, nums: list[int], k: int, multiplier: int, expected: list[int]):
        result = run_get_final_state(Solution, nums, k, multiplier)
        assert_get_final_state(result, expected)
