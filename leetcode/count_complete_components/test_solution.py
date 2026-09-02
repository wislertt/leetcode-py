import pytest

from leetcode_py import logged_test

from .helpers import assert_count_complete_components, run_count_complete_components
from .solution import Solution


class TestTestCountCompleteComponents:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, expected",
        [
            (1, [], 1),
            (2, [], 2),
            (2, [[0, 1]], 1),
            (3, [], 3),
            (3, [[0, 1]], 2),
            (3, [[0, 1], [1, 2], [0, 2]], 1),
            (4, [[0, 1], [2, 3]], 2),
            (4, [[0, 1], [1, 2], [2, 3]], 0),
            (6, [[0, 1], [0, 2], [1, 2], [3, 4]], 3),
            (6, [[0, 1], [0, 2], [1, 2], [3, 4], [3, 5]], 1),
            (5, [[0, 1], [0, 2], [0, 3], [0, 4]], 0),
            (4, [[0, 1], [0, 2], [0, 3], [1, 2], [1, 3], [2, 3]], 1),
            (5, [[0, 1], [0, 2], [1, 2], [3, 4]], 2),
            (5, [[0, 1], [2, 3]], 3),
            (3, [[0, 1], [0, 2]], 0),
            (
                6,
                [[0, 5], [0, 3], [2, 5], [0, 2], [4, 5], [3, 4], [1, 3], [2, 4], [1, 2], [0, 4]],
                0,
            ),
            (5, [[1, 3], [2, 4], [0, 2], [1, 2], [0, 4], [3, 4], [2, 3], [1, 4], [0, 1]], 0),
            (5, [[1, 3], [1, 2], [0, 2], [0, 1], [1, 4], [0, 3], [2, 3], [2, 4]], 0),
            (
                6,
                [[0, 1], [0, 4], [2, 5], [3, 4], [1, 3], [0, 3], [2, 4], [4, 5], [0, 2], [3, 5]],
                0,
            ),
            (6, [[1, 3]], 5),
        ],
    )
    def test_count_complete_components(self, n: int, edges: list[list[int]], expected: int):
        result = run_count_complete_components(Solution, n, edges)
        assert_count_complete_components(result, expected)
