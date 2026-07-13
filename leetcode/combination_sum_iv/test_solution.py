import pytest

from leetcode_py import logged_test

from .helpers import assert_combination_sum4, run_combination_sum4
from .solution import Solution


class TestCombinationSumIV:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, target, expected",
        [
            ([1, 2, 3], 4, 7),
            ([9], 3, 0),
            ([1, 2, 3], 1, 1),
            ([1, 2, 3], 2, 2),
            ([1, 2, 3], 3, 4),
            ([2, 3], 1, 0),
            ([1], 3, 1),
            ([1, 2], 4, 5),
            ([3, 2, 1], 4, 7),
            ([1, 2], 10, 89),
            ([1, 2, 3], 10, 274),
            ([2], 4, 1),
            ([5], 4, 0),
            ([1, 2], 1, 1),
            ([1, 2, 3], 5, 13),
        ],
    )
    def test_combination_sum4(self, nums: list[int], target: int, expected: int):
        result = run_combination_sum4(Solution, nums, target)
        assert_combination_sum4(result, expected)
