import pytest

from leetcode_py import logged_test

from .helpers import assert_find_the_city, run_find_the_city
from .solution import Solution


class TestFindTheCityWithTheSmallestNumberOfNeighborsAtAThresholdDistance:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, distance_threshold, expected",
        [
            [4, [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], 4, 3],
            [5, [[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]], 2, 0],
            [2, [[0, 1, 1]], 1, 1],
            [2, [[0, 1, 1]], 10, 1],
            [3, [[0, 1, 2], [1, 2, 2]], 2, 2],
            [3, [[0, 1, 2], [1, 2, 2]], 5, 2],
            [4, [[0, 1, 1], [1, 2, 1], [2, 3, 1]], 1, 3],
            [4, [[0, 1, 1], [1, 2, 1], [2, 3, 1]], 10, 3],
            [6, [[0, 1, 4], [1, 2, 3], [2, 3, 5], [3, 4, 2], [4, 5, 1]], 3, 0],
            [
                5,
                [
                    [2, 4, 5],
                    [1, 3, 3],
                    [1, 2, 3],
                    [1, 4, 4],
                    [0, 3, 1],
                    [0, 4, 4],
                    [3, 4, 1],
                    [2, 3, 4],
                ],
                6,
                4,
            ],
            [4, [[1, 3, 1]], 4, 2],
            [
                5,
                [
                    [1, 2, 4],
                    [2, 3, 5],
                    [1, 3, 4],
                    [2, 4, 5],
                    [0, 2, 3],
                    [0, 1, 3],
                    [3, 4, 1],
                    [0, 4, 4],
                    [0, 3, 3],
                ],
                8,
                4,
            ],
            [3, [[0, 1, 5], [1, 2, 1]], 5, 2],
            [4, [[0, 3, 2], [2, 3, 1], [0, 1, 3]], 1, 1],
            [4, [[1, 2, 5], [0, 3, 5]], 1, 3],
            [6, [[4, 5, 5]], 8, 3],
        ],
    )
    def test_find_the_city(
        self, n: int, edges: list[list[int]], distance_threshold: int, expected: int
    ):
        result = run_find_the_city(Solution, n, edges, distance_threshold)
        assert_find_the_city(result, expected)
