import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_time, run_minimum_time
from .solution import Solution


class TestParallelCoursesIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, relations, time, expected",
        [
            (1, [], [7], 7),
            (3, [[1, 3], [2, 3]], [3, 2, 5], 8),
            (5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5], 12),
            (2, [], [4, 9], 9),
            (3, [], [5, 1, 3], 5),
            (4, [[1, 2], [2, 3], [3, 4]], [1, 2, 3, 4], 10),
            (4, [[4, 3], [3, 2], [2, 1]], [2, 3, 4, 5], 14),
            (4, [[1, 3], [2, 3], [3, 4]], [2, 6, 1, 3], 10),
            (5, [[1, 4], [2, 4], [3, 5], [4, 5]], [3, 1, 2, 4, 2], 9),
            (6, [[1, 3], [2, 3], [3, 5], [4, 5], [5, 6]], [1, 2, 3, 4, 5, 6], 16),
            (7, [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]], [1, 2, 1, 2, 1, 2, 1], 7),
            (5, [[1, 5], [2, 5], [3, 5], [4, 5]], [10, 9, 8, 7, 1], 11),
            (6, [[5, 6], [1, 2], [1, 4]], [8, 7, 6, 1, 5, 5], 15),
            (6, [[2, 5], [1, 5], [4, 2]], [6, 10, 6, 10, 9, 5], 29),
            (2, [], [1, 10], 10),
            (4, [[2, 4], [1, 3]], [3, 5, 10, 7], 13),
            (3, [[2, 3], [1, 3]], [9, 4, 5], 14),
            (2, [], [6, 1], 6),
        ],
    )
    def test_minimum_time(self, n: int, relations: list[list[int]], time: list[int], expected: int):
        result = run_minimum_time(Solution, n, relations, time)
        assert_minimum_time(result, expected)
