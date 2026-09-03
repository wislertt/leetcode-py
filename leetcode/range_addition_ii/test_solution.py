import pytest

from leetcode_py import logged_test

from .helpers import assert_max_count, run_max_count
from .solution import Solution


class TestRangeAdditionII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "m, n, ops, expected",
        [
            (3, 3, [[2, 2], [3, 3]], 4),
            (
                3,
                3,
                [
                    [2, 2],
                    [3, 3],
                    [3, 3],
                    [3, 3],
                    [2, 2],
                    [3, 3],
                    [3, 3],
                    [3, 3],
                    [2, 2],
                    [3, 3],
                    [3, 3],
                    [3, 3],
                ],
                4,
            ),
            (3, 3, [], 9),
            (1, 1, [], 1),
            (1, 1, [[1, 1]], 1),
            (4, 4, [[4, 4]], 16),
            (5, 5, [[2, 3], [3, 2]], 4),
            (10, 10, [[1, 1]], 1),
            (100, 100, [], 10000),
            (3, 4, [[2, 2], [3, 3]], 4),
            (40000, 40000, [[40000, 40000]], 1600000000),
            (5, 5, [[5, 1], [1, 5], [3, 3]], 1),
            (7, 2, [[3, 2], [7, 1]], 3),
            (2, 8, [[2, 5]], 10),
            (6, 6, [[6, 6], [1, 1], [6, 6]], 1),
            (9, 9, [[4, 7], [3, 9], [9, 3]], 9),
            (10000, 10000, [], 100000000),
            (3, 3, [[3, 3], [2, 2], [3, 3]], 4),
        ],
    )
    def test_max_count(self, m: int, n: int, ops: list[list[int]], expected: int):
        result = run_max_count(Solution, m, n, ops)
        assert_max_count(result, expected)
