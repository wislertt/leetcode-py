import pytest

from leetcode_py import logged_test

from .helpers import assert_second_minimum, run_second_minimum
from .solution import Solution


class TestSecondMinimumTimeToReachDestination:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, time, change, expected",
        [
            (5, [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5]], 3, 5, 13),
            (2, [[1, 2]], 3, 2, 11),
            (2, [[1, 2]], 3, 3, 15),
            (2, [[1, 2]], 1, 1, 5),
            (2, [[1, 2]], 1000, 1000, 5000),
            (3, [[1, 2], [2, 3]], 1, 1, 7),
            (3, [[1, 2], [2, 3]], 2, 4, 12),
            (3, [[1, 2], [2, 3]], 1000, 1000, 7000),
            (3, [[1, 2], [1, 3], [2, 3]], 2, 4, 4),
            (3, [[1, 2], [1, 3], [2, 3]], 5, 5, 15),
            (4, [[1, 2], [1, 3], [2, 4], [3, 4]], 1, 2, 6),
            (4, [[1, 2], [1, 3], [2, 4], [3, 4]], 3, 3, 21),
            (4, [[1, 2], [1, 3], [1, 4]], 5, 5, 25),
            (4, [[1, 2], [1, 3], [1, 4]], 2, 3, 8),
            (5, [[1, 2], [2, 3], [3, 4], [4, 5], [2, 4]], 3, 2, 15),
            (5, [[1, 2], [1, 3], [2, 4], [3, 5], [4, 5]], 1, 3, 3),
            (6, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [3, 6]], 2, 5, 14),
            (8, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [3, 6]], 2, 3, 20),
        ],
    )
    def test_second_minimum(
        self, n: int, edges: list[list[int]], time: int, change: int, expected: int
    ):
        result = run_second_minimum(Solution, n, edges, time, change)
        assert_second_minimum(result, expected)
