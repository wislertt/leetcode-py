import pytest

from leetcode_py import logged_test

from .helpers import assert_find_min_arrow_shots, run_find_min_arrow_shots
from .solution import Solution


class TestMinimumNumberOfArrowsToBurstBalloons:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "points, expected",
        [
            ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
            ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
            ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
            ([[1, 2]], 1),
            ([[5, 6], [1, 2]], 2),
            ([[1, 10], [2, 9], [3, 8]], 1),
            ([[-2147483648, 2147483647]], 1),
            ([[1, 2], [2, 3]], 1),
            ([[1, 2], [3, 4]], 2),
            ([[0, 9], [1, 8], [2, 7], [3, 6]], 1),
            ([[1, 5], [2, 6], [3, 7], [8, 10]], 2),
            ([[9, 12], [1, 4], [5, 8], [4, 5]], 3),
            ([[3, 9], [7, 12], [3, 9]], 1),
            ([[1, 4], [4, 5], [5, 6], [6, 7]], 2),
            ([[-5, -1], [-3, 0], [2, 6]], 2),
        ],
    )
    def test_find_min_arrow_shots(self, points: list[list[int]], expected: int):
        result = run_find_min_arrow_shots(Solution, points)
        assert_find_min_arrow_shots(result, expected)
