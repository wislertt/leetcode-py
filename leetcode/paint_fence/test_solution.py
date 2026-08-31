import pytest

from leetcode_py import logged_test

from .helpers import assert_num_ways, run_num_ways
from .solution import Solution


class TestPaintFence:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, k, expected",
        [
            (1, 1, 1),
            (1, 2, 2),
            (2, 2, 4),
            (2, 3, 9),
            (3, 2, 6),
            (3, 3, 24),
            (3, 1, 0),
            (4, 2, 10),
            (5, 2, 16),
            (7, 2, 42),
            (2, 1, 1),
            (4, 3, 66),
            (5, 3, 180),
            (10, 2, 178),
            (10, 3, 27408),
            (2, 10, 100),
            (7, 3, 1344),
            (4, 10, 9810),
            (6, 2, 26),
            (8, 2, 68),
        ],
    )
    def test_num_ways(self, n: int, k: int, expected: int):
        result = run_num_ways(Solution, n, k)
        assert_num_ways(result, expected)
