import pytest

from leetcode_py import logged_test

from .helpers import assert_intersection_size_two, run_intersection_size_two
from .solution import Solution


class TestSetIntersectionSizeAtLeastTwo:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "intervals, expected",
        [
            ([[1, 3], [3, 7], [8, 9]], 5),
            ([[1, 3], [1, 4], [2, 5], [3, 5]], 3),
            ([[1, 2], [2, 3], [2, 4], [4, 5]], 5),
            ([[1, 2]], 2),
            ([[1, 2], [1, 2]], 2),
            ([[1, 3], [2, 3], [3, 4]], 3),
            ([[5, 6], [6, 7], [7, 8]], 4),
            ([[1, 10], [2, 3], [4, 5]], 4),
            ([[1, 2], [4, 5], [7, 8]], 6),
            ([[0, 1], [1, 2], [2, 3]], 4),
            ([[1, 4], [2, 4], [3, 4]], 2),
            ([[1, 100]], 2),
            ([[8, 9], [7, 8], [7, 9], [6, 7], [4, 7]], 4),
            ([[8, 9], [7, 8], [3, 7], [7, 9]], 4),
            ([[6, 9], [5, 6], [1, 2], [6, 9]], 5),
            ([[6, 8], [2, 7]], 2),
            ([[7, 9], [6, 7]], 3),
            ([[2, 6], [7, 9], [8, 9], [7, 8], [5, 8]], 5),
        ],
    )
    def test_intersection_size_two(self, intervals: list[list[int]], expected: int):
        result = run_intersection_size_two(Solution, intervals)
        assert_intersection_size_two(result, expected)
