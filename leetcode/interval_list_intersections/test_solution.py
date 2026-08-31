import pytest

from leetcode_py import logged_test

from .helpers import assert_interval_intersection, run_interval_intersection
from .solution import Solution


class TestIntervalListIntersections:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "first_list, second_list, expected",
        [
            (
                [[0, 2], [5, 10], [13, 23], [24, 25]],
                [[1, 5], [8, 12], [15, 24], [25, 26]],
                [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]],
            ),
            ([[1, 3], [5, 9]], [], []),
            ([], [[1, 3]], []),
            ([[0, 4], [6, 8]], [], []),
            ([[1, 2]], [[1, 2]], [[1, 2]]),
            ([[1, 3]], [[4, 6]], []),
            ([[1, 5]], [[2, 3]], [[2, 3]]),
            ([[1, 5]], [[5, 10]], [[5, 5]]),
            ([[1, 5]], [[2, 10]], [[2, 5]]),
            ([[3, 5], [9, 20]], [[1, 2], [6, 8], [21, 30]], []),
            ([[0, 10]], [[1, 2], [3, 4], [5, 6], [7, 8]], [[1, 2], [3, 4], [5, 6], [7, 8]]),
            ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),
            ([[1, 4], [8, 12]], [[2, 3], [5, 7], [9, 11]], [[2, 3], [9, 11]]),
        ],
    )
    def test_interval_intersection(
        self, first_list: list[list[int]], second_list: list[list[int]], expected: list[list[int]]
    ):
        result = run_interval_intersection(Solution, first_list, second_list)
        assert_interval_intersection(result, expected)
