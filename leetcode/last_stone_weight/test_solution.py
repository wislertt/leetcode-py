import pytest

from leetcode_py import logged_test

from .helpers import assert_last_stone_weight, run_last_stone_weight
from .solution import Solution


class TestLastStoneWeight:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "stones, expected",
        [
            ([2, 7, 4, 1, 8, 1], 1),
            ([1], 1),
            ([2, 2], 0),
            ([3, 1], 2),
            ([2, 2, 2], 2),
            ([1, 1, 1, 1], 0),
            ([9, 3, 2, 10], 0),
            ([10], 10),
            ([1000], 1000),
            ([1000, 1000], 0),
            ([5, 5, 5], 5),
            ([31, 26, 33, 21, 40], 9),
            ([7, 6, 7, 6, 9], 3),
            ([1, 1000, 2, 999], 0),
            ([4, 4, 4, 4, 4], 4),
            ([9, 8, 7, 6, 5, 4], 1),
            ([12, 4, 9, 11, 5], 1),
        ],
    )
    def test_last_stone_weight(self, stones: list[int], expected: int):
        result = run_last_stone_weight(Solution, stones)
        assert_last_stone_weight(result, expected)
