import pytest

from leetcode_py import logged_test

from .helpers import assert_find_champion, run_find_champion
from .solution import Solution


class TestFindChampionII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, expected",
        [
            (3, [[0, 1], [1, 2]], 0),
            (4, [[0, 2], [1, 3], [1, 2]], -1),
            (1, [], 0),
            (2, [], -1),
            (2, [[0, 1]], 0),
            (2, [[1, 0]], 1),
            (3, [[0, 1], [0, 2]], 0),
            (3, [[1, 0], [2, 0]], -1),
            (3, [], -1),
            (4, [[0, 1], [1, 2], [2, 3]], 0),
            (5, [[0, 1], [0, 2], [0, 3], [0, 4]], 0),
            (4, [[1, 0], [2, 0], [3, 0]], -1),
            (3, [[0, 1], [2, 1]], -1),
            (4, [[3, 0], [3, 1], [3, 2]], 3),
            (5, [[1, 0], [2, 0], [3, 1], [4, 1]], -1),
            (6, [[0, 1], [0, 2], [1, 3], [2, 3], [3, 4], [4, 5]], 0),
            (7, [[1, 3], [3, 4], [1, 4], [6, 2], [0, 4], [6, 0]], -1),
            (8, [[2, 7], [1, 2], [5, 0], [3, 7]], -1),
            (4, [[1, 2], [3, 1]], -1),
            (8, [[6, 7], [4, 0], [3, 5], [6, 5], [4, 3], [1, 5], [7, 0]], -1),
        ],
    )
    def test_find_champion(self, n: int, edges: list[list[int]], expected: int):
        result = run_find_champion(Solution, n, edges)
        assert_find_champion(result, expected)
