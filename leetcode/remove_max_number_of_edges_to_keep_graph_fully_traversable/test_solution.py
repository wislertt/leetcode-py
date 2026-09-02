import pytest

from leetcode_py import logged_test

from .helpers import assert_max_num_edges_to_remove, run_max_num_edges_to_remove
from .solution import Solution


class TestRemoveMaxNumberOfEdgesToKeepGraphFullyTraversable:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, expected",
        [
            (4, [[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]], 2),
            (4, [[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]], 0),
            (4, [[3, 2, 3], [1, 1, 2], [2, 3, 4]], -1),
            (2, [[1, 1, 2], [2, 1, 2]], 0),
            (2, [[3, 1, 2]], 0),
            (2, [[1, 1, 2]], -1),
            (2, [[2, 1, 2]], -1),
            (3, [[1, 1, 2], [1, 2, 3], [2, 1, 3], [2, 1, 2], [3, 2, 3]], 2),
            (4, [[1, 1, 2], [2, 3, 4]], -1),
            (4, [[3, 1, 2], [3, 3, 4], [3, 1, 3], [3, 2, 4]], 1),
            (5, [[1, 1, 2], [2, 1, 2], [1, 2, 3], [2, 2, 3], [1, 3, 4], [2, 3, 4], [3, 4, 5]], 0),
            (3, [[3, 1, 2], [1, 1, 2]], -1),
            (3, [[1, 1, 2], [2, 1, 3], [3, 2, 3], [3, 1, 3], [3, 1, 2]], 3),
            (
                4,
                [
                    [2, 1, 3],
                    [2, 2, 3],
                    [2, 1, 4],
                    [3, 2, 4],
                    [1, 1, 4],
                    [3, 1, 2],
                    [2, 3, 4],
                    [3, 1, 4],
                    [1, 2, 3],
                ],
                5,
            ),
            (3, [[2, 2, 3], [3, 1, 3], [3, 2, 3], [1, 1, 2], [2, 1, 3], [1, 2, 3]], 4),
            (3, [[1, 1, 3], [2, 1, 3], [2, 1, 2], [2, 2, 3], [3, 1, 3], [3, 1, 2], [1, 1, 2]], 5),
        ],
    )
    def test_max_num_edges_to_remove(self, n: int, edges: list[list[int]], expected: int):
        result = run_max_num_edges_to_remove(Solution, n, edges)
        assert_max_num_edges_to_remove(result, expected)
