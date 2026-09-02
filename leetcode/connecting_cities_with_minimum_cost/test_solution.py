import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_cost, run_minimum_cost
from .solution import Solution


class TestConnectingCitiesWithMinimumCost:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, connections, expected",
        [
            (3, [[1, 2, 5], [1, 3, 6], [2, 3, 1]], 6),
            (4, [[1, 2, 3], [3, 4, 4]], -1),
            (2, [[1, 2, 5]], 5),
            (2, [[1, 2, 0]], 0),
            (4, [[1, 2, 1], [2, 3, 2], [3, 4, 3]], 6),
            (3, [[1, 2, 1], [1, 2, 1]], -1),
            (4, [[1, 2, 3], [2, 3, 1], [3, 1, 2], [3, 4, 5]], 8),
            (4, [[1, 2, 1], [1, 2, 1], [3, 4, 3]], -1),
            (5, [[1, 2, 5], [2, 3, 4], [3, 4, 3], [4, 5, 2], [1, 5, 10]], 14),
            (5, [[1, 2, 1], [3, 4, 1], [4, 5, 1]], -1),
            (6, [[1, 2, 7], [2, 3, 5], [3, 4, 9], [4, 5, 6], [5, 6, 2], [6, 1, 4]], 24),
            (6, [[1, 2, 7], [2, 3, 5], [3, 4, 9], [4, 5, 6], [5, 6, 2]], 29),
            (4, [[2, 3, 1], [3, 4, 2], [1, 4, 5], [1, 2, 8]], 8),
            (3, [[1, 3, 100000], [2, 3, 100000]], 200000),
            (
                6,
                [
                    [1, 2, 61275],
                    [2, 3, 23823],
                    [3, 4, 63143],
                    [4, 5, 72032],
                    [5, 6, 72378],
                    [2, 3, 62847],
                    [3, 5, 1079],
                ],
                221698,
            ),
            (
                5,
                [
                    [5, 2, 89663],
                    [5, 1, 89859],
                    [5, 3, 44083],
                    [5, 3, 81668],
                    [3, 4, 93320],
                    [3, 4, 16272],
                ],
                239877,
            ),
        ],
    )
    def test_minimum_cost(self, n: int, connections: list[list[int]], expected: int):
        result = run_minimum_cost(Solution, n, connections)
        assert_minimum_cost(result, expected)
