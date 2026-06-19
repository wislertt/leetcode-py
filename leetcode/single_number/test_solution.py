import pytest

from leetcode_py import logged_test

from .helpers import assert_single_number, run_single_number
from .solution import Solution


class TestSingleNumber:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([2, 2, 1], 1),
            ([4, 1, 2, 1, 2], 4),
            ([1], 1),
            ([1, 1, 2], 2),
            ([-1, -1, -2], -2),
            ([0, 0, 1], 1),
            ([1, 2, 1, 2, 3], 3),
            ([10], 10),
            ([-3, -3, 5], 5),
            ([0, 1, 0], 1),
            ([100, 99, 100], 99),
            ([2, 2, 3, 3, 5], 5),
            ([6], 6),
        ],
    )
    def test_single_number(self, nums: list[int], expected: int):
        result = run_single_number(Solution, nums)
        assert_single_number(result, expected)
