import pytest

from leetcode_py import logged_test

from .helpers import assert_schedule_course, run_schedule_course
from .solution import Solution


class TestCourseScheduleIII:
    def setup_method(self):
        self.solution = Solution()

    @logged_test
    @pytest.mark.parametrize(
        "courses, expected",
        [
            ([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]], 3),
            ([[1, 2]], 1),
            ([[3, 2], [4, 3]], 0),
            ([[1, 2], [2, 3]], 2),
            ([[1, 1], [1, 2], [1, 3]], 3),
            ([[5, 5], [4, 6], [3, 7]], 2),
            ([[10, 10]], 1),
            ([[7, 5]], 0),
            ([[1, 2], [2, 2]], 1),
            ([[2, 3], [3, 4], [4, 5]], 1),
            ([[4, 4], [4, 8], [4, 12], [4, 16]], 4),
            ([[9, 10], [1, 2], [2, 3]], 2),
            ([[3, 3], [3, 3], [3, 3]], 1),
            ([[1, 4], [2, 4], [3, 4], [4, 4]], 2),
            ([[2, 9], [1, 10], [3, 4], [3, 12], [2, 7]], 5),
            ([[4, 10], [1, 4], [2, 7], [4, 9], [6, 5], [6, 3]], 3),
            ([[1, 1], [6, 7], [1, 9], [3, 10], [3, 2]], 3),
            ([[5, 3], [6, 6], [6, 9]], 1),
            ([[5, 9], [4, 11], [5, 12], [1, 6], [4, 10]], 3),
            ([[6, 3], [6, 12], [3, 5], [2, 8], [2, 2], [2, 8]], 4),
        ],
    )
    def test_schedule_course(self, courses: list[list[int]], expected: int):
        result = run_schedule_course(Solution, courses)
        assert_schedule_course(result, expected)
