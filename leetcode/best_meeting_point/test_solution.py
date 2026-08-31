import pytest

from leetcode_py import logged_test

from .helpers import assert_min_total_distance, run_min_total_distance
from .solution import Solution


class TestBestMeetingPoint:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]], 6),
            ([[1, 1]], 1),
            ([[1, 0], [0, 1]], 2),
            ([[1, 1], [1, 1]], 4),
            ([[0, 0, 0, 1], [1, 0, 0, 1]], 4),
            ([[1, 0, 1], [0, 1, 0], [1, 0, 1]], 8),
            ([[1, 0, 0, 0, 0, 0, 0, 0, 1]], 8),
            ([[1], [0], [0], [1]], 3),
            ([[0, 1], [1, 0], [0, 1]], 3),
            ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 12),
            ([[1, 0, 1, 0, 1], [0, 0, 0, 0, 0]], 4),
            ([[0, 0, 1], [0, 1, 0], [1, 0, 0]], 4),
        ],
    )
    def test_min_total_distance(self, grid: list[list[int]], expected: int):
        result = run_min_total_distance(Solution, grid)
        assert_min_total_distance(result, expected)
