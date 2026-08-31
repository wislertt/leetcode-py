import pytest

from leetcode_py import logged_test

from .helpers import assert_delete_and_earn, run_delete_and_earn
from .solution import Solution


class TestDeleteAndEarn:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, expected",
        [
            ([3, 4, 2], 6),
            ([2, 2, 3, 3, 3, 4], 9),
            ([1], 1),
            ([1, 1], 2),
            ([1, 2], 2),
            ([2, 1], 2),
            ([1, 1, 1], 3),
            ([8, 7, 6, 5], 14),
            ([1, 2, 3, 4, 5], 9),
            ([10, 10, 10], 30),
            ([4, 4, 4, 4], 16),
            ([9999, 9999], 19998),
            ([5, 5, 6, 6, 7], 17),
            ([3, 1, 3, 1, 3], 11),
            ([12, 32, 93, 17, 100, 72, 40, 82, 91, 100], 639),
            ([84, 69, 76, 88, 68, 79, 9, 45, 74, 44], 524),
        ],
    )
    def test_delete_and_earn(self, nums: list[int], expected: int):
        result = run_delete_and_earn(Solution, nums)
        assert_delete_and_earn(result, expected)
