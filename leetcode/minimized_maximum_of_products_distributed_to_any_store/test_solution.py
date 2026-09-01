import pytest

from leetcode_py import logged_test

from .helpers import assert_minimized_maximum, run_minimized_maximum
from .solution import Solution


class TestMinimizedMaximumOfProductsDistributedToAnyStore:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, quantities, expected",
        [
            (6, [11, 6], 3),
            (7, [15, 10, 10], 5),
            (1, [100000], 100000),
            (1, [1], 1),
            (2, [1, 1], 1),
            (5, [1, 1, 1], 1),
            (3, [100], 34),
            (4, [11], 3),
            (2, [7, 7], 7),
            (5, [1, 1, 1, 1, 1], 1),
            (6, [12, 6], 3),
            (2, [100000, 100000], 100000),
            (10, [3, 3, 4], 1),
            (10, [10, 10, 10], 4),
            (4, [1, 2, 3, 4], 4),
            (5, [15, 10, 1], 8),
            (11, [11, 11, 11], 4),
            (9, [1, 1, 1, 1, 1, 1, 1, 1, 1], 1),
            (8, [3, 15, 16, 20, 11, 15], 15),
            (4, [7, 10, 9, 18], 18),
            (6, [11, 12, 1, 5, 3], 11),
            (3, [19], 7),
            (7, [15], 3),
            (8, [4, 11, 1, 9, 14], 7),
            (7, [16, 16, 8, 19, 14], 16),
            (4, [14, 15, 15, 4], 15),
            (4, [3], 1),
            (5, [18], 4),
            (6, [16], 3),
            (4, [1, 9], 3),
            (5, [2, 11], 3),
            (4, [1, 7], 3),
            (7, [18], 3),
            (4, [14, 11], 7),
            (4, [12, 12], 6),
            (5, [12], 3),
            (6, [8, 8, 5, 8, 17, 12], 17),
            (4, [12, 3], 4),
            (100000, [100000, 100000, 100000, 100000, 100000, 99999], 7),
        ],
    )
    def test_minimized_maximum(self, n: int, quantities: list[int], expected: int):
        result = run_minimized_maximum(Solution, n, quantities)
        assert_minimized_maximum(result, expected)
