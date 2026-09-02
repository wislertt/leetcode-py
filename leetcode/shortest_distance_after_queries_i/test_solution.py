import pytest

from leetcode_py import logged_test

from .helpers import assert_shortest_distance_after_queries, run_shortest_distance_after_queries
from .solution import Solution


class TestShortestDistanceAfterRoadAdditionQueriesI:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, queries, expected",
        [
            (5, [[2, 4], [0, 2], [0, 4]], [3, 2, 1]),
            (4, [[0, 3], [0, 2]], [1, 1]),
            (3, [[0, 2]], [1]),
            (5, [[1, 3]], [3]),
            (6, [[0, 3], [3, 5], [0, 5]], [3, 2, 1]),
            (7, [[0, 5], [2, 4]], [2, 2]),
            (10, [[0, 9]], [1]),
            (8, [[0, 4], [4, 7], [2, 6]], [4, 2, 2]),
            (6, [[0, 2], [2, 5], [1, 4]], [4, 2, 2]),
            (9, [[1, 4], [0, 3], [4, 8]], [6, 6, 3]),
            (5, [[0, 3], [1, 4], [0, 4]], [2, 2, 1]),
            (12, [[0, 6], [6, 11], [0, 11]], [6, 2, 1]),
            (4, [[0, 2]], [2]),
            (7, [[0, 4], [3, 6], [1, 5]], [3, 3, 3]),
            (6, [[1, 5], [0, 2]], [2, 2]),
            (5, [[0, 2], [2, 4], [0, 4]], [3, 2, 1]),
            (11, [[5, 8], [0, 5], [8, 10]], [8, 4, 3]),
            (13, [[0, 7], [7, 12], [3, 9]], [6, 2, 2]),
            (5, [[0, 4]], [1]),
            (9, [[0, 6], [3, 6]], [3, 3]),
            (9, [[3, 8]], [4]),
            (5, [[0, 4], [1, 4], [2, 4]], [1, 1, 1]),
        ],
    )
    def test_shortest_distance_after_queries(
        self, n: int, queries: list[list[int]], expected: list[int]
    ):
        result = run_shortest_distance_after_queries(Solution, n, queries)
        assert_shortest_distance_after_queries(result, expected)
