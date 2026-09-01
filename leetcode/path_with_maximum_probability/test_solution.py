import pytest

from leetcode_py import logged_test

from .helpers import assert_max_probability, run_max_probability
from .solution import Solution


class TestPathWithMaximumProbability:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, edges, succ_prob, start_node, end_node, expected",
        [
            (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2, 0.25),
            (3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2, 0.3),
            (3, [[0, 1]], [0.5], 0, 2, 0.0),
            (2, [[0, 1]], [0.0], 0, 1, 0.0),
            (2, [[1, 0]], [0.75], 0, 1, 0.75),
            (4, [[0, 1], [1, 2], [2, 3]], [1.0, 1.0, 1.0], 0, 3, 1.0),
            (3, [[0, 1], [0, 2], [1, 2]], [0.5, 0.5, 0.5], 0, 2, 0.5),
            (5, [[0, 1], [1, 2], [0, 2], [2, 3], [3, 4]], [0.9, 0.9, 0.5, 0.8, 0.9], 0, 4, 0.5832),
            (4, [[0, 1], [0, 2], [1, 2], [2, 3]], [0.1, 0.1, 0.9, 0.5], 0, 3, 0.05),
            (5, [[0, 1], [2, 3], [3, 4]], [0.9, 0.9, 0.9], 0, 4, 0.0),
            (
                6,
                [[0, 1], [1, 3], [0, 2], [2, 3], [3, 4], [4, 5]],
                [0.4, 0.9, 0.7, 0.6, 0.5, 0.2],
                0,
                5,
                0.042,
            ),
            (4, [[0, 3], [1, 2], [2, 3]], [0.0, 0.5, 0.9], 0, 3, 0.0),
            (5, [], [], 4, 3, 0.0),
            (2, [[0, 1]], [0.5], 0, 1, 0.5),
            (4, [[1, 3], [1, 2], [0, 1]], [0.1, 0.1, 0.25], 0, 2, 0.025),
            (
                6,
                [[2, 4], [2, 3], [0, 5], [1, 4], [1, 2], [1, 3]],
                [0.5349008200257962, 0.5, 0.25, 0.3457061636606624, 1.0, 1.0],
                3,
                2,
                1.0,
            ),
        ],
    )
    def test_max_probability(
        self,
        n: int,
        edges: list[list[int]],
        succ_prob: list[float],
        start_node: int,
        end_node: int,
        expected: float,
    ):
        result = run_max_probability(Solution, n, edges, succ_prob, start_node, end_node)
        assert_max_probability(result, expected)
