import pytest

from leetcode_py import logged_test

from .helpers import assert_check_if_prerequisite, run_check_if_prerequisite
from .solution import Solution


class TestCourseScheduleIV:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "num_courses, prerequisites, queries, expected",
        [
            (2, [[1, 0]], [[0, 1], [1, 0]], [False, True]),
            (2, [], [[1, 0], [0, 1]], [False, False]),
            (3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]], [True, True]),
            (
                4,
                [[0, 1], [1, 2], [2, 3]],
                [[0, 3], [3, 0], [0, 2], [1, 3]],
                [True, False, True, True],
            ),
            (3, [[0, 1], [0, 2]], [[1, 2], [0, 1], [0, 2], [2, 1]], [False, True, True, False]),
            (5, [[3, 4], [2, 3], [1, 2], [0, 1]], [[0, 4], [4, 0], [0, 2]], [True, False, True]),
            (2, [[0, 1]], [[0, 1]], [True]),
            (2, [[0, 1]], [[1, 0]], [False]),
            (4, [], [[0, 1], [2, 3]], [False, False]),
            (3, [[0, 1], [1, 2]], [[0, 2], [2, 0], [1, 2]], [True, False, True]),
            (
                4,
                [[0, 1], [0, 2], [1, 3], [2, 3]],
                [[0, 3], [1, 2], [2, 1], [3, 0]],
                [True, False, False, False],
            ),
            (5, [[0, 1], [1, 2], [2, 3], [3, 4]], [[0, 4], [1, 4], [4, 0]], [True, True, False]),
            (
                6,
                [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],
                [[0, 5], [5, 0], [2, 4]],
                [True, False, True],
            ),
            (3, [[0, 1], [2, 1]], [[0, 2], [2, 0]], [False, False]),
            (4, [[0, 1], [0, 2], [1, 3], [2, 3], [0, 3]], [[0, 3], [3, 1]], [True, False]),
            (2, [[1, 0]], [[1, 0], [0, 1]], [True, False]),
        ],
    )
    def test_check_if_prerequisite(
        self,
        num_courses: int,
        prerequisites: list[list[int]],
        queries: list[list[int]],
        expected: list[bool],
    ):
        result = run_check_if_prerequisite(Solution, num_courses, prerequisites, queries)
        assert_check_if_prerequisite(result, expected)
