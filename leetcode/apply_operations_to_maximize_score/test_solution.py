import pytest

from leetcode_py import logged_test

from .helpers import assert_maximum_score, run_maximum_score
from .solution import Solution


class TestApplyOperationsToMaximizeScore:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "nums, k, expected",
        [
            ([8, 3, 9, 3, 8], 2, 81),
            ([19, 12, 14, 6, 10, 18], 3, 4788),
            ([1], 1, 1),
            ([2], 1, 2),
            ([5, 5], 1, 5),
            ([5, 5], 3, 125),
            ([1, 1, 1], 6, 1),
            ([2, 4, 8], 3, 128),
            ([6, 10, 15], 4, 9000),
            ([30], 1, 30),
            ([7, 3, 5, 2], 5, 12005),
            ([4, 9, 25, 49], 10, 715359965),
            ([12, 18, 6, 9], 7, 120932352),
            ([100000, 99999], 2, 999899937),
            ([2, 3, 5, 7, 11], 15, 174636000),
            ([18, 35, 27, 12, 7, 13, 9], 7, 633171532),
            ([17, 21, 25, 39, 15, 3, 13], 28, 677332730),
            ([23, 11, 28, 16, 5], 11, 160180811),
        ],
    )
    def test_maximum_score(self, nums: list[int], k: int, expected: int):
        result = run_maximum_score(Solution, nums, k)
        assert_maximum_score(result, expected)
