import pytest

from leetcode_py import logged_test

from .helpers import assert_two_sum_bsts, run_two_sum_bsts
from .solution import Solution


class TestTwoSumBSTs:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "root1_list, root2_list, target, expected",
        [
            ([2, 1, 4], [1, 0, 3], 5, True),
            ([0, -10, 10], [5, 1, 7, 0, 2], 18, False),
            ([2, 1, 4], [1, 0, 3], 4, True),
            ([2, 1, 4], [1, 0, 3], 3, True),
            ([2, 1, 4], [1, 0, 3], 8, False),
            ([1], [1], 2, True),
            ([1], [1], 3, False),
            ([-5, -10, -3], [-6, -10, -4], -14, True),
            ([1000000000], [1000000000], 2000000000, True),
            ([-1000000000], [-1000000000], -2000000000, True),
            ([0, -10, 10], [5, 1, 7, 0, 2], 12, True),
            ([5, 3, 8, 1, 4, 7, 9], [10, 6, 15, 3, 8, 11, 18], 24, True),
            ([3, None, 4], [2, None, 3], 6, True),
            ([10, 5, 15, 2, 7], [5, 1, 8], 15, True),
            ([23, -45, None, -49], [23, -5, None, -11, 20], 46, True),
            ([14, None, 33, None, 41], [34, -55, None, None, 3, -2, 17], 31, True),
            ([12, -1, 23, -49], [-35, -36, 43, None, None, 29, None, 24], -10, False),
            ([-5, -46, 20, -56, None, 18, 40], [-10, -18, 36, -59, -11], -101, False),
        ],
    )
    def test_two_sum_bsts(
        self,
        root1_list: list[int | None],
        root2_list: list[int | None],
        target: int,
        expected: bool,
    ):
        result = run_two_sum_bsts(Solution, root1_list, root2_list, target)
        assert_two_sum_bsts(result, expected)
