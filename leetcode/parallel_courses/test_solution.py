import pytest

from leetcode_py import logged_test

from .helpers import assert_minimum_semesters, run_minimum_semesters
from .solution import Solution


class TestParallelCourses:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "n, relations, expected",
        [
            (3, [[1, 3], [2, 3]], 2),
            (3, [[1, 2], [2, 3], [3, 1]], -1),
            (2, [[1, 2]], 2),
            (2, [[2, 1]], 2),
            (4, [[1, 2], [2, 3], [3, 4]], 4),
            (4, [[1, 3], [1, 4], [2, 3], [2, 4]], 2),
            (3, [[1, 2], [2, 3]], 3),
            (5, [[2, 1], [3, 1], [4, 1], [1, 5]], 3),
            (4, [[1, 2], [1, 3], [3, 4], [2, 4]], 3),
            (5, [[1, 2], [1, 3], [2, 4], [3, 5], [4, 5]], 4),
            (6, [[1, 2], [1, 3], [2, 4], [3, 5], [4, 6], [5, 6]], 4),
            (4, [[1, 2], [2, 3], [3, 1]], -1),
            (5, [[1, 2], [3, 4], [2, 3]], 4),
            (6, [[1, 3], [2, 3], [3, 4], [5, 6], [4, 5]], 5),
            (3, [[2, 1], [3, 2]], 3),
            (7, [[1, 2], [1, 3], [2, 4], [3, 4], [4, 5], [5, 6], [5, 7]], 5),
            (4, [[1, 2], [1, 4], [3, 4]], 2),
            (6, [[3, 4]], 2),
            (4, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], 4),
            (3, [[1, 2], [1, 3], [2, 3]], 3),
            (4, [[3, 4]], 2),
            (6, [[1, 2], [1, 5], [2, 3], [2, 6], [3, 5], [5, 6]], 5),
            (3, [[1, 2], [2, 1], [3, 1], [3, 2]], -1),
            (6, [[1, 2], [1, 3], [1, 5], [2, 4], [3, 5], [5, 1], [5, 6], [6, 5]], -1),
            (5, [[1, 3], [1, 5], [2, 1], [2, 4], [3, 5], [4, 2], [4, 3], [5, 4]], -1),
            (6, [[1, 3], [1, 4], [1, 5], [2, 1], [3, 6], [4, 3]], 5),
        ],
    )
    def test_minimum_semesters(self, n: int, relations: list[list[int]], expected: int):
        result = run_minimum_semesters(Solution, n, relations)
        assert_minimum_semesters(result, expected)
