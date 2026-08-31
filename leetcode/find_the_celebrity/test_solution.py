import pytest

from leetcode_py import logged_test

from .helpers import assert_find_celebrity, run_find_celebrity
from .solution import Solution


class TestFindTheCelebrity:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "graph, expected",
        [
            ([[1, 1, 0], [0, 1, 0], [1, 1, 1]], 1),
            ([[1, 0, 1], [1, 1, 0], [0, 1, 1]], -1),
            ([[1, 0], [0, 1]], -1),
            ([[1, 1], [0, 1]], 1),
            ([[1, 0], [1, 1]], 0),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], -1),
            ([[1, 0, 0], [1, 1, 0], [1, 1, 1]], 0),
            ([[1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 1, 0], [1, 1, 1, 1]], -1),
            ([[1, 1, 1, 1], [0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 1, 1]], 1),
            ([[1, 1], [1, 1]], -1),
            ([[1, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 1]], -1),
            ([[1, 0, 1, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]], -1),
            ([[1, 1, 1], [0, 1, 0], [0, 1, 1]], 1),
            ([[1, 0, 0], [1, 1, 0], [1, 0, 1]], 0),
        ],
    )
    def test_find_celebrity(self, graph: list[list[int]], expected: int):
        result = run_find_celebrity(Solution, graph)
        assert_find_celebrity(result, expected)
