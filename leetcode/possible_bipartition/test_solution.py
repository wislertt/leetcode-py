import pytest

from leetcode_py import logged_test

from .helpers import assert_possible_bipartition, run_possible_bipartition
from .solution import Solution


class TestPossibleBipartition:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, dislikes, expected",
        [
            (4, [[1, 2], [1, 3], [2, 4]], True),
            (3, [[1, 2], [1, 3], [2, 3]], False),
            (1, [], True),
            (2, [], True),
            (2, [[1, 2]], True),
            (3, [], True),
            (5, [[1, 2], [2, 3], [3, 4], [4, 5]], True),
            (4, [[1, 2], [2, 3], [3, 4], [1, 4]], True),
            (5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], False),
            (6, [[1, 2], [3, 4], [5, 6]], True),
            (6, [[1, 2], [3, 4], [4, 5], [3, 5]], False),
            (6, [[1, 2], [2, 3], [1, 3], [4, 5], [5, 6], [4, 6]], False),
            (8, [[1, 2], [1, 3], [3, 4], [2, 5], [5, 6], [6, 7], [7, 8]], True),
            (7, [[1, 3], [3, 5], [1, 5], [2, 4], [4, 6]], False),
            (6, [[1, 2], [1, 4], [1, 6], [3, 6]], True),
            (8, [[1, 2], [3, 8], [7, 8]], True),
            (6, [[1, 6], [2, 5], [3, 6], [5, 6]], True),
            (6, [[3, 5], [4, 5], [3, 4]], False),
            (6, [[1, 5], [1, 4], [4, 5]], False),
            (8, [[5, 8], [5, 6], [6, 8]], False),
        ],
    )
    def test_possible_bipartition(self, n: int, dislikes: list[list[int]], expected: bool):
        result = run_possible_bipartition(Solution, n, dislikes)
        assert_possible_bipartition(result, expected)
