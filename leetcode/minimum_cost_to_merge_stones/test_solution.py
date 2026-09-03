import pytest

from leetcode_py import logged_test

from .helpers import assert_merge_stones, run_merge_stones
from .solution import Solution


class TestMinimumCostToMergeStones:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "stones, k, expected",
        [
            ([3, 2, 4, 1], 2, 20),
            ([3, 2, 4, 1], 3, -1),
            ([3, 5, 1, 2, 6], 3, 25),
            ([1], 2, 0),
            ([100], 30, 0),
            ([1, 2], 2, 3),
            ([1, 2, 3], 2, 9),
            ([7, 7, 7, 7, 7], 5, 35),
            ([10, 10, 10, 10, 10], 2, 120),
            ([1, 2, 3, 4, 5, 6], 3, -1),
            ([6, 4, 4, 6], 2, 40),
            ([1, 2, 3, 4, 5, 6, 7], 3, 49),
            ([95, 10, 30], 3, 135),
            ([51, 46, 9, 60, 22, 69, 56, 17, 29, 86], 2, 1432),
            ([87, 63, 26, 88, 86, 47, 30], 4, 674),
            ([6, 87, 96, 63, 19, 60, 92, 91, 54, 89, 26], 3, 1508),
            ([60, 92, 99, 28], 6, -1),
            ([70, 23, 90, 91, 14, 33, 21, 37, 12, 1, 41, 3, 82, 33, 38, 67, 100], 4, -1),
        ],
    )
    def test_merge_stones(self, stones: list[int], k: int, expected: int):
        result = run_merge_stones(Solution, stones, k)
        assert_merge_stones(result, expected)
