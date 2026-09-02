import pytest

from leetcode_py import logged_test

from .helpers import assert_leftmost_building_queries, run_leftmost_building_queries
from .solution import Solution


class TestFindBuildingWhereAliceAndBobCanMeet:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "heights, queries, expected",
        [
            ([6, 4, 8, 5, 2, 7], [[0, 1], [0, 3], [2, 4], [3, 4], [2, 2]], [2, 5, -1, 5, 2]),
            ([5, 3, 8, 2, 6, 1, 4, 6], [[0, 7], [3, 5], [5, 2], [3, 0], [1, 6]], [7, 6, -1, 4, 6]),
            ([1], [[0, 0]], [0]),
            ([3, 3], [[0, 1]], [-1]),
            ([3, 3], [[1, 0], [0, 1]], [-1, -1]),
            ([1, 2], [[0, 1], [1, 0]], [1, 1]),
            ([2, 2, 2, 2], [[0, 1], [0, 3], [2, 2]], [-1, -1, 2]),
            ([1, 2, 3, 4, 5], [[0, 1], [0, 4], [2, 3]], [1, 4, 3]),
            ([5, 4, 3, 2, 1], [[0, 1], [0, 4]], [-1, -1]),
            ([7, 1, 9, 5, 3, 8], [[5, 2]], [-1]),
            ([2, 9], [[0, 1], [1, 1]], [1, 1]),
            ([3, 6, 5, 1], [[2, 1]], [-1]),
            ([7, 1, 9, 4], [[1, 1], [0, 1], [2, 0]], [1, 2, 2]),
            ([6, 6, 6, 1, 6, 6], [[0, 0], [0, 1], [4, 5]], [0, -1, -1]),
            ([5, 2, 8], [[0, 2]], [2]),
            ([2, 6, 2], [[1, 1]], [1]),
            ([4, 8, 9, 7], [[2, 2]], [2]),
            ([8, 2], [[1, 0], [0, 0]], [-1, 0]),
        ],
    )
    def test_leftmost_building_queries(
        self, heights: list[int], queries: list[list[int]], expected: list[int]
    ):
        result = run_leftmost_building_queries(Solution, heights, queries)
        assert_leftmost_building_queries(result, expected)
