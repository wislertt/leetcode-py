import pytest

from leetcode_py import logged_test

from .helpers import assert_last_stone_weight_ii, run_last_stone_weight_ii
from .solution import Solution


class TestLastStoneWeightII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "stones, expected",
        [
            ([2, 7, 4, 1, 8, 1], 1),
            ([31, 26, 33, 21, 40], 5),
            ([1], 1),
            ([2, 2], 0),
            ([1, 1], 0),
            ([1, 2], 1),
            ([10], 10),
            ([1, 2, 3], 0),
            ([1, 2, 4], 1),
            ([100], 100),
            ([1, 1, 1, 1], 0),
            ([2, 4, 8], 2),
            ([5, 5, 5], 5),
            ([3, 3, 3, 3], 0),
            ([9, 9, 9], 9),
            ([1, 2, 3, 4, 5], 1),
            ([10, 10, 10, 10], 0),
            ([7, 7, 7, 7, 7], 7),
        ],
    )
    def test_last_stone_weight_ii(self, stones: list[int], expected: int):
        result = run_last_stone_weight_ii(Solution, stones)
        assert_last_stone_weight_ii(result, expected)
