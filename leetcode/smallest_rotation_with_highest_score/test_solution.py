import pytest

from leetcode_py import logged_test

from .helpers import assert_best_rotation, run_best_rotation
from .solution import Solution


class TestSmallestRotationWithHighestScore:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 3, 1, 4, 0], 3),
            ([1, 3, 0, 2, 4], 0),
            ([0], 0),
            ([0, 0], 0),
            ([1, 0], 1),
            ([0, 1], 0),
            ([0, 0, 0, 0, 0], 0),
            ([3, 3, 3, 3, 3, 3], 0),
            ([0, 0, 0, 0, 0, 0, 0], 0),
            ([4, 6, 0, 6, 3, 4, 7, 1], 1),
            ([7, 2, 2, 9, 5, 5, 3, 5, 4, 4], 9),
            ([1, 0, 0], 1),
            ([0, 8, 0, 5, 3, 8, 9, 7, 4, 3], 0),
            ([0, 1, 1, 2, 5, 4], 0),
            ([4, 3, 0, 2, 1], 1),
            ([6, 5, 0, 5, 1, 0, 3], 1),
            ([8, 3, 1, 6, 6, 7, 8, 6, 2], 6),
            ([4, 3, 0, 1, 2], 1),
            ([2, 4, 5, 0, 8, 7, 5, 7, 1], 5),
            ([3, 4, 6, 7, 8, 9, 4, 9, 8, 4], 5),
        ],
    )
    def test_best_rotation(self, nums: list[int], expected: int):
        result = run_best_rotation(Solution, nums)
        assert_best_rotation(result, expected)
