import pytest

from leetcode_py import logged_test

from .helpers import assert_find_relative_ranks, run_find_relative_ranks
from .solution import Solution


class TestRelativeRanks:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "score, expected",
        [
            ([5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),
            ([10, 3, 8, 9, 4], ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]),
            ([1], ["Gold Medal"]),
            ([0], ["Gold Medal"]),
            ([2, 1], ["Gold Medal", "Silver Medal"]),
            ([3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal"]),
            ([1, 2, 3], ["Bronze Medal", "Silver Medal", "Gold Medal"]),
            ([4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4"]),
            ([1000000, 0], ["Gold Medal", "Silver Medal"]),
            ([6, 5, 4, 3, 2, 1], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5", "6"]),
            ([7, 3, 9, 1], ["Silver Medal", "Bronze Medal", "Gold Medal", "4"]),
            ([50, 40, 30, 20, 10], ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]),
            ([12, 10, 1, 13, 37, 7], ["Bronze Medal", "4", "6", "Silver Medal", "Gold Medal", "5"]),
            ([1, 9, 35, 15, 21], ["5", "4", "Gold Medal", "Bronze Medal", "Silver Medal"]),
            ([23, 22, 9, 19, 39], ["Silver Medal", "Bronze Medal", "5", "4", "Gold Medal"]),
            ([17, 31, 30, 3, 39], ["4", "Silver Medal", "Bronze Medal", "5", "Gold Medal"]),
        ],
    )
    def test_find_relative_ranks(self, score: list[int], expected: list[str]):
        result = run_find_relative_ranks(Solution, score)
        assert_find_relative_ranks(result, expected)
