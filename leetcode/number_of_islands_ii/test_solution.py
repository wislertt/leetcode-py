import pytest

from leetcode_py import logged_test

from .helpers import assert_num_islands2, run_num_islands2
from .solution import Solution


class TestNumberOfIslandsII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "m, n, positions, expected",
        [
            (3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]], [1, 1, 2, 3]),
            (1, 1, [[0, 0]], [1]),
            (1, 2, [[0, 0], [0, 0], [0, 1]], [1, 1, 1]),
            (2, 2, [[0, 0], [0, 1], [1, 0], [1, 1]], [1, 1, 1, 1]),
            (3, 3, [[0, 0], [1, 1], [2, 2], [1, 0], [0, 1]], [1, 2, 3, 2, 2]),
            (1, 5, [[0, 2], [0, 1], [0, 3], [0, 0], [0, 4]], [1, 1, 1, 1, 1]),
            (4, 1, [[3, 0], [2, 0], [1, 0], [0, 0]], [1, 1, 1, 1]),
            (3, 3, [[0, 0], [0, 2], [2, 0], [2, 2], [1, 1], [0, 1], [1, 0]], [1, 2, 3, 4, 5, 3, 2]),
            (2, 3, [[0, 0], [1, 1], [0, 2], [1, 2], [0, 1], [1, 0]], [1, 2, 3, 2, 1, 1]),
            (2, 2, [[0, 0], [1, 1], [0, 0], [1, 0], [0, 1]], [1, 2, 2, 1, 1]),
            (
                3,
                4,
                [[2, 3], [0, 0], [2, 0], [1, 1], [0, 1], [1, 3], [1, 2], [0, 3]],
                [1, 2, 3, 4, 3, 3, 2, 2],
            ),
            (1, 1, [[0, 0], [0, 0], [0, 0]], [1, 1, 1]),
            (3, 3, [[1, 1], [0, 1], [2, 1], [1, 0], [1, 2]], [1, 1, 1, 1, 1]),
            (
                2,
                4,
                [[0, 3], [1, 3], [0, 0], [1, 0], [0, 2], [1, 2], [1, 1], [0, 1]],
                [1, 1, 2, 2, 2, 2, 1, 1],
            ),
            (3, 2, [[2, 1], [0, 0], [2, 0], [1, 1], [0, 1], [1, 0]], [1, 2, 2, 2, 1, 1]),
        ],
    )
    def test_num_islands2(self, m: int, n: int, positions: list[list[int]], expected: list[int]):
        result = run_num_islands2(Solution, m, n, positions)
        assert_num_islands2(result, expected)
