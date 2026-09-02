import pytest

from leetcode_py import logged_test

from .helpers import assert_min_score, run_min_score
from .solution import Solution


class TestMinimumScoreOfAPathBetweenTwoCities:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, roads, expected",
        [
            (4, [[1, 2, 9], [2, 3, 6], [2, 4, 5], [1, 4, 7]], 5),
            (4, [[1, 2, 2], [1, 3, 4], [3, 4, 7]], 2),
            (2, [[1, 2, 3]], 3),
            (3, [[1, 2, 1], [2, 3, 10]], 1),
            (4, [[2, 1, 7], [3, 4, 1], [2, 3, 5], [2, 4, 9], [1, 4, 3]], 1),
            (5, [[1, 2, 4], [1, 3, 9], [3, 4, 2], [2, 5, 8], [4, 5, 1]], 1),
            (5, [[1, 2, 5], [2, 3, 3], [4, 5, 100], [3, 4, 50]], 3),
            (3, [[1, 2, 5], [2, 3, 7], [3, 1, 6]], 5),
            (2, [[1, 2, 10000]], 10000),
            (6, [[1, 2, 9], [1, 3, 1], [3, 4, 9], [4, 5, 9], [5, 6, 9]], 1),
            (6, [[1, 2, 7], [2, 3, 7], [3, 4, 7], [5, 6, 1], [4, 5, 9]], 1),
            (4, [[1, 2, 3], [2, 3, 3], [3, 4, 3]], 3),
            (5, [[2, 3, 1], [3, 4, 1], [4, 5, 1], [1, 5, 6]], 1),
            (4, [[1, 2, 6], [3, 4, 1], [2, 3, 6]], 1),
            (7, [[1, 2, 8], [2, 3, 8], [3, 1, 8], [3, 4, 6], [4, 5, 2], [5, 6, 2], [6, 7, 2]], 2),
            (6, [[1, 3, 5], [3, 5, 4], [5, 6, 9], [2, 6, 3], [2, 4, 3], [1, 4, 7]], 3),
        ],
    )
    def test_min_score(self, n: int, roads: list[list[int]], expected: int):
        result = run_min_score(Solution, n, roads)
        assert_min_score(result, expected)
