import pytest

from leetcode_py import logged_test

from .helpers import assert_magnificent_sets, run_magnificent_sets
from .solution import Solution


class TestDivideNodesIntoTheMaximumNumberOfGroups:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, expected",
        [
            (6, [[1, 2], [1, 4], [1, 5], [2, 6], [2, 3], [4, 6]], 4),
            (3, [[1, 2], [2, 3], [3, 1]], -1),
            (2, [[1, 2]], 2),
            (4, [[1, 2], [2, 3], [3, 4]], 4),
            (5, [[1, 2], [3, 4]], 5),
            (4, [[1, 2], [1, 3], [1, 4]], 3),
            (4, [[1, 2], [2, 3], [3, 4], [4, 1]], 3),
            (5, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 1]], -1),
            (6, [[1, 2], [3, 4], [5, 6]], 6),
            (7, [[1, 2], [2, 3], [3, 1], [4, 5], [5, 6], [6, 7]], -1),
            (5, [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5]], 4),
            (10, [[1, 3], [3, 5], [5, 2], [2, 4], [4, 6], [6, 7], [7, 8]], 10),
            (200, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [7, 8], [8, 9]], 200),
            (500, [[250, 251]], 500),
            (20, [[6, 3], [11, 6], [17, 20], [16, 14], [9, 12], [10, 14]], 20),
            (30, [[8, 18], [7, 22], [1, 28], [1, 7], [22, 6], [24, 14], [17, 11]], 30),
            (50, [[33, 32], [6, 40], [18, 26], [29, 28], [33, 29]], 50),
            (40, [[3, 9], [13, 6], [28, 4], [30, 15], [18, 10], [5, 19]], 40),
            (25, [[19, 23], [1, 9], [13, 8], [16, 6], [8, 16], [10, 9], [22, 1]], 25),
        ],
    )
    def test_magnificent_sets(self, n: int, edges: list[list[int]], expected: int):
        result = run_magnificent_sets(Solution, n, edges)
        assert_magnificent_sets(result, expected)
