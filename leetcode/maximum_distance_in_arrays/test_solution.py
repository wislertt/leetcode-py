import pytest

from leetcode_py import logged_test

from .helpers import assert_max_distance, run_max_distance
from .solution import Solution


class TestMaximumDistanceInArrays:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "arrays, expected",
        [
            ([[1, 2, 3], [4, 5], [1, 2, 3]], 4),
            ([[1], [1]], 0),
            ([[1, 4], [0, 5]], 4),
            ([[-2, -1], [-4, -3]], 3),
            ([[1], [2], [3]], 2),
            ([[1, 5], [2, 6], [0, 9]], 8),
            ([[-10], [-10], [-10]], 0),
            ([[0], [100]], 100),
            ([[1, 2], [1, 2]], 1),
            ([[-5, 0, 5], [1, 2, 3], [-100, 100]], 105),
            ([[7], [3], [10], [0]], 10),
        ],
    )
    def test_max_distance(self, arrays: list[list[int]], expected: int):
        result = run_max_distance(Solution, arrays)
        assert_max_distance(result, expected)
